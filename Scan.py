#сканер
import socket

white=open("whiteips.txt")
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
while(Index_Line!=Count_Lines-2):
    ips.seek(lines_index[Index_Line])
    string_IPS=ips.readline()
    #print(string_IPS)
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
        s.settimeout(0.01)
        try:
            s.connect((first_string_ips, Port))
        except socket.error:
            pass
        else:
            s.close
            print(first_string_ips+':'+str(Port)+'\n')
            a=(first_string_ips+':'+str(Port)+'\n')
    Index_Line=Index_Line+1
print(a)
