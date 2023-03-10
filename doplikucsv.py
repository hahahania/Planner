import os
import csv


def opening_file(file='dane.csv'):
    file = open(file, 'r')
    return csv.reader(file)


def new_info(list, file_name='dane.csv'):
    file = open(file_name, 'a')
    w = csv.writer(file)
    w.writerow(list)
    file.close()


def acsending_date(file_name='dane.csv'):
    r = opening_file(file_name)
    sorted_file = sorted(r, key=lambda x: (x[1], x[2]))
    new_file = open(file_name, 'w')
    w = csv.writer(new_file)
    w.writerows(sorted_file)


def decsending_date(file_name='dane.csv'):
    r = opening_file(file_name)
    sorted_file = sorted(r, key=lambda x: (x[1], x[2]), reverse=True)
    os.remove(file_name)
    new_file = open(file_name, 'w')
    w = csv.writer(new_file)
    w.writerows(sorted_file)


def acsending_update_date(file_name='dane.csv'):
    r = opening_file(file_name)
    sorted_file = sorted(r, key=lambda x: (x[-2], x[-1]))
    new_file = open(file_name, 'w')
    w = csv.writer(new_file)
    w.writerows(sorted_file)


def decsending_update_date(file_name='dane.csv'):
    r = opening_file(file_name)
    sorted_file = sorted(r, key=lambda x: (x[-2], x[-1]), reverse=True)
    os.remove(file_name)
    new_file = open(file_name, 'w')
    w = csv.writer(new_file)
    w.writerows(sorted_file)


def key_word(word, file_name='dane.csv'):
    r = opening_file(file_name)
    for line in r:
        for el in line:
            if word in el:
                return line


def remove_row(info1, info2, file_name='dane.csv'):
    r = opening_file(file_name)
    data = indicate_element(info1, info2, r)
    os.remove(file_name)
    new_file = open(file_name, 'w')
    w = csv.writer(new_file)
    w.writerows(correct_data(data))

# deleting event part 1


def indicate_element(info1, info2, reader):
    lines = list(reader)
    for index, element in enumerate(lines):
        for i in element:
            if info1 and info2 in i:
                lines[index][0] = 'DELETED'
    return lines

# deleting event part 2


def correct_data(data):
    for index, element in enumerate(data):
        for i in element:
            if 'DELETED' in i:
                del data[index]
    return data


def change_priority(name, date, time, new_info, file_name='dane.csv'):
    reader = opening_file(file_name)
    lines = list(reader)
    for index, element in enumerate(lines):
        if date and time and name in element:
            lines[index][3] = new_info
    os.remove(file_name)
    new_file = open(file_name, 'a')
    w = csv.writer(new_file)
    w.writerows(lines)


def change_date(name, date, time, new_date, new_time, file_name='dane.csv'):
    reader = opening_file(file_name)
    lines = list(reader)
    for index, element in enumerate(lines):
        if date and time and name in element:
            lines[index][1] = new_date
            lines[index][2] = new_time
    os.remove(file_name)
    new_file = open(file_name, 'a')
    w = csv.writer(new_file)
    w.writerows(lines)


def change_level(name, date, time, new_level, file_name='dane.csv'):
    reader = opening_file(file_name)
    lines = list(reader)
    for index, element in enumerate(lines):
        if date and time and name in element:
            lines[index][4] = new_level
    os.remove(file_name)
    new_file = open(file_name, 'a')
    w = csv.writer(new_file)
    w.writerows(lines)
