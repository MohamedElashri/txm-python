from setuptools import setup, find_packages

setup(
    name='txm',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click==8.0.3',
    ],
    entry_points={
        'console_scripts': [
            'txm=txm.cli:txm',
        ],
    },
)
