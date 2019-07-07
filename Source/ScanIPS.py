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


def FinalIpRange(first_string_ips,second_string_ips):


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
        FinalIpRange(first_string_ips,second_string_ips)


def StringParser(Array,CountOfDash,CountOfZeros):
    DashIndexArray = [0 for i in range(CountOfDash)]
    ZeroIndexArray = [0 for i in range(CountOfZeros)]

    ZeroIndexArray = ReturnArrayWithIndex("\n",Array,ZeroIndexArray)
    DashIndexArray = ReturnArrayWithIndex("-",Array,DashIndexArray)
    if Debug == True : print(ZeroIndexArray,DashIndexArray)
    
    FragmentationFunc(Array,CountOfDash,ZeroIndexArray,DashIndexArray)