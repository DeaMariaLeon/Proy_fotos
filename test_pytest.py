from ver_fotos_enpath import get_names 


def test_names():
    
    path = "/Users/dealeon/Dir_de_prueba"
    
    assert set(get_names(path)) == set([('/Users/dealeon/Dir_de_prueba/IMG_1660.JPG'),
                                ('/Users/dealeon/Dir_de_prueba/folder1/IMG_1626.JPG'),
                                ('/Users/dealeon/Dir_de_prueba/folder1/IMG_1623.JPG'),
                                ('/Users/dealeon/Dir_de_prueba/folder1/folder2/folder3/IMG_1622.JPG'),
                                ('/Users/dealeon/Dir_de_prueba/X661.jpg')])

def test_empty():
    path = "/Users/dealeon/Dir_de_prueba"
    assert set(get_names(path)) == []   

def test_names2():
    path = "/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos"    

       
    assert get_names(path)   ==    [('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/658.jpg'),
                     ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/659.jpg'),
                     ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/661.jpg'),
                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/660.jpg'),
                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/654.jpg'),
                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/655.jpg'),
                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/657.jpg'),
                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/656.jpg'),
                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/fotos2/654 copy.jpg'),
                    ('/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos/fotos2/655 copy.jpg')]

def test_path():

    path = " "
    assert get_names(path) == "Correct your path"                    