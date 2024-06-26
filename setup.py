from setuptools import find_packages, setup

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->'list[str]':
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    packages=find_packages(),
    version='0.0.1',
    author='Akshay',
    author_email='kulkarni.akshayp@northeastern.edu',
    install_requires=get_requirements('requirements.txt'),
)
