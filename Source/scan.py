import socket
from peewee import *
import preparation as pr
from playhouse.shortcuts import model_to_dict, dict_to_model
from termcolor import colored

db = SqliteDatabase("/home/frizik/Projects/ScanTelegramBot/Data/WhiteIps.db")

class ListIps(Model):
    town = CharField()
    ips = CharField()
    ports = CharField()

    class Meta:
        database = db  
        
ListIps.create_table()


def Check():
    CheckList = "" # Для проверки есть ли уже такой ip в базе
    for l in ListIps.select():
        CheckList = CheckList + l.ips + "\n"
        #print(l.ips)
    #print(colored(CheckList,"yellow")) # Cформированный чеклист
    return CheckList

def CheckForUniqueness(TownName,FinalIp,Port):
    CheckList = Check() #Полный пиздец но бота будет всё равно немного подргуому работать так тчо пока так сойдёт
    if FinalIp not in CheckList:
        #print("Новая уникальная строка")
        City = ListIps(town = TownName, ips = FinalIp, ports = Port)
        City.save() 
    '''else : 
        print("Найденна повторная строка!!!")'''


def ScanFunction(FinalIp,TownName):
    FinalIpPing = socket.socket()
    FinalIpPing.settimeout(0.01)

    LogPathNotWorked = "/home/frizik/Projects/ScanTelegramBot/Logs/pinglgN.txt"
    LogPathWorked = "/home/frizik/Projects/ScanTelegramBot/Logs/pinglg.txt"
    Port = 80

    try:
        FinalIpPing.connect((FinalIp, Port))
    except socket.error:
        RezultString = FinalIp + ":" + str(Port) + ": not work...next"
        pr.LogWriter(RezultString,LogPathNotWorked)
        pass
    else:
        RezultString = FinalIp + ":" + str(Port)
        CheckForUniqueness(TownName,FinalIp,Port)
        pr.LogWriter(RezultString,LogPathWorked)
        FinalIpPing.close