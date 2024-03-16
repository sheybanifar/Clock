
from validation import d
from os import system, path
import pickle


class Alarm:
    def __init__(self, title, time, occurrence, sound, snooze, status):
        self.title = title
        self.time = time
        self.occurrence = occurrence
        self.sound = sound
        self.snooze = snooze
        self.status = status
    
    def __str__(self):
        return self.title
    
def add_alarm(title, time, occurrence, sound, snooze):
        '''takes alarm parameters and creating alarm instance'''
        with open('alarmdb.bin', 'rb') as alarmdb_reader:
            try:
                alarm_list = pickle.load(alarmdb_reader)
            except EOFError:
                alarm_list = []
        with open('alarmdb.bin', 'wb') as alarmdb_updater:
            new_alarm = Alarm(title, time, occurrence, sound, snooze, status='ON')
            alarm_list.append(new_alarm)
            pickle.dump(alarm_list, alarmdb_updater)
        system('cls')
        print('new alarm successfully created.\n')
            
