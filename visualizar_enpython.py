
from ver_fotos_enpath import get_names
import tensorflow as tf
from bs4 import BeautifulSoup
from pathlib import Path
import os
from PIL import Image
from PIL.ExifTags import TAGS



def check_outputhtml(path, output_file):
    """Function to check if the output html file  exists and if the 
       path has not already been processed (used) before. 
       All the resized pictures and their links will be added on this output file.
       
       path: Root directory where I want to take all the pictures from.
       output_file: html file name   
       used_path: boolean, indicates that the path has been used before
       new_output = boolean to say that the html is a new document (will need a header)  
       soup: the whole html document
       num_of_fotos = number of pics in the document
             
    """
    if Path(output_file).exists(): 
        with open(output_file, "r") as html:
            soup = BeautifulSoup(html, "html.parser")
            heads = [tag.string for tag in soup.find_all('h1')] # finds all the headers (paths processed before)
            links = [l for l in soup.find_all('a')]    # finds all the <a href tags
            
        used_path = path in heads #if the path exists, I don't want to process it again
        new_output = False 
    else:    
        used_path = False
        new_output = True
        links = []
        soup = None
    num_of_fotos = len(links)  
    return used_path, new_output, soup, num_of_fotos
    


def process_pics(path, num_ofpics):
    """ Process the pictures to resize them (to smaller resolution),
        gives them a new name and adds name and link to a variable that
        will be added to an html document
        path: root directory
        num_ofpics: number of pictures already in the html document"""

    tmp_output = ''
    names = get_names(path) #get the entire name of all the pictures to process (including their path)
    for x, i in enumerate(names):
        # foto = tf.io.read_file(i)
        # foto = tf.io.decode_jpeg(foto)
        # foto = tf.image.convert_image_dtype(foto, tf.float32)
        # foto = tf.image.resize(foto, [128, 128], preserve_aspect_ratio=True)
        # img = tf.keras.preprocessing.image.array_to_img(foto)
        
        img_string = "/Users/dealeon/Directorio_fotostf/fotito" + str(x + num_ofpics) + ".jpg"

        #img_string = "/Users/dealeon/Documents/proy_fotos/test_pic_orientation_Directorio_fotostf/fotito" + str(x + num_ofpics) + ".jpg"
        #img_string = "/Users/dealeon/Documents/Directorio_fotostf/fotito" + str(x + num_ofpics) + ".jpg"
        
        img = Image.open(i)
        img.thumbnail((128,128), Image.ANTIALIAS)
        
        try:
            exif = img.info['exif']
            img.save(img_string, exif = exif)  
        except KeyError:    
            img.save(img_string)

        
        i = i.replace(" ", "%20") #subdirectories (i) might have spaces, links get broken if not replaced with %20
        tmp_output += '<a href=' + i  +'><img src="' + img_string + '"></img></a>\n'
        
    return tmp_output        

def write_soup(output_file, text):
    with open(output_file, "w") as f:
                    f.write(text)

def build_html(path, used_path, new_output, soup, num_ofpics, output_file):
    """ Function to build html document. If it is new, it needs a header.
        If it is not new, the path and the pictures with their links, need to be inserted.
    """ 
    if used_path: 
        print("Path already on output.html file")
        return
    
    output = ''
    if new_output:
        
        output = '<!DOCTYPE html>\n'
        output+= '<html>\n'
        output+= '<head><title>Fotos de Dea</title></head>\n'
        output+= '<body>\n'
        output+= '<h1>' + path + '</h1>'
        output+= process_pics(path, num_ofpics) 
        output+= '</body>\n'
        output+= '</html>\n'
        with open(output_file, "w") as new_html:
            new_html.write(output)

    else:
        tag = soup.new_tag("h1")
        tag.string = path
        original_body=soup.body
        original_body.append(tag)
        tmp_output = process_pics(path, num_ofpics)
        soup2 = BeautifulSoup(tmp_output, "html.parser")
        soup.body.append(soup2)
        with open(output_file, "w") as f:
                    f.write(str(soup))
    return            

def remove_subdirectory(path, soup, output_file):
    dir_to_remove = "<h1>" + path + "</h1>"
    pic_names = get_names(path)
    number_ofpics = len(pic_names)
    #for p in pic_names:
        #os.remove(p)
        
    soup2 = BeautifulSoup(dir_to_remove, "html.parser")
    tag = soup2.h1
    headers = soup.select("h1")
    for h in headers:
        if h == tag:

            links_in_path = h.find_next_siblings("a", limit = number_ofpics)
            for l in links_in_path: l.decompose()    
            h.decompose()
            soup.smooth()
            write_soup(output_file, str(soup))    
            return 
    return    



#path = "/Users/dealeon/Pictures/Fotos/Noruega2009"
path = "/Users/dealeon/Dir_de_prueba"
#path = "/Users/dealeon/Dir_de_prueba2"
#path = "/Users/dealeon/Pictures/Fotos - library/2019"
#path = "/Users/dealeon/Pictures/Fotos - library/22 June 2015"
#path = "/Users/dealeon/Pictures/Fotos - library/5 April 2015"
#path = '../test_pic_orientation'
#path = '/Users/dealeon/Documents/proy_fotos/test_pic_orientation'
path  ='/Users/dealeon/Documents/My Pictures'
print(os.getcwd())
output_file = "output.html"
remove_flag = False

if Path(path).exists():
    used_path, new_output, soup, num_ofpics = check_outputhtml(path, output_file)

    if remove_flag:
        remove_subdirectory(path, soup, output_file)
    else:    
        build_html(path, used_path, new_output, soup, num_ofpics, output_file)



#print(soup.prettify())


