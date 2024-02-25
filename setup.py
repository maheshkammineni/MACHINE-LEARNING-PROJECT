from setuptools import setup
from typing import List

# Decalaring the variables for setup functions

Project_Name = "Housing_Predictor"
VERSION = "0.0.1"
Author = "Mahesh Kammineni"
Description = "This is the first complete project housing price prediction"
Pacakges = ['housing']
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    "This function going to return list of requirement mention in requirements.txt file"

    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines() # return is going to return a list which contain name of libraries.
    
    

setup(
name = Project_Name,
version= VERSION ,
author =Author,
description = Description,
packages = Pacakges,
install_requires = get_requirements_list()

)


    