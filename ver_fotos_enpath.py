
import pathlib
import re

def path_func(my_path):
    return pathlib.Path(my_path)

def get_names(my_path):
    path = path_func(my_path)
    if path.exists() and path.is_dir():
        pattern = '.*JPG$|.JPEG$'
        regex = re.compile(pattern, flags=re.IGNORECASE)
        names = [(f.as_posix(), f.parent.as_posix())  for f in path.rglob("*") if (f.is_file() and regex.search(f.name))]
        return names    
    else :
        return "Correct your path"

#string = get_names("/Users/dealeon/Documents/Practice II/Proy_Fotos/fotos") 
#print(string)