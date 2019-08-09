import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
import random
import subprocess as sp
from termcolor import colored
import pyfiglet
import parser  as pr
import preparation as pre
import requests
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
import re

SeparationString = "=========================================================="
IpAdress = ""
TownName = ""

# Функция вывода сообщения
def WriteMsgFunc(user_id, message,vk):
    random_id = random.randint(0, 12345678900987654321)
    vk.method('messages.send', {'user_id': user_id,'message': message,'random_id':random_id})

# Функция с приветственным сообщением 
def StartFunc(event,user_id,vk):
    hello = open("/home/frizik/Projects/ScanTelegramBot/TextMessages/Hello_Massage.txt")
    StringFromCommands = hello.read()
    WriteMsgFunc(event.user_id,StringFromCommands,vk)
    hello.close()

# Функция для вывода списка доступных команд
def HelpFunc(event,user_id,vk):
    commands=open("/home/frizik/Projects/ScanTelegramBot/TextMessages/Commands.txt","r")
    StringFromCommands=commands.read()
    WriteMsgFunc(event.user_id,StringFromCommands,vk)
    commands.close()

# Подготовительная функция
def Prepare(Answer,CountOfDash,CountOfZeros,TownName):    
    pre.StringParser(Answer,CountOfDash,CountOfZeros,TownName)

# Функция для загрузки картинок и документов
def UploadFunc(login,password,PathString):
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth(token_only=True)
    upload = vk_api.VkUpload(vk_session)
    document = upload.document(PathString,"db",group_id = 184430889)
    DocumentUrl = "vk.com/doc{}_{}".format(document["doc"]["owner_id"],document["doc"]["id"])
    return DocumentUrl

#Функция выдающая диапозон ip адрессов на город
def NewTownFunc(event,user_id,vk,TownName,login,password):
    try:
        Answer = pr.AutoParserIPs(TownName)
    except:
        WriteMsgFunc(event.user_id,"Город не найден в базе,возможно его там нет,либо вы ввели неверное название,пожалуйста повторите попытку",vk)
        return
    logPath = "/home/frizik/Projects/ScanTelegramBot/Data/ips.txt"
    ips = open(logPath,"w")
    ips.write(Answer)
    ips.close()

    DocumentUrl = UploadFunc(login,password,logPath)
    WriteMsgFunc(event.user_id,"Получен диапозон ip адрессов города,в этом текстовом файле вы можете их просмотреть",vk)
    WriteMsgFunc(event.user_id,DocumentUrl,vk)
    print(colored("Город ","blue"),colored(TownName,"red"),colored(" обработан!!!","blue"))
    return Answer

# Настройка клавиатуры 
def KeyboardInitialize(user_id,vk):
    keyboard = VkKeyboard(one_time = False)
    keyboard.add_button('Добавить порт', color = VkKeyboardColor.POSITIVE)
    keyboard.add_button('Выбрать город', color = VkKeyboardColor.POSITIVE)
    keyboard.add_line()  # Переход на вторую строку
    keyboard.add_button('Начать сканирование', color = VkKeyboardColor.POSITIVE)
    keyboard.add_button('Помощь', color = VkKeyboardColor.POSITIVE)

    random_id = random.randint(0,12345678900987654321)
    msg = "Клавиатура для удобной работы"
    vk.method('messages.send', {'user_id': user_id, 'message': msg, 'keyboard': keyboard.get_keyboard(),'random_id':random_id})

# Сканируюущая функция
def ScanFunc(IpAdress,TownName,event,user_id,vk,login,password):
    if IpAdress == "":
        WriteMsgFunc(event.user_id, "Невозможно начать сканирование так как не выбран город,пожалуйста проверьте указан ли диапозон адрессов",vk)
        return
    print(colored("Начинаю сканирование города:","yellow"),colored(TownName,"red"))
    prefab = re.compile('-')
    CountOfStrings = len(prefab.findall(IpAdress))
    prefab1 = re.compile('\n')
    CountOfn = len(prefab1.findall(IpAdress))
    pre.StringParser(IpAdress,CountOfStrings,CountOfn,TownName)

    DataBasePath = "/home/frizik/Projects/ScanTelegramBot/Data/WhiteIps.db"
    DocumentUrl = UploadFunc(login,password,DataBasePath)
    WriteMsgFunc(event.user_id,"Обработка завершенна,сформированна база данных ,содержащая список всех доступных адрессов с портами",vk)
    WriteMsgFunc(event.user_id,DocumentUrl,vk)
    print(colored("Город обработан полученна база данных доступных адрессов!!!","blue"))

# Основная функция 
def main():
    random.seed(version=2)
    AsciiArt = pyfiglet.figlet_format("ScanVkBot")
    tmp = sp.call('clear',shell=True)
    print(colored(AsciiArt,"yellow"))
    print(colored(SeparationString,"magenta"))
    
    print(colored("Введите ключ бота:","yellow"),end = "")
    token = input()
    print(colored("Введите логин от страницы администратора:","yellow"),end = "")
    login = input()
    print(colored("Введите пароль от страницы администратора:","yellow"),end = "")
    password = input()
    
    try:
        vk = vk_api.VkApi(token = token)
        print(colored("Успешное подключение,бот запущен!!!","green"))
        print(colored(SeparationString,"magenta"))
    except:
        print(colored("Не удалось подключится,проверьте правильность введённых данных","red"))

    longpoll = VkLongPoll(vk)
    Triger = False
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                if request == "старт" or request == "Старт":
                    StartFunc(event,event.user_id,vk)
                    KeyboardInitialize(event.user_id,vk)
                if request == "помощь" or request == "Помощь":
                    HelpFunc(event,event.user_id,vk)
                if request == "Начать сканирование" or request == "начать сканирование":
                    WriteMsgFunc(event.user_id,"Началось сканирование,это может занять много времени,ожидайте ответного сообщения со списком найденных доступных ip адрессов",vk)
                    ScanFunc(IpAdress,TownName,event,event.user_id,vk,login,password)
                if request == "город" or request == "Выбрать город":
                    WriteMsgFunc(event.user_id,"Введите название города для скана",vk)
                    Triger = True
                else:
                    if Triger == True:
                        Triger = False
                        WriteMsgFunc(event.user_id,"Подготавливается диапозон адрессов,пожалуйста подождите",vk)
                        IpAdress = NewTownFunc(event,event.user_id,vk,request,login,password)

# При импорте 
if __name__ == "__main__":
    main()