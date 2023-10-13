from setuptools import setup, find_packages

setup(
    name='txm',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        # Add any other dependencies you might have
    ],
    entry_points={
        'console_scripts': ['txm=txm.cli:txm'],
    },
    author='Mohamed Elashri',
    email='txm@elashri.com',
    description='A tmux helper utility',
    #long_description=open('../README.md').read(),
    #long_description_content_type='text/markdown',
    url='https://github.com/MohamedElashri/txm', 
)
