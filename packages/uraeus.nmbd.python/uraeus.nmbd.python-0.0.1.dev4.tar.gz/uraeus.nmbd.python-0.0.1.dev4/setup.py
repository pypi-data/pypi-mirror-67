import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

short_description = 'Numerical simulation environment of constrained multi-body systems in python.'

setuptools.setup(
    name = "uraeus.nmbd.python",
    namespace_packages=['uraeus', 'uraeus.nmbd'],
    version = "0.0.1.dev4",
    author = "Khaled Ghobashy",
    author_email = "khaled.ghobashy@live.com",
    description = short_description,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/khaledghobashy/uraeus-nmbd-python",
    packages = ['uraeus.nmbd'] + setuptools.find_packages(exclude=("tests",)),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    python_requires = '>=3.6',
    install_requires=[
          'uraeus.smbd>=0.0.1.dev3',
          'numpy',
          'scipy',
          'numba',
          'pandas'],
)