import PySimpleGUI as sg
from wydarzenie import Event
from poprawność import check_time, check_date
from doplikucsv import key_word, decsending_date, acsending_date, new_info, remove_row, decsending_update_date, acsending_update_date
from interfejs_operacje import priority, execution_time_and_date, change_execution_level


def main_page():
    main_layout = [[sg.Button('Show event', button_color='grey', key='-SHOW-')],
                   [sg.Button('Add new event', button_color='grey', key='-NEW-')],
                   [sg.Button('Delete event', button_color='grey',
                              key='-DELETE-')],
                   [sg.Button('Other operations', button_color='grey',
                              key='-OPERATIONS-')],
                   [sg.Button('Exit', button_color='grey', key='-EXIT-')]]
    window = sg.Window('LZdZ', layout=main_layout,
                       background_color='Black', modal=True)
    while True:
        event, values = window.read()
        if event == '-EXIT-' or event == sg.WIN_CLOSED:
            break
        if event == '-NEW-':
            new_event_window()
        if event == '-SHOW-':
            show_event()
        if event == '-DELETE-':
            delete_event()
        if event == '-OPERATIONS-':
            operations()


def show_event():
    show_event_layout = show_event_layout = [[sg.Text('Please enter keyword or date and time of the event')],
                                             [sg.Text('Date : '), sg.Input(
                                                 key='-DATE-'), sg.Text('Time : '), sg.InputText(key='-TIME-')],
                                             [sg.Text('Keyword : '),
                                              sg.InputText(key='-KEYWORD-')],
                                             [sg.Button('Display found event', key='-FOUNDEVENTS-'), sg.Button('Back to home page', key='-BACK-')]]
    window = sg.Window('Displaying event',
                       layout=show_event_layout, background_color='black')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-BACK-':
            window.close()
        elif event == '-FOUNDEVENTS-':
            str_time = values['-TIME-']
            str_date = values['-DATE-']
            if check_time(str_time) and check_date(str_date):
                if values['-KEYWORD-'] != '':
                    list_of_info = key_word(values['-KEYWORD-'])
                if values['-SHOWBYDATE-'] != '':
                    list_of_info = key_word(values['-SHOWBYDATE-'])
                info = '\n'.join(list_of_info)
                sg.Popup('Found event :',
                         info, background_color='black')
            else:
                sg.popup('Error',
                         'Incorrect form of data or time.\n Please try again')

####################################


def new_event_window():
    new_event_layout = [[sg.Text('Enter information about event')],
                        [sg.Text('Name', size=(50, 1)),
                        sg.InputText(key='-NAME-')],
                        [sg.Text('Date of execution (rrrr-mm-dd) or "lack" ',
                                 size=(50, 1)), sg.InputText(key='-DATE-')],
                        [sg.Text('Time of execution (hh:mm) or "lack" ',
                                 size=(50, 1)), sg.InputText(key='-VALIDATE-')],
                        [sg.Text('Priority of task (NO - normal, NI - low, WY - high)',
                                 size=(50, 1)), sg.InputText(key='-PRIORITY-')],
                        [sg.Text('Execution level (0-100)',
                                 size=(50, 1)), sg.InputText(key='-LEVEL-')],
                        [sg.Text('Category (eg. "work","home" etc.)',
                                 size=(50, 1)), sg.InputText(key='-CATEGORY-')],
                        [sg.Text('Describtion or leave empty space :',
                                 size=(50, 1)), sg.InputText(key='-DESCRIPTION-')],
                        [sg.Button('Submit', key='-CHECK-'), sg.Button('Back to home page', key='-BACK-')]]
    window = sg.Window('New event', layout=new_event_layout,
                       background_color='black')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-BACK-':
            window.close()
        elif event == '-CHECK-':
            str_time = values['-VALIDATE-']
            str_date = values['-DATE-']
            if check_time(str_time) and check_date(str_date):
                myevent = Event(values['-NAME-'], values['-DATE-'], values['-VALIDATE-'],
                                values['-PRIORITY-'], values['-LEVEL-'], values['-CATEGORY-'], values['-DESCRIPTION-'])
                sg.popup(
                    'New event', f'Created task :\n{str(myevent)}', background_color='black')
                myevent.update()
                new_info(myevent.creating_list())

            else:
                sg.popup('Error',
                         'Incorrect form of data or time.\n Please try again')


def operations():
    operations_layout = [[sg.Text('Available operations: ')],
                         [sg.Button('Priority change', key='-PRIORITY-')],
                         [sg.Button('Date and time of execution change',
                                    key='-CHANGEDATE-')],
                         [sg.Button('Execution level change', key='-LEVEL-')],
                         [sg.Text('Displaying events sorted by date and time of execution '),
                          sg.Button('Ascending', key='-DATEASCENDING-'), sg.Button('Descending', key='-DATEDESCENDING-')],
                         [sg.Text('Displaying events sorted by updated time and date'), sg.Button(
                             'Ascending', key='-ASC-UPDATE-DATE-'), sg.Button('Descending', key='-DESC-UPDATE-DATE-')],
                         [sg.Button('Back to home page', key='-BACK-')]]
    window = sg.Window('Operations', layout=operations_layout,
                       background_color='black')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-BACK-':
            window.close()
        elif event == '-DATEASCENDING-':
            acsending_date()
        elif event == '-DATEDESCENDING-':
            decsending_date()
        elif event == '-DESC-UPDATE-DATE-':
            decsending_update_date()
        elif event == '-ASC-UPDATE-DATE-':
            acsending_update_date()
        elif event == '-PRIORITY-':
            priority()
        elif event == '-CHANGEDATE-':
            execution_time_and_date()
        elif event == '-LEVEL-':
            change_execution_level()


def delete_event():
    delete_event_layout = [[sg.Text('Date and time of creating is needed to delete event')],
                           [sg.Text('Date of creating'),
                            sg.InputText(key='-DATE-')],
                           [sg.Text('Time of creating',),
                            sg.InputText(key='-TIME-')],
                           [sg.Button('Submit', key='-CHECK-'), sg.Button('Back to home page', key='-BACK-')]]
    window = sg.Window('Deleting event', layout=delete_event_layout,
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
                remove_row(str_date, str_time)
                sg.Popup('Event deleted successfuly ')
            else:
                sg.popup('Error',
                         'Incorrect form of data or time.\n Please try again')
