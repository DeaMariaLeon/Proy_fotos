from ver_fotos_enpath import get_names 
from visualizar_enpython import check_outputhtml
from pathlib import Path
from bs4 import BeautifulSoup


def test_names():
    
    path = "/Users/dealeon/Dir_de_prueba"
    
    assert set(get_names(path)) == set([('/Users/dealeon/Dir_de_prueba/X661.jpg', '/Users/dealeon/Dir_de_prueba'), 
                                        ('/Users/dealeon/Dir_de_prueba/test2.jpeg', '/Users/dealeon/Dir_de_prueba'), 
                                        ('/Users/dealeon/Dir_de_prueba/IMG_1660.JPG', '/Users/dealeon/Dir_de_prueba'), 
                                        ('/Users/dealeon/Dir_de_prueba/folder1/IMG_1626.JPG', '/Users/dealeon/Dir_de_prueba/folder1'), 
                                        ('/Users/dealeon/Dir_de_prueba/folder1/IMG_1623.JPG', '/Users/dealeon/Dir_de_prueba/folder1'), 
                                        ('/Users/dealeon/Dir_de_prueba/folder1/folder2/folder3/IMG_1622.JPG', '/Users/dealeon/Dir_de_prueba/folder1/folder2/folder3')])

def test_empty():
    path = "/Users/dealeon/Dir_de_prueba"
    assert set(get_names(path)) == []   

def test_names2():
    path = "/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos"    

       
    assert get_names(path)   ==    [('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/658.jpg', 
                                        '/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos'), 
                                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/659.jpg', 
                                    '/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos'), 
                                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/661.jpg', 
                                    '/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos'), 
                                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/660.jpg', 
                                    '/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos'), 
                                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/654.jpg', 
                                    '/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos'), 
                                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/655.jpg', 
                                    '/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos'), 
                                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/657.jpg', 
                                    '/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos'), 
                                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/656.jpg', 
                                    '/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos'), 
                                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/fotos2/654 copy.jpg', 
                                    '/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/fotos2'), 
                                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/fotos2/655 copy.jpg', 
                                    '/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/fotos2')]

def test_path():

    path = " "
    assert get_names(path) == "Correct your path"     


def test_output_newfile():
    path = "/Users/dealeon/Dir_de_prueba2"
    used_path = False 
    new_output = True 
    soup = None 
    num_of_fotos = 0
    last_fotito = 0
    assert (used_path, new_output, soup, num_of_fotos, last_fotito) == check_outputhtml(path, "x")

def test_output_existingfile():
    output_file = "output_copy.html" 
    if Path(output_file).exists(): 
        with open(output_file, "r") as html:
            soup = BeautifulSoup(html, "html.parser")
    else:
        soup = ""        
    path = "/Users/dealeon/Dir_de_prueba"
    used_path = False 
    new_output = False 
    num_of_fotos = 5
    last_fotito = 4
    assert (used_path, new_output, soup, num_of_fotos, last_fotito) == check_outputhtml(path, "output_copy.html")