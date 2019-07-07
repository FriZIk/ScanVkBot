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


def TestFunc(Array):
    ZeroIndexArray = 0
    first_string_ips = Array[ZeroIndexArray:Array.index("-")]
    second_string_ips = Array[Array.index("-")+1:Array.index("\n")] 
    print(first_string_ips,second_string_ips)


def StringParser(Array,CountOfDash,CountOfZeros):
    DashIndexArray = [0 for i in range(CountOfDash)]
    ZeroIndexArray = [0 for i in range(CountOfZeros)]

    ZeroIndexArray = ReturnArrayWithIndex("\n",Array,ZeroIndexArray)
    DashIndexArray = ReturnArrayWithIndex("-",Array,DashIndexArray)

    print(ZeroIndexArray,DashIndexArray)

    if Debug == True:
        print(Array,Count,count)
        Count1 = ReturnCount("\n",Array)
        Count2 = ReturnCount("-",Array)
        print(Count1,Count2)