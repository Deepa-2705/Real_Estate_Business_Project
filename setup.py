from setuptools import find_packages,setup
from typing import List

HYPHON_DOT_E='-e .'

def get_requirements(file_paths:str)->List[str]:
    requirements=[]
    with open(file_paths)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHON_DOT_E in requirements:
            requirements.remove(HYPHON_DOT_E)

        return requirements


setup(
    name='RealEstateBusiness',
    version='0.0.1',
    author='Deepa Gupta',
    email="deepagupta35795@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)