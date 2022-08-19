#!/usr/bin/env python

from ver_fotos_enpath import get_names
from bs4 import BeautifulSoup
from pathlib import Path
import os
from PIL import Image
import json


class Output:
    """Class containing all the information of the output html file
       we want to generate or modify
    """
    new_file = True
    used_path = False
    num_of_fotos = 0

    def __init__(self, name):
        self.name = name

    def soup(self, html):

        self.soup = BeautifulSoup(html, "html.parser")

    def __str__(self):
        return f'The name of the output file is {self.name} '


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
    """Function to check if the output html file  exists and if the
       path has not already been processed (used) before.
       All the resized pictures and their links will be added on this output file.

       Inputs
       ------
       path: string
           Root directory to read all the pictures.
       output_file: string
           html file name

       Returns
       -------
       result: class

    """

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
        result.num_of_fotos = len(result.soup.find_all('a'))

    return result


def process_pics(path, fotito_directory, result):
    """ Rescale the pictures to smaller resolution,
        gives them a new name and adds name and link to a variable that
        will be added to an html document

        Inputs
        ------
        path: string
            Root directory to read all the pictures.
        fotito_directory: string
            Diretory where the scaled photos will be stored
        result: class

        Returns
        -------
        tmp_output: string (html file)
    """
    tmp_output = ''
    names = get_names(path)
    print("Control-C or Delete to interrupt\n")
    for x, i in enumerate(names):

        fotito_name = "fotito" + str(x + 1 + result.num_of_fotos) + ".jpg"
        img_string = fotito_directory + "/" + fotito_name
        img = Image.open(i[0])
        img.thumbnail((224,224))

        #picture orientation info is in the exif info of the JPEG file is this exif info has been created by the camera
        #So we retrieve this information from the uncompressed JPEG and save it into the compressed one if this information exists

        try:

            exif = img.info['exif']
            img.save(img_string, exif = exif)
        except KeyError:
            #If the exif information is not available in the original JPEG file, then there will be a dictionary Key Error
            img.save(img_string)
        j = i[0].replace(" ", "%20") #subdirectories (i) might have spaces, links get broken if not replaced with %20
        tmp_output += '<a href=' + j  +'><img src="' + img_string + '"></img></a>\n'

    return tmp_output


def write_soup(output_file, text):
    with open(output_file, "w") as f:
                    f.write(text)


def build_html(path, result, fotito_directory):
    """ Function to build html document. If it is new, it needs a header.
        If it is not new, the path and the pictures with their links, need to be inserted.
    """
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
        result.soup(output_str)

    else:
        tag = result.soup.new_tag("h1")
        tag.string = path
        result.soup.body.append(tag)
        tmp_output = process_pics(path, fotito_directory, result)
        soup2 = BeautifulSoup(tmp_output, "html.parser")
        result.soup.body.append(soup2)

    return str(result.soup)

#########    Main program    ##########################

data, fotito_directory, output_file, path = load_constants()

if check_input(fotito_directory) and check_input(path):
    result = check_outputhtml(path, output_file)

    if not(result.used_path):
        output = build_html(path, result, fotito_directory)
        print(result)
        write_soup(output_file, output)

else:
    print("Please check your path names in variables.json file")


#if __name__ == '__main__':

#    file = Output('output_test.html')

