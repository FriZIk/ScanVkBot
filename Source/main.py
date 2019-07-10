import telebot
from telebot import types
import parser
import os
from termcolor import colored
import pyfiglet
import subprocess as sp


def Scaner():
    Path = "/home/frizik/Projects/ScanTelegramBot/Logs"
    Flag = True
    if os.path.exists(Path + "/pinglg.txt") == True and Flag == True : os.remove(Path + "/pinglg.txt")
    if os.path.exists(Path + "/pinglgN.txt") == True and Flag == True: os.remove(Path + "/pinglgN.txt")
    if os.path.exists(Path + "/iplg.txt") == True and Flag == True:  os.remove(Path + "/iplg.txt")
    if os.path.exists(Path + "/ipworkedlg.txt") == True and Flag == True: os.remove(Path + "/ipworkedlg.txt")
    print(colored("Введите название города:","yellow"), end = "")
    TownName = input() 
    parser.AutoParserIPs(TownName)

AsciiArt = pyfiglet.figlet_format("ScanTelegramBot")

tmp = sp.call('clear',shell=True)
print(colored(AsciiArt,"yellow"))
print(colored("Введите ключ бота:", "yellow"), end = "")
BotFatherKey = input()
bot = telebot.TeleBot(BotFatherKey)
try:
    user = bot.get_me()
    print(colored("Успешное подключение!","green"))
except:
    print(colored("Ошибка подключения,проверьте правильность введённых данных","red"))
Scaner()


@bot.message_handler(commands=["start"])
def handle_start(message):
    hello=open("Hello_Massage.txt")
    String_From_Commands=hello.read()
    bot.send_message(message.chat.id,String_From_Commands)
    hello.close()


@bot.message_handler(commands=["help"])
def handle_help(message):
    commands=open("Commands.txt","r")
    String_From_Commands=commands.read()
    bot.send_message(message.chat.id,String_From_Commands)
    commands.close()


@bot.message_handler(commands=["newip"])
def handle_scan(message):
    msg=bot.send_message(message.chat.id,"New range of addresses")
    bot.register_next_step_handler(msg,writeIPS)

def writeIPS(message):
    try:
        IPS=message.text
        ips=open("ips.txt","w")
        ips.write(IPS)
        ips.close()
        bot.send_message(message.chat.id,"New address range is loaded!!!")
    except Exception as e:
        bot.reply_to(message,"Unknown error,try again((")


@bot.message_handler(commands=["ports"])
def handle_ports(message):
    ports=open("ports.txt")
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add("21","22","80")
    Port=bot.reply_to(message,"Select the port to scan",reply_markup=markup)
    bot.register_next_step_handler(Port,writePORT)
def writePORT(message):
    try:
        port=message.text
        ips=open("ports.txt","w")
        ips.write(port)
        ips.close()
        bot.send_message(message.chat.id,"Port selected!!!")
    except Exception as e:
        bot.reply_to(message,"Unknown error,try again(")


@bot.message_handler(commands="logs")
def handle_stoping_scan(message):
    bot.send_message(message.chat.id,"scanning stopped")
    
    
if __name__ == "__main__":
    bot.polling(none_stop=True)