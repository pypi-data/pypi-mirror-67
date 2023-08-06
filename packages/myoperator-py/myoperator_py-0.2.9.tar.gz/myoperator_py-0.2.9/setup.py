#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'statsd==3.3.0',
    'Django>=1.8.0',
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="MyOperator",
    author_email='dev@myoperator.co',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="CentralLog helps recording the logs by MyOperator standards",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='centrallog',
    name='myoperator_py',
    packages=['myoperator.centrallog', 'myoperator.apm'],
    package_dir={
        'myoperator.centrallog': 'myoperator/centrallog',
        'myoperator.apm': 'myoperator/apm/src'
    },
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/myoperator/centrallog',
    version='0.2.9',
    zip_safe=False,
)
