"""Setup file."""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='psiz',
    version='0.3.0',
    description='Toolbox for inferring psychological embeddings.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    author='Brett D. Roads',
    author_email='brett.roads@gmail.com',
    license='Apache Licence 2.0',
    packages=['psiz'],
    python_requires='>=3, <3.8',
    install_requires=[
        'tensorflow>=2', 'scipy', 'pandas', 'scikit-learn',
        'matplotlib', 'tensorflow-probability', 'numexpr', 'pillow'
    ],
    include_package_data=True,
    url='https://github.com/roads/psiz',
    download_url='https://github.com/roads/psiz/archive/v0.3.0.tar.gz'
)
