from setuptools import setup

setup(
    name = 'rcmh',
    description = 'Regression by clustering using Metropolis-Hastings',
    url = 'https://arxiv.org/abs/1811.12295',
    author = 'Simón Ramírez Amaya',
    author_email = 's.ramirez34@uniandes.edu.co',
    packages = [
        'rcmh'
    ],
    install_requires = [
        'pandas',
        'numpy',
        'scipy',
        'sklearn'
    ],
    include_package_data = True,
    package_data = {
        'rcmh': ['data/*']
    }
)
