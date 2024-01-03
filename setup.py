from setuptools import find_packages, setup

def get_requirements(file_path: str):
    """
    Retrieve a list of requirements from a file.
    """
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()
        return [req for req in requirements if req != '-e .']

setup(
    name='mlproject',
    version='0.0.1',
    author='nagraj desai',
    author_email='nagrajdesaee@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=get_requirements('requirements.txt')
)
