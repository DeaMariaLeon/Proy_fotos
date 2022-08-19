import pathlib
import re
import pytest
import shutil
import pprint

DIRECTORY1 = "Dir_de_prueba1/"#, "Dir_de_prueba2/folder1/folder2/folder3")

DIRECTORY2 = "Dir_de_prueba2/"

"""
DIRECTORY2 =[('/Users/dealeon/Dir_de_prueba/X661.jpg', '/Users/dealeon/Dir_de_prueba'),
                                        ('/Users/dealeon/Dir_de_prueba/test2.jpeg', '/Users/dealeon/Dir_de_prueba'),
                                        ('/Users/dealeon/Dir_de_prueba/IMG_1660.JPG', '/Users/dealeon/Dir_de_prueba'),
                                        ('/Users/dealeon/Dir_de_prueba/folder1/IMG_1626.JPG', '/Users/dealeon/Dir_de_prueba/folder1'),
                                        ('/Users/dealeon/Dir_de_prueba/folder1/IMG_1623.JPG', '/Users/dealeon/Dir_de_prueba/folder1'),
                                        ('/Users/dealeon/Dir_de_prueba/folder1/folder2/folder3/IMG_1622.JPG', '/Users/dealeon/Dir_de_prueba/folder1/folder2/folder3')]

"""
def path_func(my_path):
    return pathlib.Path(my_path)

def get_names(path):
    """Get all the photos from my_path
    """
    if isinstance(path, (pathlib.WindowsPath, pathlib.PosixPath)):
        path = pathlib.Path(path)
    else:
        if isinstance(path, str):
            path = pathlib.Path(path)

    if path.exists() and path.is_dir():
        pattern = '.*JPG$|.JPEG$'
        regex = re.compile(pattern, flags=re.IGNORECASE)
        names = [(f.as_posix(), f.parent.as_posix())  for f in path.rglob("*") if (f.is_file() and regex.search(f.name))]
        return names
    else :
        return "Correct your path"
    return

@pytest.fixture(scope="session")
def create_dir1(tmp_path_factory):

    newtemp_dir = tmp_path_factory.mktemp(DIRECTORY1, numbered=False)
    yield newtemp_dir
    shutil.rmtree(str(newtemp_dir), ignore_errors=False)
    #shutil.rmtree(str(newtemp_dir.parent), ignore_errors=False)


def test_1(create_dir1):
    file = '/Users/dealeon/Dir_deprueba1/X661.jpg'
    print("test 1", create_dir1)
    print(file)

    path_with_file = shutil.copy(file, create_dir1, follow_symlinks=True)
    print(path_with_file)
    print(create_dir1.parent)

    print(get_names(create_dir1))
    print(type(create_dir1))

    assert get_names(create_dir1) == [(path_with_file, str(create_dir1))]

    return


@pytest.fixture(scope="session")
def create_dir2(tmp_path_factory):

    newtemp_dir0 = tmp_path_factory.mktemp( DIRECTORY2, numbered=False)
    #newtemp_dir = newtemp_dir0 / "folder1"

    newtemp_dir = newtemp_dir0 / "folder1"
    newtemp_dir.mkdir()
    newtemp_dir2 = newtemp_dir / "folder2"
    newtemp_dir2.mkdir()
    yield newtemp_dir0
    shutil.rmtree(str(newtemp_dir0), ignore_errors=False)
    #shutil.rmtree(str(newtemp_dir0.parent), ignore_errors=False)

def test_2(create_dir2):
    file = '/Users/dealeon/Dir_deprueba1/X661.jpg'
    print(create_dir2)
    print(file)


    path_with_file = shutil.copy(file, create_dir2/"folder1/", follow_symlinks=True)
    path_with_file2 = shutil.copy(file, create_dir2/"folder1/folder2", follow_symlinks=True)
    print(path_with_file)
    print(f'{path_with_file2=}')
    print(create_dir2.parent)

    print(get_names(create_dir2))
    print(type(create_dir2))

    assert get_names(create_dir2) == [(path_with_file, str(create_dir2/"folder1/"))]

    return


#if __name__=="__main__":
#    test_1(create_dir)


