import sys
PATH = '/home/zhra/projects/python/mano-microprogram-computer-simulater/'
sys.path.append( PATH )
import basicFunctions as BF

import microProgramAssembler as MPA

variables = {}


def find_index(in_key):
    for key, value in MPA.oprands.items():
        if key==in_key :
            temp = value - value%4
            return BF.dec_to_bin(int(temp/4) , 4)
        
    return '0000'

def read_ProgramMemory():
    code = open(f'{PATH}/memory/program.txt' , "r").read()
    code = code.split('\n')
    code = list(map( str.strip ,code ))
    output_code = []
    for line in code :
        line = line.split(' ')
        temp = []
        for i in line :
            i = i.strip()
            if i!='' :
                temp.append(i)
        output_code.append(temp) 

    return output_code

def align( in_code ) :
    line_counter = 0 
    output_code = []

    for i in range(len(in_code)) :
        temp = in_code[i]
        if 'ORG' in temp :
            line_counter = int(temp[1])
        else :
            in_code[i].append(line_counter)
            output_code.append(in_code[i])
            line_counter += 1
    return output_code

def fill_variables_table( in_code ):
    for line in in_code :
        if ':' in line[0] :
            variables[line[0][:-1]] = str(line[-1])

def translate_to_binary( in_code ) :
    output_code = []
    for line in in_code :
        temp = []
        if line[0] in MPA.oprands :
            if line[0]=='HAL' :
                temp.append('0')
                temp.append(find_index('HAL'))
                temp.append(11*'0')
            else :
                #I:
                if line[-2] == 'I' :
                    temp.append('1')
                else :
                    temp.append('0')
                #opcode:
                temp.append(find_index(line[0]))
                #address:
                if line[1] == 'BIN' :
                    temp.append(BF.bin_to_bin(line[2]))
                elif line[1] == 'HEX' :
                    temp.append(BF.hex_to_bin(line[2]))
                elif line[1] == 'DEC' :
                    temp.append(BF.dec_to_bin(int(line[2]),11))
                else :
                    temp.append(BF.dec_to_bin(int(variables[line[1]]),11))
        else :
            #I:
            temp.append('0')
            #opcode:
            temp.append('0000')
            #address:
            if line[1] == 'BIN' :
                temp.append(BF.bin_to_bin(line[2]))
            elif line[1] == 'HEX' :
                temp.append(BF.hex_to_bin(line[2]))
            else :
                temp.append(BF.dec_to_bin(int(line[2]),11))
        temp.append(line[-1])
        output_code.append(temp)
    return output_code
            
def programAssembler() : 
    code = read_ProgramMemory()
    code = align(code)
    fill_variables_table(code)
    return translate_to_binary(code)
#     temp = translate_to_binary(code)
#     for i in range(0 , len(temp)):
#         print(code[i])
#         print(temp[i])

# MPA.microProgramAssembler()
# print(MPA.oprands)
# programAssembler()