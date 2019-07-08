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


#пока что не кушает самый первый адресс сращу перескакивает на следуюущий  
def FinalIpRange(first_string_ips,second_string_ips,CountOfDash):
    FirstSeparation = first_string_ips.split(".")
    SecondSeparation = second_string_ips.split(".")
    print(FirstSeparation,SecondSeparation)
    for i in range(4):
        if FirstSeparation[i] != SecondSeparation[i]:
            IpElementF = int(FirstSeparation[i])
            IpElementS = int(SecondSeparation[i])
            while IpElementF != IpElementS:
                if IpElementF > IpElementS:
                    while IpElementF < 255:
                        IpElementF = IpElementF + 1
                        FirstSeparation[i] = str(IpElementF)
                        RezultString = FirstSeparation[0] + "." + FirstSeparation[1] + "." + FirstSeparation[2] + "." + FirstSeparation[3]
                        print(RezultString)
                    IpElementF = 0
                    while IpElementF < IpElementS :
                        IpElementF = IpElementF + 1
                        FirstSeparation[i] = str(IpElementS)
                        RezultString = RezultString = FirstSeparation[0] + "." + FirstSeparation[1] + "." + FirstSeparation[2] + "." + FirstSeparation[3]
                        print(RezultString)
                    break

                else :
                    IpElementF = IpElementF + 1
                    FirstSeparation[i] = str(IpElementF)
                    RezultString = FirstSeparation[0] + "." + FirstSeparation[1] + "." + FirstSeparation[2] + "." + FirstSeparation[3]
                    print(RezultString)
                

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
        print(first_string_ips,second_string_ips)
        FinalIpRange(first_string_ips,second_string_ips,CountOfDash)


def StringParser(Array,CountOfDash,CountOfZeros):
    DashIndexArray = [0 for i in range(CountOfDash)]
    ZeroIndexArray = [0 for i in range(CountOfZeros)]

    ZeroIndexArray = ReturnArrayWithIndex("\n",Array,ZeroIndexArray)
    DashIndexArray = ReturnArrayWithIndex("-",Array,DashIndexArray)
    if Debug == True : print(ZeroIndexArray,DashIndexArray)
    
    FragmentationFunc(Array,CountOfDash,ZeroIndexArray,DashIndexArray)