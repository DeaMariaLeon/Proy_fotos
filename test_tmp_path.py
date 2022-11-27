import pathlib
import pytest
import shutil
from ver_fotos_enpath import get_names

DIRECTORY1 = "Test_dir1/"

DIRECTORY2 = "Test_dir2/"


@pytest.fixture(scope="module")
def create_dir1(tmp_path_factory):
    newtemp_dir = tmp_path_factory.mktemp(DIRECTORY1, numbered=False)
    yield newtemp_dir
    shutil.rmtree(str(newtemp_dir), ignore_errors=False)


def test_1(create_dir1):
    file = 'X661.jpg'
    path_with_file = shutil.copy(file, create_dir1, follow_symlinks=True)
    assert get_names(create_dir1) == [(path_with_file, str(create_dir1))]
    return


@pytest.fixture(scope="session")
def create_dir2(tmp_path_factory):

    newtemp_dir0 = tmp_path_factory.mktemp(DIRECTORY2, numbered=False)
    newtemp_dir = pathlib.Path(newtemp_dir0 / "folder1/folder2")
    newtemp_dir.mkdir(parents=True)
    yield newtemp_dir
    shutil.rmtree(str(newtemp_dir0), ignore_errors=False)


def test_2(create_dir2):
    file = 'X661.jpg'
    path_with_file1 = shutil.copy(file, create_dir2/"folder1/",
                                  follow_symlinks=True)
    path_with_file2 = shutil.copy(file, create_dir2,
    #path_with_file2 = shutil.copy(file, create_dir2/"folder1/folder2",
                                  follow_symlinks=True)

    assert get_names(create_dir2) == [(path_with_file1,
                                      str(create_dir2/"folder1/")),
                                      (path_with_file2,
                                      str(create_dir2/"folder1/folder2"))]

    return
