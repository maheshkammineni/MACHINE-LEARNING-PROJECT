from setuptools import setup
from typing import List

# Decalaring the variables for setup functions

Project_Name = "Housing_Predictor"
VERSION = "0.0.1"
Author = "Mahesh Kammineni"
Description = "This is the first complete project housing price prediction"
Pacakges = ['housing']
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list():
    with open("requirements.txt", "r") as requirements_file:
        return [line.strip() for line in requirements_file if not line.startswith("-e .")]# return is going to return a list which contain name of libraries.
    
    

setup(
name = Project_Name,
version= VERSION ,
author =Author,
description = Description,
packages = Pacakges,
install_requires = get_requirements_list()

)


    