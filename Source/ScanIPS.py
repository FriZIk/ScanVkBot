import socket
import numpy as np
from numpy import matrix 
import peewee

Debug = False

def ReturnArrayWithIndex(Combination,Array,TargetArray):
    index = 0
    CountOfCombination = 0
    if Debug == True : print(Array)
    while index < len(Array):
        index = Array.find(Combination, index)
        if index == -1:
            break
        index += 1
        TargetArray[CountOfCombination] = index
        CountOfCombination = CountOfCombination + 1
    return TargetArray


def LogWriter(RezultString):
    Logs = open("log.txt","a")
    Logs.write(RezultString + "\n")
    Logs.close()


def FinalIpRange(first_string_ips,second_string_ips,CountOfDash):
    FirstSeparation = first_string_ips.split(".")
    SecondSeparation = second_string_ips.split(".")
    print(FirstSeparation,SecondSeparation)
    for Iterator in range(4):
        if FirstSeparation[Iterator] != SecondSeparation[Iterator]:хз как-то в браузеер 
            IpElementF = int(FirstSeparation[Iterator])
            IpElementS = int(SecondSeparation[Iterator]) 
            if FirstSeparation[Iterator] != SecondSeparation[Iterator]:
                if FirstSeparation[Iterator] < SecondSeparation[Iterator]:
                    if Iterator == 3:
                        while IpElementF < IpElementS + 1:
                            FirstSeparation[Iterator] = str(IpElementF)
                            RezultString = FirstSeparation[0] + "." + FirstSeparation[1] + "." + FirstSeparation[2] + "." + FirstSeparation[3]
                            IpElementF = IpElementF + 1
                            LogWriter(RezultString)
                        TrueCountF = int(FirstSeparation[Iterator - 1])
                        TrueCountS = int(SecondSeparation[Iterator - 1])
                        while TrueCountF < TrueCountS:
                            TrueCountF = TrueCountF + 1
                            FirstSeparation[Iterator - 1] = str(TrueCountF)
                            IpElementF = 0
                            while IpElementF < 255:
                                FirstSeparation[Iterator] = str(IpElementF)
                                RezultString = FirstSeparation[0] + "." + FirstSeparation[1] + "." + FirstSeparation[2] + "." + FirstSeparation[3]
                                IpElementF = IpElementF + 1
                                LogWriter(RezultString)                


def FragmentationFunc(Array,CountOfDash,ZeroIndexArray,DashIndexArray):
    IndexForDash =  0
    IndexForZero = 0
    while IndexForDash < CountOfDash:
        first_string_ips = Array[IndexForZero:DashIndexArray[IndexForDash]-1]
        if IndexForDash == CountOfDash - 1 : 
            a = len(Array)
            second_string_ips = Array[DashIndexArray[IndexForDash]:a]
        else :
            second_string_ips = Array[DashIndexArray[IndexForDash]:ZeroIndexArray[IndexForDash]-1]
            IndexForZero = ZeroIndexArray[IndexForDash]
        IndexForDash = IndexForDash + 1
        Logs = open("log.txt" , "a")
        Logs.write("Рабочая строка:" + first_string_ips + " " + second_string_ips + "\n")
        Logs.close()
        print(first_string_ips,second_string_ips)
        FinalIpRange(first_string_ips,second_string_ips,CountOfDash)


def StringParser(Array,CountOfDash,CountOfZeros):
    DashIndexArray = [0 for i in range(CountOfDash)]
    ZeroIndexArray = [0 for i in range(CountOfZeros)]

    ZeroIndexArray = ReturnArrayWithIndex("\n",Array,ZeroIndexArray)
    DashIndexArray = ReturnArrayWithIndex("-",Array,DashIndexArray)
    if Debug == True : print(ZeroIndexArray,DashIndexArray)
    
    FragmentationFunc(Array,CountOfDash,ZeroIndexArray,DashIndexArray)