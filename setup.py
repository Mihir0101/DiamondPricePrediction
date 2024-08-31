from setuptools import find_packages,setup
from typing import List

E = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as obj:
        requirements=obj.readlines()
        requirements=[i.replace('\n','') for i in requirements]
        
        if E in requirements:
            requirements.remove(E)
        return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Mihir',
    author_email='parmarmihir31616@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
    )