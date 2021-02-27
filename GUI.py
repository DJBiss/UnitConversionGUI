# ---------------------------------- Imports --------------------------------- #
import PySimpleGUI as sg
from Conversion import convert

# ---------------------------------------------------------------------------- #
#         Hello! This is a simple unit conversion app using PySimpleGUI        #
# ---------------------------------------------------------------------------- #


# ------------------------------ Colour Settings ----------------------------- #
sg.theme('DarkBlue12')
sg.theme_background_color('#43506c')
sg.theme_text_element_background_color('#43506c')
sg.theme_input_background_color('#43506c')
sg.theme_input_text_color('#e9e9eb')

# ------------------------------ Variable Setup ------------------------------ #
box_size = (25,1)
drop_size = (15,1)
button_size = (16,1)

length_str = ['Picometres', 'Nanometres', 'Micrometres', 'Millimetres', 'Metres', 'Kilometres', 'Inches', 'Feet', 'Yards', 'Miles', 'Nautical Miles']
area_str = ['Square Millimetres', 'Square Centimetres', 'Square Metres', 'Square Kilometres', 'Square Inches', 'Square Feet', 'Square Yards', 'Square Miles', 'Ares', 'Hectares', 'Acres']
vol_str = ['Millilitres', 'Cubic Centimetres', 'Centilitres', 'Cubic Metres', 'Litres', 'Cubic Feet', 'Pints', 'Gallons']
mass_str = ['Milligrams', 'Grams', 'Kilograms', 'Tonnes (Metric Tons)', 'Kilotonnes', 'Megatonnes', 'Ounces', 'Pounds', 'Stone']
time_str = ['Microseconds', 'Milliseconds', 'Seconds', 'Minutes', 'Hours', 'Days', 'Weeks', 'Months', 'Years']
speed_str = ['Metres/Second', 'Kilometres/Hour', 'Miles/Hour', 'Knots']

# --------------------------- End of Variable Setup -------------------------- #


# ----------------------------- Button Functions ----------------------------- #
def domain_button(button_text):
    return sg.Button(button_text, enable_events=True, size=button_size, button_color=('#e9e9eb on #3d619b'))

def change_converter(list, header):
    window['-UNIT_IN-'](values=list) # update the unit list to the 'domain' we are interested in
    window['-UNIT_OUT-'](values=list) # update the unit list to the 'domain' we are interested in
    window['-IN_VAL-']('') # reset the user input, so that we don't convert our old number to the new unit
    window['-HEADER-'](f'{header} Conversion') # change the header text to reflect the current domain of units

# ---------------------------------------------------------------------------- #

# ----------------------------- Window Definition ---------------------------- #
layout = [[sg.Text('Length Conversion', key='-HEADER-', size=(40,0), justification='c', font=('Franklin Gothic Book', 14, 'bold'))],
          [sg.HorizontalSeparator()],
          [sg.Input(key='-IN_VAL-', size=(22,1), justification='c', border_width=0), sg.Text('Input a number to convert', key='-OUT_VAL-', size=box_size, justification='c')],
          [sg.Combo(length_str, key='-UNIT_IN-', size=drop_size, enable_events=True), sg.Combo(length_str, key='-UNIT_OUT-', size=drop_size, enable_events=True)],
          [sg.Button('Convert', size=button_size), sg.Button('Close', size=button_size)],
          [sg.HorizontalSeparator()],
          [domain_button('Length'), domain_button('Area'), domain_button('Volume')],
          [domain_button('Mass'), domain_button('Time'), domain_button('Speed') ]]

window = sg.Window('Unit Converter App', layout, grab_anywhere=True, element_justification='c', element_padding=(10,10), font=('Franklin Gothic Book', 12))

# ---------------------------------------------------------------------------- #
while True:
    event, values = window.read()
    if event in (None, 'Close', sg.WIN_CLOSED):
        break
    if event in ('Convert', '-UNIT_IN-', '-UNIT_OUT-'):
        try:
            input_val = float(values['-IN_VAL-'])
            convert_from = values['-UNIT_IN-'].upper()
            convert_to = values['-UNIT_OUT-'].upper()
            ans = convert(input_val, convert_from, convert_to)
            
            window['-OUT_VAL-'].update(str(ans))

        except ValueError:
            window['-OUT_VAL-'].update("Input a number to convert")

    if event == 'Length':
        change_converter(length_str, 'Length')
    if event == 'Area':
        change_converter(area_str, 'Area')
    if event == 'Volume':
        change_converter(vol_str, 'Volume')
    if event == 'Mass':
        change_converter(mass_str, 'Mass')
    if event == 'Time':
        change_converter(time_str, 'Time')
    if event == 'Speed':
        change_converter(speed_str, 'Speed')

window.close()
exit()