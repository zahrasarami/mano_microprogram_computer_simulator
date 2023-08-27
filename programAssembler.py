import microProgramAssembler as MPA

variables = {}

def dec_to_bin(num , bit):
    ans = bin(num)[2:]
    ans = '0'*(bit-len(ans)) + ans
    return ans

def find_index(in_key):
    counter = 0 
    for key, value in MPA.oprands.items():
        if key==in_key :
            return dec_to_bin(counter , 4)
        counter += 1
    return '0000'

def bin_to_bin(num):
    ans = '0'*(16-len(num)) + num
    return ans

def hex_to_bin(num):
    ans = bin(int(num, 16))[2:]
    ans = '0'*(16-len(ans)) + ans
    return ans

def read_ProgramMemory():
    code = open('./program.txt' , "r").read()
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
            #I:
            if line[-2] == 'I' :
                temp.append('1')
            else :
                temp.append('0')
            #opcode:
            temp.append(find_index(line[0]))
            #address:
            if line[1] == 'BIN' :
                temp.append(bin_to_bin(line[2]))
            elif line[1] == 'HEX' :
                temp.append(hex_to_bin(line[2]))
            elif line[1] == 'DEC' :
                temp.append(dec_to_bin(int(line[2]),16))
            else :
                temp.append(dec_to_bin(int(variables[line[1]]),11))
        else :
            #I:
            temp.append('0')
            #opcode:
            temp.append('0000')
            #address:
            if line[1] == 'BIN' :
                temp.append(bin_to_bin(line[2]))
            elif line[1] == 'HEX' :
                temp.append(hex_to_bin(line[2]))
            else :
                temp.append(dec_to_bin(int(line[2]),16))
        temp.append(line[-1])
        output_code.append(temp)
    return output_code
            
def programAssembler() : 
    code = read_ProgramMemory()
    code = align(code)
    fill_variables_table(code)
    return translate_to_binary(code)
