import registers as R
import mainMemory as M

condition = False
endFlag = False
endProgramFlag = False

def dec_to_bin(num , bit):
    ans = bin(num)[2:]
    ans = '0'*(bit-len(ans)) + ans
    return ans

def bin_to_bin(num , bit):
    ans = '0'*(bit-len(num)-1) + num
    return ans

#F1 oprands :

def F1_001() : 
    R.AC = bin_to_bin( bin(int(R.AC,2) + int(R.DR,2))[2:17],16 )
    # # print('in add')

def F1_010() :
    R.reset_AC()
    # # print('CLRAC')

def F1_011() :
    R.AC = bin_to_bin( bin(int(R.AC,2) + int('1',2))[2:17] , 16)
    # # print('INCAC')

def F1_100() :
    R.AC = R.DR
    # # print('DRTAC')

def F1_101() :
    R.AR = R.DR[5:16]
    # # print('DRTAR')

def F1_110() :
    R.AR = R.PC
    # print('PCTAR')

def F1_111() :
    M.Memory[int(R.AR ,2)] = R.DR
    # print(f'write in{int(R.AR ,2)} PC:{R.PC}')

#F2 oprands :

def F2_001() :
    R.AC = bin_to_bin( bin(int(R.AC,2) - int(R.DR,2))[2:17] , 16 )
    # print('SUB')

def F2_010() :
    R.AC = bin_to_bin( bin(int(R.AC,2) | int(R.DR,2))[2:17] , 16 )
    # print('OR')

def F2_011() :
    R.AC = bin_to_bin( bin(int(R.AC,2) & int(R.DR,2))[2:17] , 16 )
    # print('AND')

def F2_100() :
    R.DR = M.Memory[int(R.AR ,2)]
    # print(f'read from{int(R.AR ,2)} pc:{R.PC} dr:{R.DR}')

def F2_101() :
    R.DR = R.AC
    # print('ACTDR')

def F2_110() :
    R.DR = bin_to_bin( bin(int(R.DR,2) + int('1',2))[2:17] , 16 )
    # print('INCDR')

def F2_111() :
    R.DR[5:16] = R.PC
    # print('PCTDR')

#F3 oprands :
 
def F3_001() :
    R.AC = bin_to_bin( bin(int(R.AC,2) ^ int(R.DR,2))[2:17] , 16)
    # print('XOR')

def F3_010() :
    R.AC = bin_to_bin( bin(~int(R.AC,2))[3:19] , 16 )
    # print('COM')

def F3_011() :
    R.AC = R.AC[1:16] + '0'
    # print('SHL')

def F3_100() :
    R.AC = '0' + R.AC[1:16]
    # print('SHr')

def F3_101() :
    # print(f'OLD{R.PC}')
    R.PC = bin_to_bin( bin(int(R.PC,2) + int('1',2))[2:12] , 11 )
    # print(f'new{R.PC}')

def F3_110() :
    R.PC = R.AR
    # print('ARTPC')

def F3_111() :
    global endProgramFlag
    # # print('++++++++++in hall')
    endProgramFlag = True
    pass

#CD:

def CD_00() :
    global condition
    condition =  True

def CD_01() :
    global condition
    if R.DR[0] == '1':
        condition =  True 
    else :
        condition =  False

def CD_10() :
    global condition
    if R.AC[0] == '1':
        condition =  True 
    else :
        condition =  False
    
def CD_11() : 
    global condition  
    if R.AC == 16*'0':
        condition =  True 
    else :
        condition =  False

#BR:

def BR_00(in_AD) :
    if condition==True :
        R.CAR = in_AD
    else :
        R.CAR = dec_to_bin(int(R.CAR,2)+1 , 7)

def BR_01() :
    if condition==True :
        R.CAR = bin_to_bin( bin(int(R.CAR,2) + int('1',2))[2:8] , 7 )
    else :
        R.CAR = dec_to_bin(int(R.CAR,2)+1 , 7)

def BR_10(in_AD) :
    if condition==True :
        R.SBR = bin_to_bin(bin(int(R.CAR,2) + int('1',2))[2:8] , 7)
        R.CAR = in_AD
    else :
        R.CAR = bin_to_bin( bin(int(R.CAR,2) + int('1',2))[2:8] , 7)

def BR_11() :
    global endFlag
    temp = '0'+R.DR[2:5]+'00'
    R.CAR = temp
    endFlag = True




