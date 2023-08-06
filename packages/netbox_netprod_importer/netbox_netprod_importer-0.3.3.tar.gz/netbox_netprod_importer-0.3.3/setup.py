#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

requirements = [
    "appdirs", "cachetools", "defusedxml", "lxml", "napalm", "netboxapi",
    "simplejson", "tqdm"
]
setup_requirements = [
    "pytest-runner",
]
test_requirements = [
    "pytest", "pytest-cov", "pytest-mock", "pynxos"
]

setup(
    author="Scaleway",
    author_email="contact@scaleway.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Microservice import into netbox devices in production",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords="netbox_netprod_importer",
    name="netbox_netprod_importer",
    packages=find_packages(include=["netbox_netprod_importer", "netbox_netprod_importer.*"]),
    package_data={
        "netbox_netprod_importer": ["templates/**"]
    },
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://gitlab.infra.online.net/network/netbox_netprod_importer",
    version="0.3.3",
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'netbox-netprod-importer = netbox_netprod_importer.__main__:parse_args',
        ],
    }
)
