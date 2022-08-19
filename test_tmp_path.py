import pathlib
import re
import pytest
import shutil
import pprint
from ver_fotos_enpath import get_names

DIRECTORY1 = "Test_dir1/"#, "Test_dir2/folder1/folder2/folder3")

DIRECTORY2 = "Test_dir2/"

"""
DIRECTORY2 =[('""Dir_de_prueba/X661.jpg', '""Dir_de_prueba'),
                                        ('""Dir_de_prueba/test2.jpeg', '""Dir_de_prueba'),
                                        ('""Dir_de_prueba/IMG_1660.JPG', '""Dir_de_prueba'),
                                        ('""Dir_de_prueba/folder1/IMG_1626.JPG', '""Dir_de_prueba/folder1'),
                                        ('""Dir_de_prueba/folder1/IMG_1623.JPG', '""Dir_de_prueba/folder1'),
                                        ('""Dir_de_prueba/folder1/folder2/folder3/IMG_1622.JPG', '""Dir_de_prueba/folder1/folder2/folder3')]

"""

@pytest.fixture(scope="module")
def create_dir1(tmp_path_factory):

    newtemp_dir = tmp_path_factory.mktemp(DIRECTORY1, numbered=False)
    yield newtemp_dir
    shutil.rmtree(str(newtemp_dir), ignore_errors=False)

def test_1(create_dir1):
    file = '/Users/dealeon/Dir_deprueba1/X661.jpg'
    path_with_file = shutil.copy(file, create_dir1, follow_symlinks=True)

    assert get_names(create_dir1) == [(path_with_file, str(create_dir1))]

    return


@pytest.fixture(scope="session")
def create_dir2(tmp_path_factory):

    newtemp_dir0 = tmp_path_factory.mktemp( DIRECTORY2, numbered=False)
    newtemp_dir = newtemp_dir0 / "folder1"
    newtemp_dir.mkdir()
    newtemp_dir2 = newtemp_dir / "folder2"
    newtemp_dir2.mkdir()
    yield newtemp_dir0
    shutil.rmtree(str(newtemp_dir0), ignore_errors=False)
    #shutil.rmtree(str(newtemp_dir0.parent), ignore_errors=False)

def test_2(create_dir2):
    file = '/Users/dealeon/Dir_deprueba1/X661.jpg'
    path_with_file1 = shutil.copy(file, create_dir2/"folder1/", follow_symlinks=True)
    path_with_file2 = shutil.copy(file, create_dir2/"folder1/folder2", follow_symlinks=True)

    assert get_names(create_dir2) == [(path_with_file1, str(create_dir2/"folder1/")), (path_with_file2, str(create_dir2/"folder1/folder2")) ]

    return


#if __name__=="__main__":
#    test_1(create_dir)


