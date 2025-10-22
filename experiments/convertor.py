
import FreeSimpleGUI as fsg

label1 = fsg.Text('Enter the feet: ')
input_box1 = fsg.InputText()
label2 = fsg.Text('Enter the inches: ')
input_box2 = fsg.InputText()
convert_button = fsg.Button('Convert')

window = fsg.Window("Feet and Inches to Centimeters Converter",
                    layout=[[label1, input_box1], [label2, input_box2], [convert_button]])
window.read()
window.close()
