import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lexicon_overlap_score",
    version="0.0.1",
    author="Felix Welter",
    author_email="felixwelter@gmail.com",
    description="Functions for calculation of the lexicon overlap score",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.rrz.uni-hamburg.de/bay1620/lexicon_overlap_score",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1',
        'pandas'
    ],
)
