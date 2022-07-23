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

    def soup(self, html):

        self.soup = BeautifulSoup(html, "html.parser")

    def num_of_fotos(self, num_of_fotos):
        self.num = num_of_fotos
        return self.num

    def __str__(self):
        return f'The name of the output file is {self.name} '

class Imagen:
    def __init__(self, origenName):
        self.origenName = origenName


    def __str__(self):
        return f'{self.origenName} Original Imagen'

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

def check_input(directory):
    return Path(directory).exists() and not (directory.endswith("/"))


def check_outputhtml(path, output_file):
    result = Output(output_file)


    if Path(output_file).exists():
        #print(dir(result.soup))
        with open(output_file, "r") as html:
            result.soup(html)
        header = result.soup.find_all('h1', string=path)

        if (path in [str(head.string) for head in header]):
            result.used_path = True
            print("Path already in html file")


        result.new_file = False
        numberof_as = len(result.soup.find_all('a'))
        last_fotito = result.num_of_fotos(numberof_as)
    else:
        result.num_of_fotos(0)

    return result


def process_pics(path, fotito_directory, result):
    return 'x'


def build_html(path, result, fotito_directory):
    print(result)
    if result.new_file:

        output = ['<!DOCTYPE html>\n',
                  '<html>\n',
                  '<head><title>Fotos de Dea </title></head>\n',
                  '<body>\n',
                  '<h1>' + path + '</h1>',
                  process_pics(path, fotito_directory, result),
                  '</body>\n',
                  '</html>\n',
                  ]

        output_str = ''.join(output)
        print(output_str)
    else:
        result.soup.new_tag("h1")

    return result




#########    Main program    ##########################

data, fotito_directory, output_file, path = load_constants()

if check_input(fotito_directory) and check_input(path):
    result = check_outputhtml(path, output_file)

    if not(result.used_path):
        print(build_html(path, result, fotito_directory))

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

