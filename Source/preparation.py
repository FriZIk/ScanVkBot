import numpy as np
from numpy import matrix 
import scan as sc

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


def LogWriter(RezultString,FilePath):
    Logs = open(FilePath,"a")
    Logs.write(RezultString + "\n")
    Logs.close()


def FinalIpRange(first_string_ips,second_string_ips,CountOfDash,Town):
    sc.CreateDataBase()
    LogPath = "/home/frizik/Projects/ScanTelegramBot/Logs/iplg.txt"
    LogPathWorkString = "/home/frizik/Projects/ScanTelegramBot/Logs/ipworkedlg.txt"
    FirstSeparation = first_string_ips.split(".")
    SecondSeparation = second_string_ips.split(".")
    print(FirstSeparation,SecondSeparation)
    for Iterator in range(4):
        if FirstSeparation[Iterator] != SecondSeparation[Iterator]:
            IpElementF = int(FirstSeparation[Iterator])
            IpElementS = int(SecondSeparation[Iterator]) 
            if FirstSeparation[Iterator] != SecondSeparation[Iterator]:
                if FirstSeparation[Iterator] < SecondSeparation[Iterator]:
                    if Iterator == 3:
                        while IpElementF < IpElementS + 1:
                            FirstSeparation[Iterator] = str(IpElementF)
                            RezultString = FirstSeparation[0] + "." + FirstSeparation[1] + "." + FirstSeparation[2] + "." + FirstSeparation[3]
                            IpElementF = IpElementF + 1
                            LogWriter(RezultString,LogPath)
                            sc.ScanFunction(RezultString,Town)
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
                                LogWriter(RezultString,LogPath)
                                sc.ScanFunction(RezultString,Town)                


def FragmentationFunc(Array,CountOfDash,ZeroIndexArray,DashIndexArray,Town):
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

        RezultString = "Рабочая строка:" + first_string_ips + " " + second_string_ips + "\n"
        LogWriter(RezultString,"/home/frizik/Projects/ScanTelegramBot/Logs/ipworkedlg.txt")

        print(first_string_ips,second_string_ips)
        FinalIpRange(first_string_ips,second_string_ips,CountOfDash,Town)


def StringParser(Array,CountOfDash,CountOfZeros,Town):
    DashIndexArray = [0 for i in range(CountOfDash)]
    ZeroIndexArray = [0 for i in range(CountOfZeros)]

    ZeroIndexArray = ReturnArrayWithIndex("\n",Array,ZeroIndexArray)
    DashIndexArray = ReturnArrayWithIndex("-",Array,DashIndexArray)
    if Debug == True : print(ZeroIndexArray,DashIndexArray)
    
    FragmentationFunc(Array,CountOfDash,ZeroIndexArray,DashIndexArray,Town)