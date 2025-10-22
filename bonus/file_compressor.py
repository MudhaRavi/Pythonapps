import FreeSimpleGUI as sg

lable1 = sg.Text('select file to compress: ')
input_box1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose File')

lable2 = sg.Text('select file to compress: ')
input_box2 = sg.Input()
choose_button2 = sg.FileBrowse('Choose File')

window = sg.Window("File Compressor",
                   layout=[[lable1, input_box1], [choose_button1],
                           [lable2, input_box2], [choose_button2]])
window.read()
window.close()