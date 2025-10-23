import FreeSimpleGUI as sg
from zip_creator import make_archive

lable1 = sg.Text('select file to compress: ')
input_box1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose')

lable2 = sg.Text('select destination folder: ')
input_box2 = sg.Input()
choose_button2 = sg.FileBrowse('Choose')

compress_button = sg.Button('Compress')

window = sg.Window("File Compressor",
                   layout=[[lable1, input_box1], [choose_button1],
                           [lable2, input_box2], [choose_button2],
                           compress_button])

while True:
    event, values = window.read()
    filepaths = values['files'].split(';')
    folder = values['folder']
    make_archive(filepaths, folder)
window.read()
window.close()