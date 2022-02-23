
from ver_fotos_enpath import get_names
from bs4 import BeautifulSoup
from pathlib import Path
import os
from PIL import Image
from PIL.ExifTags import TAGS
import re
import json
#import sqlite3

def check_outputhtml(path, output_file):
    """Function to check if the output html file  exists and if the 
       path has not already been processed (used) before. 
       All the resized pictures and their links will be added on this output file.
       
       path: Root directory where I want to take all the pictures from.
       output_file: html file name   
       used_path: boolean, indicates that the path has been used before
       new_output: boolean to say that the html is a new document (will need a header)  
       soup: the whole html document
       num_of_fotos: number of pics in the document
       last_fotito: the number of the last small photo in html document 
             
    """
    if Path(output_file).exists(): 
        with open(output_file, "r") as html:
            soup = BeautifulSoup(html, "html.parser")
            heads = [tag.string for tag in soup.find_all('h1')] # finds all the headers (paths processed before)
            links = [l for l in soup.find_all('a')]    # finds all the <a href tags
            fotitos = [str(l.next_element) for l in links]
            #last_fotito = max([int(re.search('[0-9]+', f).group(0)) for f in fotitos])
            last_fotito = max([int(re.findall('[0-9]+', f)[-1]) for f in fotitos])
        used_path = path in heads #if the path exists, I don't want to process it again
        new_output = False 
    else:    
        used_path = False
        new_output = True
        links = []
        soup = None
        last_fotito = 0
    num_of_fotos = len(links)  
    return used_path, new_output, soup, num_of_fotos, last_fotito
    
def process_pics(path, fotito_directory, last_fotito):
    """ Process the pictures to resize them (to smaller resolution),
        gives them a new name and adds name and link to a variable that
        will be added to an html document
        path: root directory
        fotito_directory: where the small photos will be stored"""
    DATABASE = 'fotosDB.db'
    tmp_output = ''
    names = get_names(path) #get the entire name of all the pictures to process (including their path)
    last_fotito
    #con = sqlite3.connect(DATABASE)
    #cur = con.cursor()
    print("Control-C or Delete to interrupt\n")
    for x, i in enumerate(names):

        fotito_name = "fotito" + str(x + 1 + last_fotito) + ".jpg"
        img_string = fotito_directory + "/" + fotito_name
        img = Image.open(i)
        img.thumbnail((224,224), Image.ANTIALIAS)


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
        
        #cur.execute('INSERT INTO fotostb (name, link, object_id, directoryname_id) VALUES (?,?,?,?)', [fotito_name, i, 0, 0])
    #con.commit()
    #con.close()
    return tmp_output        

def write_soup(output_file, text):
    with open(output_file, "w") as f:
                    f.write(text)

def build_html(path, used_path, new_output, soup, output_file, last_fotito, fotito_directory):
    """ Function to build html document. If it is new, it needs a header.
        If it is not new, the path and the pictures with their links, need to be inserted.
    """ 
    if used_path: 
        print("Path already in html file")
        return
    
    output = ''
    if new_output:
        
        output = '<!DOCTYPE html>\n'
        output+= '<html>\n'
        output+= '<head><title>Fotos de Dea</title></head>\n'
        output+= '<body>\n'
        output+= '<h1>' + path + '</h1>'
        output+= process_pics(path, fotito_directory, last_fotito) 
        output+= '</body>\n'
        output+= '</html>\n'


    else:
        tag = soup.new_tag("h1")
        tag.string = path
        original_body=soup.body
        original_body.append(tag)
        tmp_output = process_pics(path, fotito_directory, last_fotito)
        soup2 = BeautifulSoup(tmp_output, "html.parser")
        soup.body.append(soup2)
        output = str(soup)
    return output           

def remove_subdirectory(path, soup, output_file):
    dir_to_remove = "<h1>" + path + "</h1>"
    soup2 = BeautifulSoup(dir_to_remove, "html.parser")
    tag = soup2.h1
    headers = soup.select("h1")
    
    if tag not in headers:
        print("Path not in", output_file)
        exit()

    pic_names = get_names(path)
    number_ofpics = len(pic_names)

    for h in headers:
        if h == tag:
            if len(headers) == 1:
                while True:
                    erase_file = input("Your html file is empty, do you want to erase it (Y/N)? ")
                    if erase_file.upper() == "Y":
                        print("Deleting ", output_file)
                        os.remove(output_file)
                        exit()
                    else:
                        exit()
            links_in_path = h.find_next_siblings("a", limit = number_ofpics)
            for l in links_in_path: 
                l.next_sibling.replace_with('')
                l.decompose()    
            h.decompose()

            write_soup(output_file, str(soup))    
            return 
    return    

try:
    with open("variables.json", "r") as json_file:
        data = json.load(json_file)
        fotito_directory = data["FOTITO_DIRECTORY"]
        print(os.getcwd())
        output_file = data["OUTPUT_FILE"]
        remove_flag = data["REMOVE_FLAG"] #Set to True to remove subirectories in output html file 
        path = data["PATH"]

except KeyError:
    print("Couldn't open variables.json file")

if Path(path).exists():
    used_path, new_output, soup, num_ofpics, last_fotito = check_outputhtml(path, output_file)

    if remove_flag:
        
        remove_subdirectory(path, soup, output_file)
    else:    
        output = build_html(path, used_path, new_output, soup, output_file, last_fotito, fotito_directory)
        if output:
            write_soup(output_file, output)
                   

