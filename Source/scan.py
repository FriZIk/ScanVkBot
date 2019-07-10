import socket
from peewee import *
import preparation as pr


db = SqliteDatabase("/home/frizik/Projects/ScanTelegramBot/Data/WhiteIps.db")

class ListIps(Model):
    town = CharField()
    ips = CharField()
    ports = CharField()

    class Meta:
        database = db  


def CreateDataBase():
    ListIps.create_table()
    

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
        RezultString = FinalIp + ":" + str(Port) + ": worked!!!"
        City = ListIps(town = TownName, ips = FinalIp, ports = Port)
        City.save()  # cохраним Боба в базе данных
        pr.LogWriter(RezultString,LogPathWorked)
        FinalIpPing.close