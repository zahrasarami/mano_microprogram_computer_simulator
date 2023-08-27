import registers as R
import mainMemory as M

condition = False

#F1 oprands :

def F1_001() : 
    R.AC = bin(int(R.AC,2) + int(R.DR,2))[2:17]

def F1_010() :
    R.reset_AC

def F1_011() :
    R.AC = bin(int(R.AC,2) + int('1',2))[2:17]

def F1_100() :
    R.AC = R.DR

def F1_101() :
    R.AC = R.DR[5:15]

def F1_110() :
    R.AR = R.PC

def F1_111() :
    M.Memory[int(R.AR ,2)] = R.DR

#F2 oprands :

def F2_001() :
    R.AC =bin(int(R.AC,2) - int(R.DR,2))[2:17]

def F2_010() :
    R.AC = bin(int(R.AC,2) | int(R.DR,2))[2:17]

def F2_011() :
    R.AC = bin(int(R.AC,2) & int(R.DR,2))[2:17]

def F2_100() :
    R.DR = M.Memory[int(R.AR ,2)]

def F2_101() :
    R.DR = R.AC

def F2_110() :
    R.DR = bin(int(R.DR,2) + int('1',2))[2:17]

def F2_111() :
    R.DR[5:15] = R.PC

#F3 oprands :
 
def F3_001() :
    R.AC = bin(int(R.AC,2) ^ int(R.DR,2))[2:17]

def F3_010() :
    R.AC = bin(~int(R.AC,2))[3:19]

def F3_011() :
    R.AC = R.AC[1:15] + '0'

def F3_100() :
    R.AC = '0' + R.AC[1:15]

def F3_101() :
    R.PC = bin(int(R.PC,2) + int('1',2))[2:12]

def F3_110() :
    R.PC = R.AR

def F3_111() :
    pass

#CD:

def CD_00() :
    condition =  True

def CD_01() :
    if R.DR[0] == '1':
        condition =  True 
    else :
        condition =  False

def CD_10() :
    if R.AC[0] == '1':
        condition =  True 
    else :
        condition =  False
    
def CD_11() :   
    if R.AC == 16*'0':
        condition =  True 
    else :
        condition =  False

#BR:

def BR_00(in_AD) :
    if condition==True :
        R.CAR = in_AD
    pass

def BR_01() :
    if condition==True :
        R.CAR = bin(int(R.CAR,2) + int('1',2))[2:8]
    pass

def BR_10(in_AD) :
    if condition==True :
        R.SBR = bin(int(R.CAR,2) + int('1',2))[2:8]
        R.CAR = in_AD
    else :
        R.CAR = bin(int(R.CAR,2) + int('1',2))[2:8]

def BR_11() :
    R.CAR[1:4] = R.DR[2:5]
    R.CAR[0] = '0'
    R.CAR[5] = '0'
    R.CAR[6] = '0'


