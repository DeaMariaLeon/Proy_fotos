#!/usr/bin/env python

from unicodedata import name
from ver_fotos_enpath import get_names
from bs4 import BeautifulSoup
from pathlib import Path
import os
from PIL import Image
from PIL.ExifTags import TAGS
import re
import json

class Output:

    new_file = True
    used_path = False

    def __init__(self, name):
        self.name = name

    def soup(self):
        with open(self.name, "r") as html:
            self.soup = BeautifulSoup(html, "html.parser")

    def num_of_fotos(self, num_of_fotos):
        self.num = num_of_fotos
        return self.num

    def used(self):
        self.used_path = True

    def __str__(self):
        return f'The name of the output file is {self.name} '

class Imagen:
    def __init__(self, origenName):
        self.origenName = origenName


    def __str__(self):
        return f'{self.origenName} Original Imagen'


def check_input(directory):
    return Path(directory).exists() and not (directory.endswith("/"))


def check_outputhtml(path, output_file):
    result = Output(output_file)
    result.soup()

    if Path(output_file).exists():
        #print(dir(result.soup))
        header = result.soup.find_all('h1', string=path)



        result.new_file = False
        numberof_as = len(result.soup.find_all('a'))
        last_fotito = result.num_of_fotos(numberof_as)


    print(result.soup())
    print(last_fotito)

    return

def load_constants():
    try:
        with open("variables.json", "r") as json_file:
            data = json.load(json_file)
            fotito_directory = data["SCALED_PHOTO_DIRECTORY"] #This should not have a final "/"
            print(os.getcwd())
            output_file = data["OUTPUT_FILE"]
            path = data["PHOTO_ORIGIN_PATH"] #This should not have a final "/"
    except KeyError:
        print("Could not open variables.json file")
    return data, fotito_directory, output_file, path

data, fotito_directory, output_file, path = load_constants()

if check_input(fotito_directory) and check_input(path):
    check_outputhtml(path, output_file)


"""
if __name__ == '__main__':

    print('here')

    file = Output('output_test.html')
    print(file)
    print(file.new_file)
    file.flag()
    print(file.new_file)
    file.num_of_fotos(3)
    print(file.num)

"""

