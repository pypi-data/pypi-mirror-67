
# -*- coding: utf-8 -*-
# Copyright 2020 The PsiZ Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Module of utility functions.

Classes:
    ProgressBar: A progress bar displayed in the terminal.

Functions:
    pairwise_matrix: Return the similarity matrix characterizing
        the embedding.
    similarity_matrix: Return the similarity matrix characterizing
        the embedding. Deprecated use pairwise_matrix.
    matrix_comparison: Compute correlation between two matrices.
    compare_models: Compare the similarity structure between two
        embedding models.
    rotation_matrix: Returns a two-dimensional rotation matrix.
    affine_transformation: Performs an affine transformation on a set
        of points.
    procrustean_solution: Attempt to allign two embeddings by finding
        a Procrustean solution.
"""

import copy
import datetime
import time

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import pearsonr
from sklearn.metrics import r2_score


def assess_convergence(
        obs, model, n_stimuli, n_dim, n_partition=10, n_back=2, n_shuffle=3,
        n_restart=50, score='r2', verbose=0):
    """Evaluate if a sufficient number of observations have been collected.

    In general, more observations improve model inference. However,
    there are generally diminishing returns to collecting more data.
    This function determines the impact of adding a little bit more
    data. Ideally, you should have sufficient data that adding more
    does not dramatically alter the structure of the inferred
    embedding. Structural changes are assessed by comparing the pair-
    wise similarity matrix of different embeddings.

    Arguments:
        obs: An Observations object.
        model: A PsychologicalEmbedding object.
        n_stimuli: The number of stimuli.
        n_dim: The dimensionality of the embedding.
        n_partition (optional): The number of partitions.
        n_back (optional):  The number of partitions to evaluate. Can
            be [1, n_partition-1].
        n_shuffle (optional): The number of times to shuffle and
            repeat tha analysis.
        n_restart (optional): The number of restarts to use when
            fitting the embeddings.
        score (optional): Measure to use when comparing two similarity
            matrices.
        verbose (optional): Verbosity.

    Returns:
        summary: Dictionary of results.
            n_trial_array: Number of trials in each set.

    """
    # Check arguments.
    n_back = np.maximum(n_back, 1)
    n_back = np.minimum(n_back, n_partition-1)

    n_trial_array = np.linspace(0, obs.n_trial, n_partition + 1)
    n_trial_array = np.ceil(n_trial_array[1:]).astype(int)

    val = np.ones([n_shuffle, n_partition]) * np.nan
    for i_shuffle in range(n_shuffle):
        if verbose > 0:
            print('  Shuffle {0}'.format(i_shuffle + 1))
        # Randomize observations.
        rand_idx = np.random.permutation(obs.n_trial)
        obs = obs.subset(rand_idx)

        # Infer embeddings for an increasing number of observations.
        first_part = True
        emb_list = [None] * n_partition
        for i_part in range(n_partition-n_back-1, n_partition):
            include_idx = np.arange(0, n_trial_array[i_part])
            curr_obs = obs.subset(include_idx)
            curr_emb = model(n_stimuli, n_dim=n_dim)
            curr_emb.fit(curr_obs, n_restart=n_restart, verbose=verbose)
            emb_list[i_part] = curr_emb

            if not first_part:
                simmat_0 = similarity_matrix(
                    emb_list[i_part - 1].similarity,
                    emb_list[i_part - 1].z
                )
                simmat_1 = similarity_matrix(
                    emb_list[i_part].similarity, emb_list[i_part].z
                )
                val[i_shuffle, i_part] = matrix_comparison(
                    simmat_0, simmat_1, score=score
                )
                if verbose > 0:
                    print('    {0} | measure: {1:.2f}'.format(
                        i_part, val[i_shuffle, i_part]
                    ))
            else:
                first_part = False

    return {"n_trial_array": n_trial_array, "val": val, "measure": score}


def similarity_matrix(similarity_fn, z):
    """Return a pairwise similarity matrix.

    Returns:
        A 2D array where element s_{i,j} indicates the similarity
            between the ith and jth stimulus.

    """
    n_stimuli = z.shape[0]

    xg = np.arange(n_stimuli)
    a, b = np.meshgrid(xg, xg)
    a = a.flatten()
    b = b.flatten()

    z_a = z[a, :]
    z_b = z[b, :]
    simmat = similarity_fn(z_a, z_b)
    simmat = simmat.reshape(n_stimuli, n_stimuli)
    return simmat


pairwise_matrix = similarity_matrix


def matrix_comparison(mat_a, mat_b, score='r2', elements='upper'):
    """Return a comparison score between two square matrices.

    Arguments:
        mat_a: A square matrix.
        mat_b: A square matrix the same size as mat_a
        score (optional): The type of comparison to use.
        elements (optional): Which elements to use in the computation.
            The options are upper triangular elements (upper), lower
            triangular elements (lower), or off-diagonal elements
            (off).

    Returns:
        The comparison score.

    Notes:
        'r2'
        When computing R^2 values of two similarity matrices, it is
        assumed, by definition, that the corresponding diagonal
        elements are the same between the two matrices being compared.
        Therefore, the diagonal elements are not included in the R^2
        computation to prevent inflating the R^2 value. On a similar
        note, including both the upper and lower triangular portion
        does not artificially inflate R^2 values for symmetric
        matrices.

    """
    n_row = mat_a.shape[0]
    idx_upper = np.triu_indices(n_row, 1)
    idx_lower = np.triu_indices(n_row, 1)
    if elements == 'upper':
        idx = idx_upper
    elif elements == 'lower':
        idx = idx_lower
    elif elements == 'off':
        idx = (
            np.hstack((idx_upper[0], idx_lower[0])),
            np.hstack((idx_upper[1], idx_lower[1])),
        )
    else:
        raise ValueError(
            'The argument to `elements` must be "upper", "lower", or "off".')

    if score == 'pearson':
        score, _ = pearsonr(mat_a[idx], mat_b[idx])
    elif score == 'r2':
        rho, _ = pearsonr(mat_a[idx], mat_b[idx])
        score = rho**2
        # score = r2_score(mat_a[idx], mat_b[idx])
    elif score == 'mse':
        score = np.mean((mat_a[idx] - mat_b[idx])**2)
    else:
        raise ValueError(
            'The provided `score` argument is not valid.')
    return score


def compare_models(
        model_a, model_b, group_id_a=0, group_id_b=0, score='r2',
        elements='upper'):
    """Compare two psychological embeddings.

    Arguments:
        model_a:  A psychological embedding model.
        model_b:  A psychological embedding model.
        group_id_a (optional):  A particular group ID to use when
            computing the similarity matrix for model_a.
        group_id_b (optional):  A particular group ID to use when
            computing the similarity matrix for model_b.

    Returns:
        R^2 value of the two similarity matrices derived from each
            embedding.

    """
    def sim_func_a(z_q, z_ref):
        return model_a.similarity(z_q, z_ref, group_id=group_id_a)

    def sim_func_b(z_q, z_ref):
        return model_b.similarity(z_q, z_ref, group_id=group_id_b)

    simmat_a = similarity_matrix(sim_func_a, model_a.z)
    simmat_b = similarity_matrix(sim_func_b, model_b.z)

    r_squared = matrix_comparison(
        simmat_a, simmat_b, score=score, elements=elements
    )
    return r_squared


def rotation_matrix(theta):
    """Return 2D rotation matrix.

    Arguments:
        theta: Scalar value indicating radians of rotation.

    """
    return np.array((
        (np.cos(theta), -np.sin(theta)),
        (np.sin(theta), np.cos(theta)),
    ))


def affine_transformation(z, params):
    """Return affine transformation of 2D points.

    Arguments:
        z: Original set of points.
            shape = (n_point, 2)
        params: Transformation parameters denoting x translation,
            y translation, rotation (in radians), scaling, and flip
            factor.
            shape = (5,)

    """
    x = params[0]
    y = params[1]
    translation = np.array((x, y))
    theta = params[2]
    s = params[3]
    f = params[4]
    x = f * x
    r = rotation_matrix(theta)
    z_trans = s * (np.matmul(z, r) + translation)
    return z_trans


def procrustean_solution(z_a, z_b, n_restart=10):
    """Align the two embeddings using an affine transformation.

    Arguments:
        z_a: A 2D embedding.
            shape = (n_point, 2)
        z_b: A 2D embedding.
            shape = (n_point, 2)
        n_restart (optional): A scalar indicating the number of
            restarts for the optimization routine.

    Returns:
        z_c: An affine transformation of z_b that is maximally aligned
            with z_a.
        params: The affine transformation parameters.

    """
    def objective_fn(params, z_a, z_b):
        z_c = affine_transformation(z_b, params)
        # Loss is defined as the MSE of L2 distance.
        loss = np.mean(np.sum((z_a - z_c)**2, axis=1))
        return loss

    params_best = np.array((0., 0., 0., 1.))
    loss_best = np.inf
    for _ in range(n_restart):
        (x0, y0) = np.random.rand(2)
        theta0 = 2 * np.pi * np.random.rand(1)
        s0 = 2 * np.random.rand(1)
        # Perform a flip on some restarts.
        f0 = 1.
        if np.random.rand(1) < .5:
            f0 = -1.
        params0 = np.array((x0, y0, theta0, s0, f0))
        bnds = (
            (None, None),
            (None, None),
            (0., 2*np.pi),
            (0., None),
            (f0, f0)
        )
        res = minimize(objective_fn, params0, args=(z_a, z_b), bounds=bnds)
        params_candidate = res.x
        loss_candidate = res.fun
        if loss_candidate < loss_best:
            loss_best = loss_candidate
            params_best = params_candidate
        z_c = affine_transformation(z_b, params_best)
    return (z_c, params_best)


class ProgressBar(object):
    """Display a progress bar in terminal."""

    def __init__(
            self, total, prefix='', decimals=1, length=100,
            fill='█'):
        """Initialize.

        Arguments:
            iteration: Integer indicating current iteration.
            total: Integer indicating total iterations.
            prefix (optional): String that is used as prefix.
            suffix (optional): String that is used as suffix.
            decimals (optional): Integer indicating a positive number
                of decimals in percent complete.
            length (optional): Integer indicating the character length
                of the progress bar.
            fill (optional): String indicating the bar fill character.

        """
        self.total = total
        self.prefix = prefix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.n_call = 0
        self.start_s = 0
        self.total_s = 0

    def _start(self):
        """Start timer."""
        self.start_s = time.time()

    def _stop(self):
        """Stop time."""
        self.total_s = time.time() - self.start_s

    def update(self, iteration):
        """Update progress bar to display current iteration."""
        # Start time if this is the first call.
        if self.n_call == 0:
            self._start()
        self.n_call = self.n_call + 1

        percent = ("{0:." + str(self.decimals) + "f}").format(
            100 * (iteration / float(self.total))
        )

        elapsed_time = time.time() - self.start_s
        if iteration == 0:
            time_per_iter = 0.0
        else:
            time_per_iter = elapsed_time / iteration

        eta_s = np.round((self.total - iteration) * time_per_iter)
        ett_s = np.round(self.total * time_per_iter)

        eta_str = str(datetime.timedelta(seconds=eta_s))
        ett_str = str(datetime.timedelta(seconds=ett_s))

        filledLength = int(self.length * iteration // self.total)
        bar = self.fill * filledLength + '-' * (self.length - filledLength)
        print(
            '\r    {0} |{1}| {2}% | ETA: {3} | ETT: {4}'.format(
                self.prefix, bar, percent, eta_str, ett_str
            ), end='\r'
        )
        # Print a new line on completion.
        if iteration == self.total:
            self._stop()
            print()
