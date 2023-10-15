from setuptools import setup, find_packages

setup(
    name='txm',
    version='0.1',
    packages=find_packages(),
    author='Mohamed Elashri',
    author_email='txm@elashri.com',
    description='A CLI utility for tmux',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MohamedElashri/txm',
    keywords= ['tmux', 'cli', 'utility', 'terminal', 'multiplexer', 'terminal multiplexer', 'terminal multiplexing'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
