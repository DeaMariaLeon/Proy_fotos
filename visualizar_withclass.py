from unicodedata import name
from ver_fotos_enpath import get_names
from bs4 import BeautifulSoup
from pathlib import Path
import os
from PIL import Image


class Output:

    new_file = True
    used_path = False

    def __init__(self, name, html_string):
        self.name = name

        self.html_string = html_string

    def num_of_fotos(self, num_of_fotos):
        self.num = num_of_fotos

    def flag(self):
        self.new_file = False

    def used(self):
        self.used_path = True

    def __str__(self):
        return f'The name of the output file is {self.name} '

class Imagen:
    def __init__(self, origenName):
        self.origenName = origenName


    def __str__(self):
        return f'{self.origenName} Original Imagen'


if __name__ == '__main__':

    print('here')

    file = Output('output_test.html', '<!DOCTYPE html>\n')
    print(file)
    print(file.new_file)
    file.flag()
    print(file.new_file)
    file.num_of_fotos(3)
    print(file.num)

