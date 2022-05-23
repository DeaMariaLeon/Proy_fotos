# Proy_fotos

This tool reads all photos from a subdirectory and creates a html file. The html file will have scaled versions of the photos,
and links to the original file.

It uses python 3.10.4 and the libraries included in file <mark>requirements.txt</mark>

The main program to run is <mark>visualizar_enpython.py</mark>.
The path to the original photos, the subdirectory to keep the scaled-down photos have to be entered in the file <mark>variables.json</mark>
Also the name of the html file to be created is in variables.json file.

If you delete the output html file, you should delete the scaled-down photos from their subdirectory.

The program will not work with paths already included in the output html file. But this html file can be deleted and created again running the main <mark>visualizar_enpython.py</mark>