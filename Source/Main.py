import telebot
from telebot import types
import socket

print("DarkResearch Scaner")

Key=("568486960:AAFkaZAkR-dba8yGSp0PD0ogaNtKAyEz3TA")
bot = telebot.TeleBot(Key)
print("Conecting...")
user =bot.get_me()#Проверям подключение
print("Successful connection")

#Декораторы для команд
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

#как-то всё очень криво,но красиво мы сделаме потом,сейчас главное чтобы заработало

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

#Тут начинается ад,попытка подключения по ip,предварительно этот ip ещё надо вычленить из файла,и потом изменять
@bot.message_handler(commands="scan")
def parsing_ip_and_ports_list(message):
    white=open("whiteips.txt")
    bot.send_message(message.chat.id,"Start scanning...form a list of available servers")
    #Для начала сформируем файл,в который скинем все ip адресса,которые откликнутся на порт,указанный нами
    ports=open("ports.txt","r")
    Port=ports.read()#Получили порт по которому будем сканировать
    Port=int(Port)
    ips=open("ips.txt","r")
    Count_Lines = len(ips.readlines());ips.close()
    ips = open("ips.txt", "r")#Вот за это мне стыдно,это просто ужасно,серьёзно убейте меня
    Index_Line=0;lines_index = []
    a=("")#строка для выдачи
    while ips.readline():
        lines_index.append(ips.tell())
    while(Index_Line!=Count_Lines-1):
        ips.seek(lines_index[Index_Line])
        string_IPS=ips.readline()
        print(string_IPS)
        Lenght_string_IPS=len(string_IPS)
        dash_index=string_IPS.index("-")#На этом останавливаемся,всё остальное не нужно так как разичия в строках адрессво только в последнем блоке
        first_string_ips=string_IPS[0:dash_index]#Получили нужны кусок теперь остаётся как-то инкерментирвоать последние цифры от 0 до 255
        second_string_ips=string_IPS[dash_index+1:Lenght_string_IPS-1]
        len1=len(first_string_ips)#print(len1)
        len2=len(second_string_ips)#;print(len2)
        #Подсчёт кол-ва строк в файле
        zero_index1=(first_string_ips.rfind("."))
        first_string_ips_parse=first_string_ips[zero_index1+1:len1]
        first_string_ips=first_string_ips[0:zero_index1]
        first_string_ips2 = first_string_ips
        while(first_string_ips!=second_string_ips):
            first_string_ips_parse=int(first_string_ips_parse)
            first_string_ips_parse=first_string_ips_parse+1
            first_string_ips_parse=str(first_string_ips_parse)
            first_string_ips=first_string_ips2+"."+first_string_ips_parse#Наконец-то получаем окончательный ip
            #проверяем полученный ip адресс
            s = socket.socket()
            s.settimeout(0.001)
            try:
                s.connect((first_string_ips, Port))
            except socket.error:
                pass
            else:
                s.close
                a+=(first_string_ips+':'+str(Port)+'\n')
        Index_Line=Index_Line+1
    bot.send_message(message.chat.id, "Range scan finished!!!")
    bot.send_message(message.chat.id, a)


@bot.message_handler(commands="logs")
def handle_stoping_scan(message):
    bot.send_message(message.chat.id,"scanning stopped")
if __name__ == "__main__":bot.polling(none_stop=True)
