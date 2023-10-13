from setuptools import setup, find_packages

setup(
    name='txm',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'txm = txm.cli:txm',
        ],
    },
    author='Mohamed Elashri',
    author_email='txm@elashri.com',
    description='A CLI utility for tmux',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MohamedElashri/txm',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
