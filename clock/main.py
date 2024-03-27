import os
from alarm_class import Alarm
from validation import *
import pickle

os.system('cls')
while True:
    print('--=::Welcome to Clock::=--\n')
    print('1-Alarm')
    print('2-Timer')
    print('3-Stopwatch\n')
    try:
        choice = int(input('press number from above: '))
    except ValueError:
        os.system('cls')
        print('it must be a number!')
        continue
    if choice not in (1, 2, 3):
            os.system('cls')
            print('Only Enter 1, 2 or 3')
            continue
    else:
        if choice == 1:         # Entry => Alarm
            os.system('cls')
            while True:
                print('**ALARM**\n')
                try:
                    with open('alarmdb.bin', 'rb') as alarmdb_reader:   # Loading saved alarms
                        try:
                            alarms = pickle.load(alarmdb_reader)    # List of alarm instances
                            # improve printing alarm lists in a nice justified columns
                            column1 = max(len(f'{alarm_number}- {alarm_item.title}') for alarm_item in alarms for alarm_number in range(1, len(alarms) + 1)) + 3
                            column2 = max(len(f'{alarm_item.time.hour}:{alarm_item.time.minute}:{alarm_item.time.second}') for alarm_item in alarms) + 3
                            column3 = max(len(f'{alarm_item.occurrence}') for alarm_item in alarms) + 3
                            column4 = max(len(f'{alarm_item.status}') for alarm_item in alarms) + 3
                            print('Title'.ljust(column1), 'Up Time'.ljust(column2), 'Occurrence'.ljust(column3), 'Status'.ljust(column4))
                            print('-'*column1, '-'*column2, '-'*column3, '-'*column4)
                            for alarm_item in alarms:
                                print(f'{alarms.index(alarm_item) + 1}- {alarm_item.title}'.ljust(column1), f'{alarm_item.time.hour}:{alarm_item.time.minute}:{alarm_item.time.second}'.ljust(column2), f'{alarm_item.occurrence}'.ljust(column3), f'{alarm_item.status}'.ljust(column4))
                        except (EOFError, IndexError):
                            print('0 alarm was found.')
                except FileNotFoundError:
                    with open('alarmdb.bin', 'wb') as alarmdb_creator:
                        print('0 alarm was found.')
                        pass
                print()
                print('[1] Add new alarm')
                print('[2] Modify existing')
                print('* use "Modify existing" to turn the alarm on or off')
                print('* press "Q" or Control + C to back main menu')
                try:
                    add_modify_input = input('press correct option: ')
                except ValueError:
                    os.system('cls')
                    print('Press correct value!\n')
                    continue
                except KeyboardInterrupt:
                    os.system('cls')
                    break
                if add_modify_input in ('q', 'Q'):
                    os.system('cls')
                    break
                elif add_modify_input not in ('1','2'):
                    print('Only enter 1 or 2 from options!\n')
                elif add_modify_input == '1':
                    # call validating functions to validate user inputs
                    title_validation('Choose a title for alarm: ')
                    alarm_hour = time_validation('Enter hour (HH): ')
                    alarm_minute = time_validation('Enter minute (MM): ')
                    alarm_second = time_validation('Enter second (SS): ')
                    time_creator(alarm_hour, alarm_minute, alarm_second)
                    occurrence_validation('Set occurrence for alarm: ')
                    sound_validation('Select the sound just by pressing it\'s number:')
                    snooze_validation('Select the snooze time: ')
                    Alarm.add_alarm(d['title'], d['time'], d['occurrence'], d['sound'], d['snooze'])      # instantiation the alarm
                elif add_modify_input == '2':
                    while True:
                        modify_input = input('Enter alarm title: ')
                        if modify_input == '':
                            print('it can\'t be empty!')
                            continue
                        else:
                            break
                    for alarm in alarms:
                        if alarm.title == modify_input:
                            while True:
                                if alarm.status == 'ON':
                                    turn_off_prompt = input("turn off? press 'y' to yes, 'n' to no: ")
                                    if turn_off_prompt == '':
                                        os.system('cls')
                                        print('it can\t be empty')
                                        continue
                                    elif turn_off_prompt in ('y', 'Y', 'Yes', 'yes', 'YES'):
                                        alarm.status = 'OFF'
                                        with open('alarmdb.bin', 'wb') as alarmdb_updater:
                                            pickle.dump(alarms, alarmdb_updater)
                                        break
                                    elif turn_off_prompt in ('n', 'N', 'no', 'No', 'NO'):
                                        break
                                    else:
                                        os.system('cls')
                                        print('invalid entry')
                                        continue
                                else:
                                    turn_off_prompt = input("turn on? press 'y' to yes, 'n' to no: ")
                                    if turn_off_prompt == '':
                                        os.system('cls')
                                        print('it can\t be empty')
                                        continue
                                    elif turn_off_prompt in ('y', 'Y', 'Yes', 'yes', 'YES'):
                                        alarm.status = 'ON'
                                        with open('alarmdb.bin', 'wb') as alarmdb_updater:
                                            pickle.dump(alarms, alarmdb_updater)
                                        break
                                    elif turn_off_prompt in ('n', 'N', 'no', 'No', 'NO'):
                                        break
                                    else:
                                        os.system('cls')
                                        print('invalid entry')
                                        continue
                            while True:     # busy wait until get a valid input
                                alarm_del_prompt = input('Do you want to delete alarm? (press "y" to Yes and "n" to No) ')
                                if alarm_del_prompt in ('y', 'Y', 'Yes', 'yes', 'YES'):
                                    del alarms[alarms.index(alarm)]
                                    break
                                elif alarm_del_prompt in ('n', 'N', 'no', 'No', 'NO'):
                                    try:
                                        input('press Enter to continue and, press "Control + C" to exit modifying process...')
                                    except KeyboardInterrupt:
                                        break
                                    title_validation('Choose a title for alarm: ')
                                    alarm_hour = time_validation('Enter hour (HH): ')
                                    alarm_minute = time_validation('Enter minute (MM): ')
                                    alarm_second = time_validation('Enter second (SS): ')
                                    time_creator(alarm_hour, alarm_minute, alarm_second)
                                    occurrence_validation('Set occurrence for alarm: ')
                                    sound_validation('Select the sound just by pressing it\'s number:')
                                    snooze_validation('Select the snooze time: ')
                                    alarm.title = d['title']
                                    alarm.time = d['time']
                                    alarm.occurrence = d['occurrence']
                                    alarm.sound = d['sound']
                                    alarm.snooze = d['snooze']
                                    break
                                else:
                                    print('Incorrect! try again')
                                    continue
                            with open('alarmdb.bin', 'wb') as alarmdb_updater:  # Update modified alarm on database
                                pickle.dump(alarms, alarmdb_updater)
                    os.system('cls')
                    print('Alarm not found! please try again\n')
        elif choice == 2:       # Entry => Timer
            pass
        elif choice == 3:       # Entry => Stopwatch
            pass
            
        
        
        
    
