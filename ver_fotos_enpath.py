
import pathlib
import re

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


