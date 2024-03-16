import os
import datetime
from re import split
from just_playback import Playback

# define a dictionary to store user input in it
d = {}

# functions to validate user inputs & store them to the 'd'
def title_validation(prompt):
    '''function to check input as a title'''
    while True:
        if prompt == 'Choose a title for alarm: ':
            title = input(prompt)
            if title == '':
                print('it can\'t be empty')
                continue
            else:
                d['title'] = title
                break
def time_validation(prompt):
    '''function to check input as a time'''
    os.system('cls')
    while True:
        try:
            time = int(input(prompt))
        except ValueError:
            print('Invalid! only enter a number')
            continue
        if prompt == 'Enter hour (HH): ' and time > 23:
            print('Invalid! hour must be in (0 - 23)')
            continue
        elif time >= 60:
            print('Enter a number less than 60')
            continue
        else:
            break
    return time   

def time_creator(alarm_hour, alarm_minute, alarm_second):
    '''function to create time object from provided HH, MM and SS'''
    d['time'] = datetime.time(alarm_hour, alarm_minute, alarm_second)

def occurrence_validation(prompt):
    '''function to check input as an occurrence'''
    os.system('cls')
    while True:
        print('select occurrence (only type it\'s number): ')
        print('1- Once')
        print('2- Daily')
        print('3- Custom')
        print()
        try:
            occurrence_option = int(input())
        except ValueError: 
            os.system('cls')   
            print('Only enter number!\n')
            continue
        if occurrence_option not in (1, 2, 3):
            os.system('cls')
            print('invalid choice!\n')
            continue
        else:
            break
    if occurrence_option == 1:
        d['occurrence'] = 'once'
    elif occurrence_option == 2:
        d['occurrence'] = 'daily'
    elif occurrence_option == 3:
        weekday_number = {
            '1': 'Sat',
            '2': 'Sun',
            '3': 'Mon',
            '4': 'Tue',
            '5': 'Wed',
            '6': 'Thu',
            '7': 'Fri'
        }
        os.system('cls')
        while True:
            print('\nchoose weekdays: ')
            print()
            print('1- Saturday')
            print('2- Sunday')
            print('3- Monday')
            print('4- Tuesday')
            print('5- Wednesday')
            print('6- Thursday')
            print('7- Friday')
            print()
            weekday = input('Enter weekday number seperated by comma: ')
            if weekday == '':
                os.system('cls')
                print('it can\'t be empty')
                continue
            splitted = split(',', weekday)
            if len(splitted) > 7:
                os.system('cls')
                print('Wrong! You must enter a number between 1-7')
                continue
            try:
                for item in splitted:
                    int(item)
            except ValueError:
                os.system('cls')
                print('Wrong! Just numbers accepted')
            else:
                weekday_list = weekday.split(',')
                weekday_dict = {}
                for WEEKDAY in weekday_list:
                    weekday_dict[WEEKDAY] = weekday_number[WEEKDAY]
                occurrence_custom = ",".join(list(weekday_dict.values()))
                d['occurrence'] = occurrence_custom
                print(d)
                break

sound_files = {
        1:('breakfast', r'.\data\breakfast.mp3'),
        2:('evening', r'.\data\evening.mp3'),
        3:('good life', r'.\data\good life.mp3'),
        4:('sportman', r'.\data\sportman.mp3')
    }

def sound_validation(prompt):
    '''Function to validate user choice as a sound for alarm'''
    os.system('cls')
    print(prompt)
    while True:
        print()
        print('1-breakfast')
        print('2-evening')
        print('3-good life')
        print('4-sportman')
        print()
        try:
            sound = int(input())
        except ValueError:
            os.system('cls')
            print('Invalid Character!')
            continue
        if sound not in range(1,5):
            os.system('cls')
            print('Number is ivalid! select correct one')
            continue
        else:
            while True:
                playback = Playback()
                try:
                    playback.load_file(sound_files[sound][1])
                except KeyError:
                    pass
                except ValueError:
                    pass
                playback.play()
                confirm = input("press 'y' or 'Y' to confirm; otherwise press a key... " )
                if confirm in ('y', 'Y'):
                    os.system('cls')
                    d['sound'] = sound
                    break
                else:
                    try:
                        sound = int(input("to hear one another press it\'s number... "))
                    except Exception:
                        pass
                    if sound not in range(1,5):
                        os.system('cls')
                        print('Number is ivalid! select correct one ')
                        continue
        break
        
def snooze_validation(prompt):
    '''Function to validate user input as snooze '''
    snooze_value = [3, 5, 10]
    os.system('cls')
    while True:
        print('choose the snooze by typing it\'s value: ')
        print()
        for number in snooze_value:
            print('- ' + str(number) + ' min')
        try:
            snooze = int(input())
        except ValueError:
            os.system('cls')
            print('Only enter a number!\n')
            continue
        if snooze not in snooze_value:
            os.system('cls')
            print('Invalid value! only enter values from the list below\n')
            continue
        else:
            os.system('cls')
            d['snooze'] = snooze
            break

