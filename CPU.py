import microProgramAssembler as MPA
import programAssembler as PA
import microOprations as MO
import mainMemory 
import microMemory



def execute_F1( in_code ) :
    if in_code=='001' :
        MO.F1_001()
    elif in_code=='010' :
        MO.F1_010()
    elif in_code=='011' :
        MO.F1_011()
    elif in_code=='100' :
        MO.F1_100()
    elif in_code=='101' :
        MO.F1_101()
    elif in_code=='110' :
        MO.F1_110()
    elif in_code=='111' :
        MO.F1_111()
    else :
        pass

def execute_F2( in_code ) :
    if in_code=='001' :
        MO.F2_001()
    elif in_code=='010' :
        MO.F2_010()
    elif in_code=='011' :
        MO.F2_011()
    elif in_code=='100' :
        MO.F2_100()
    elif in_code=='101' :
        MO.F2_101()
    elif in_code=='110' :
        MO.F2_110()
    elif in_code=='111' :
        MO.F2_111()
    else :
        pass

def execute_F3( in_code ) :
    if in_code=='001' :
        MO.F3_001()
    elif in_code=='010' :
        MO.F3_010()
    elif in_code=='011' :
        MO.F3_011()
    elif in_code=='100' :
        MO.F3_100()
    elif in_code=='101' :
        MO.F3_101()
    elif in_code=='110' :
        MO.F3_110()
    elif in_code=='111' :
        MO.F3_111()
    else :
        pass

def execute_CD( in_code ) :
    if in_code=='00':
        MO.CD_00()
    elif in_code=='01' :
        MO.CD_01()
    elif in_code=='10' :
        MO.CD_10()
    elif in_code=='11' :
        MO.CD_11()
    else :
        MO.condition = False

def execute_BR( in_code  , ad) :
    if in_code=='00':
        MO.BR_00(ad)
    elif in_code=='01' :
        MO.BR_01()
    elif in_code=='10' :
        MO.BR_10(ad)
    elif in_code=='11' :
        MO.BR_11()
    else :
        pass

def execute( command ):

    execute_F1(command[0:3])
    execute_F2(command[3:6])
    execute_F3(command[6:9])
    #check condition 
    execute_CD(command[9:11])
    execute_BR(command[11:13] , command[13:20])
    
def step() :
    #fetch
    codeLine = mainMemory.Memory[int(MO.R.PC,2)] 
    #find efective address
    if codeLine[0] == '1' :
        MO.R.AR = mainMemory.Memory[int(codeLine[5:16] ,2)][5:16]  
    else :
        MO.R.AR = codeLine[5:16]
    #findCAR
    opcode = '0'+codeLine[1:5]+'00'
    MO.R.CAR = opcode
    #start microprogram rootin
    MO.endFlag = False

    while MO.endFlag==False :
        command = microMemory.microMemory[int(MO.R.CAR , 2)]
        execute(command)   

def initial(start) :
    MO.R.PC = PA.dec_to_bin(start,11)
    MO.R.reset_CAR()
    MO.R.reset_AR()
    MO.R.reset_AC()
    MO.R.reset_DR()
    MO.R.reset_SBR()
    
def run() :
    microProgramMemory = MPA.microProgramAssembler()
    microMemory.fill_micro_memory(microProgramMemory)

    programMemory = PA.programAssembler()
    mainMemory.fill_main_memory(programMemory)
    start = programMemory[0][-1]
    # for i in range(0 , len(microProgramMemory)) :
    #     print(microMemory.microMemory[i])
    #     print( microProgramMemory[i], '\n')
    # print(microProgramMemory)
    # print("|||||||||||||||||||||||||||||||||||||||||")
    # print(programMemory)
    

    initial(start)
    while MO.endProgramFlag==False :
        step()
    # step()
    # print(f'______pc is {MO.R.PC}')
       
def  print_registers() :
    print('AC:' ,MO.R.AC)
    print('PC:' ,MO.R.PC)
    print('CAR:' ,MO.R.CAR)
    print('AR:' ,MO.R.AR)
    print('DR:' ,MO.R.DR)
    print('SBR:' ,MO.R.SBR)


run()
print_registers()
print(mainMemory.Memory[20:23])
