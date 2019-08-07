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

# Функция вывода сообщения
def WriteMsgFunc(user_id, message,random_id,vk):
    vk.method('messages.send', {'user_id': user_id,'message': message,'random_id':random_id})

# Функция с приветственным сообщением 
def StartFunc(event,user_id,random_id,vk):
    hello = open("/home/frizik/Projects/ScanTelegramBot/TextMessages/Hello_Massage.txt")
    StringFromCommands = hello.read()
    WriteMsgFunc(event.user_id,StringFromCommands,random_id,vk)
    hello.close()

# Функция для вывода списка доступных команд
def HelpFunc(event,user_id,random_id,vk):
    commands=open("/home/frizik/Projects/ScanTelegramBot/TextMessages/Commands.txt","r")
    StringFromCommands=commands.read()
    WriteMsgFunc(event.user_id,StringFromCommands,random_id,vk)
    commands.close()

# Подготовительная функция
def Prepare(Answer,CountOfDash,CountOfZeros,TownName):    
    pre.StringParser(Answer,CountOfDash,CountOfZeros,TownName)

#Функция выдающая диапозон ip адрессов на город
def NewTownFunc(event,user_id,random_id,vk,TownName,login,password):
    Answer = pr.AutoParserIPs(TownName)
    logPath = "/home/frizik/Projects/ScanTelegramBot/Data/ips.txt"
    ips = open(logPath,"w")
    ips.write(Answer)
    ips.close()

    vk_session = vk_api.VkApi(login, password)
    vk_session.auth(token_only=True)

    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo('/home/frizik/Photo/москва/DSC05281.JPG',album_id=264629427,group_id=184430889)
    vk_photo_url = 'https://vk.com/photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])
    print(photo, '\nLink: ', vk_photo_url)
    WriteMsgFunc(event.user_id,photo_url,random_id,vk)

    #document = upload.docs('')Загрзука фотографий работает теперь нудно разобраться с документами

# Основная функция 
def main():
    AsciiArt = pyfiglet.figlet_format("ScanVkBot")
    tmp = sp.call('clear',shell=True)
    print(colored(AsciiArt,"yellow"))
    
    print(colored("Введите ключ бота:","yellow"),end = "")
    token = input()
    print(colored("Введите логин от страницы администратора:","yellow"),end = "")
    login = input()
    print(colored("Введите пароль оут страницы администратораЖ","yellow"),end = "")
    password = input()

    token = input()
    vk = vk_api.VkApi(token=token)
    random.seed(version=2)
    longpoll = VkLongPoll(vk)
    Triger = False
    for event in longpoll.listen():
        random_id = random.randint(0, 12345678900987654321)
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                request = event.text
                if request == "старт" or request == "Старт":
                    StartFunc(event,event.user_id,random_id,vk)
                if request == "помощь" or request == "Помощь":
                    HelpFunc(event,event.user_id,random_id,vk)
                if request == "город" or request == "Город":
                    WriteMsgFunc(event.user_id,"Введите название города для скана",random_id,vk)
                    Triger = True 
                    print(Triger)
                else:
                    if Triger == True:
                        Triger = False
                        NewTownFunc(event,event.user_id,random_id,vk,request,login,password)
                        
                    else :
                        WriteMsgFunc(event.user_id, "Неизветсная команда,проверьте правильность введённых данных",random_id,vk)

# При импорте 
if __name__ == "__main__":
    main()