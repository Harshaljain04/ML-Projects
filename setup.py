from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path)->List[str]:
    '''
    this function will return the list of requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

setup(
    name='ML-Projects',
    version='0.0.1',
    author='Harshal',
    author_email='harshaljn04@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)