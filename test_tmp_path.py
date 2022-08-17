import pathlib
import re
import pytest
import shutil
import pprint



DIRECTORY1 = "Dir_de_prueba1/"

MYFILES =[('/Users/dealeon/Dir_de_prueba/X661.jpg', '/Users/dealeon/Dir_de_prueba'),
                                        ('/Users/dealeon/Dir_de_prueba/test2.jpeg', '/Users/dealeon/Dir_de_prueba'),
                                        ('/Users/dealeon/Dir_de_prueba/IMG_1660.JPG', '/Users/dealeon/Dir_de_prueba'),
                                        ('/Users/dealeon/Dir_de_prueba/folder1/IMG_1626.JPG', '/Users/dealeon/Dir_de_prueba/folder1'),
                                        ('/Users/dealeon/Dir_de_prueba/folder1/IMG_1623.JPG', '/Users/dealeon/Dir_de_prueba/folder1'),
                                        ('/Users/dealeon/Dir_de_prueba/folder1/folder2/folder3/IMG_1622.JPG', '/Users/dealeon/Dir_de_prueba/folder1/folder2/folder3')]





def path_func(my_path):
    return pathlib.Path(my_path)



def get_names(path):
    """Get all the photos from my_path
    """

    #path = path_func(my_path)
    if path.exists() and path.is_dir():
        pattern = '.*JPG$|.JPEG$'
        regex = re.compile(pattern, flags=re.IGNORECASE)
        names = [(f.as_posix(), f.parent.as_posix())  for f in path.rglob("*") if (f.is_file() and regex.search(f.name))]
        return names
    else :
        return "Correct your path"
    return

@pytest.fixture(scope="session")
def create_dir(tmp_path_factory):

    return tmp_path_factory.mktemp(DIRECTORY1, numbered=False)


def test_1(create_dir):
    file = '/Users/dealeon/Dir_deprueba1/X661.jpg'

    #shutil.copytree(p.parent, cache_dir, dirs_exist_ok=True)
    path_with_file = shutil.copy(file, create_dir, follow_symlinks=True)
    print(path_with_file)
    print(create_dir.parent)
    print(create_dir)
    print(get_names(create_dir))

    assert False

    return
##TODO
# Quitar de get_names y visualizar_enpython que corran pathlib.Path - poner if my_path es ya un pathlib.Path, no lo corra
# Por que no borra los dir temporales???

#if __name__=="__main__":
#    test_1(create_dir)


