from setuptools import setup
from hound import __version__

with open('README.md') as r:
    long_description = r.read()

setup(
    name = 'hound',
    version = __version__,
    packages = [
        'hound',
    ],
    description = 'A FireCloud database extension',
    url = 'https://github.com/getzlab/hound',
    author = 'Aaron Graubert - Broad Institute - Cancer Genome Computational Analysis - Getz Lab',
    author_email = 'aarong@broadinstitute.org',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    install_requires = [
        "google-cloud-storage>=1.20.0",
        "google-auth>=1.6.3",
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
    ],
    license="BSD3"
)
