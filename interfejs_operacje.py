import PySimpleGUI as sg
from poprawność import check_date, check_time
from doplikucsv import change_priority, change_date, change_level


def priority():
    priority_layout = [[sg.Text('To change [riority enter]:')],
                       [sg.Text('Date of creating'),
                        sg.InputText(key='-DATEOFCREATING-')],
                       [sg.Text('Time of creating'),
                        sg.InputText(key='-TIMEOFCREATING-')],
                       [sg.Text('Name'),
                        sg.InputText(key='-NAME-')],
                       [sg.Button('Submit', key='-CHECK-'), sg.Button('Back to home page', key='-BACK-')]]
    window = sg.Window('Priority change', layout=priority_layout,
                       background_color='black')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-BACK-':
            window.close()
        elif event == '-CHECK-':
            str_date = values['-DATEOFCREATING-']
            str_time = values['-TIMEOFCREATING-']
            if check_time(str_time) and check_date(str_date):
                priority_second_window(values['-NAME-'], str_date, str_time)
            else:
                sg.popup('Error',
                         'Incorrect form of data or time.\n Please try again')


def priority_second_window(name, date, time):
    new_layout = [[sg.Text('Please enter new priority:'),
                   sg.InputText(key='-PRIORITY-')],
                  [sg.Button('Change priority', key='-CHANGE-')]]
    new_window = sg.Window('Priority change',
                           layout=new_layout, background_color='black')
    while True:
        event, values = new_window.read()
        if event == sg.WIN_CLOSED:
            new_window.close()
        elif event == '-CHANGE-':
            change_priority(name, date, time, values['-PRIORITY-'])
            new_window.close()
            sg.popup('Change applied succesfully')


def execution_time_and_date():
    execution_date_layout = [[sg.Text('To change date and time of execution enter:')],
                             [sg.Text('Date of creating'),
                              sg.InputText(key='-DATE-')],
                             [sg.Text('Time of creating'), sg.InputText(
                                 key='-TIME-')],
                             [sg.Text('Name'),
                              sg.InputText(key='-NAME-')],
                             [sg.Button('Submit', key='-CHECK-'), sg.Button('Back to home page', key='-BACK-')]]
    window = sg.Window('Change of execution date', layout=execution_date_layout,
                       background_color='black')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-BACK-':
            window.close()
        elif event == '-CHECK-':
            str_date = values['-DATE-']
            str_time = values['-TIME-']
            if check_time(str_time) and check_date(str_date):
                change_date_second_window(
                    values['-NAME-'], values['-DATE-'], values['-TIME-'])
            else:
                sg.popup('Error',
                         'Incorrect form of data or time.\n Please try again')


def change_date_second_window(name, date, time):
    new_layout = [[sg.Text('Please enter new data:')],
                  [sg.Text('Execution date : '),
                   sg.InputText(key='-NEWDATE-')],
                  [sg.Text('Execution time : '),
                   sg.InputText(key='-NEWTIME-')],
                  [sg.Button('Change date and time ', key='-CHANGE-')]]
    new_window = sg.Window('Change of date and time',
                           new_layout, background_color='black')

    while True:
        event, values = new_window.read()
        if event == sg.WIN_CLOSED:
            new_window.close()
        elif event == '-CHANGE-':
            change_date(name, date, time,
                        values['-NEWDATE-'], values['-NEWTIME-'])
            new_window.close()
            sg.popup('Time and date changed succesfully')


def change_execution_level():
    execution_level_layout = [[sg.Text('To change level of execution enter:')],
                              [sg.Text('Date of creating'),
                               sg.InputText(key='-DATE-')],
                              [sg.Text('Time of creating'),
                               sg.InputText(key='-TIME-')],
                              [sg.Text('Name'),
                               sg.InputText(key='-NAME-')],
                              [sg.Button('Submit', key='-CHECK-'), sg.Button('Back to home page', key='-BACK-')]]
    window = sg.Window('Change execution level', layout=execution_level_layout,
                       background_color='black')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-BACK-':
            window.close()
        elif event == '-CHECK-':
            str_date = values['-DATE-']
            str_time = values['-TIME-']
            if check_time(str_time) and check_date(str_date):
                change_level_second_window(
                    values['-NAME-'], values['-DATE-'], values['-TIME-'])
            else:
                sg.popup('Error',
                         'Incorrect form of data or time.\n Please try again')


def change_level_second_window(name, date, time):
    new_layout = [[sg.Text('Please enter new execution level : '), sg.InputText(key='-LEVEL-')],
                  [sg.Button('Change', key='-CHANGE-')]]
    new_window = sg.Window('CHange execution level',
                           new_layout, background_color='black')
    while True:
        event, values = new_window.read()
        if event == sg.WIN_CLOSED:
            new_window.close()
        elif event == '-CHANGE-':
            change_level(name, date, time, values['-LEVEL-'])
            new_window.close()
            sg.popup('Execution level changed succesfully')
