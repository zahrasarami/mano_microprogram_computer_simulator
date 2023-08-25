F1 = {  'NOP':'000',
        'ADD':'001', 
        'CLRAC':'010', 
        'INCAC':'011', 
        'DRTAC':'100', 
        'DRTAR':'101', 
        'PCTAR':'110', 
        'WRITE':'111'
    }
F2 = {  'NOP':'000',
        'SUB':'001', 
        'OR':'010', 
        'AND':'011', 
        'READ':'100', 
        'ACTDR':'101', 
        'INCDR':'110', 
        'PCTDR':'111'
    }
F3 = {  'NOP':'000',
        'XOR':'001', 
        'COM':'010', 
        'SHL':'011', 
        'SHR':'100', 
        'INCPC':'101', 
        'ARTPC':'110', 
        'HAL':'111'
    }

CD = {  'U':'00',
        'I':'01',
        'S':'10',
        'Z':'11'
    }

BR = {  'JMP':'00',
        'CALL':'01',
        'RET':'10',
        'MAP':'11'
    }

oprands = {}

def dec_to_bin(num):
    ans = bin(num)[2:]
    ans = '0'*(7-len(ans)) + ans
    return ans

def read_microProgramMemory():
    code = open('./microProgram.txt' , "r").read()
    code = code.split('\n')
    code = list(map( str.strip ,code ))
    output_code = []
    for line in code :
        line = line.split(' ')
        temp = []
        for i in line :
            i = i.strip()
            if i!='' and i!=',' :
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

def fill_oprands_table( in_code ):
    for line in in_code :
        if ':' in line[0] :
           oprands[line[0][:-1]] =  line[-1]
    
def translate_to_binary( in_code ) :
    f1 = '000'
    f2 = '000'
    f3 = '000'
    cd = '00'
    br = '00'
    ad = '0000000'
    output_code = []
    for line in in_code :
        check = 0
        if line[check] in oprands :
            check += 1
        for i in range(check , len(line)) :
            if line[i] in F1 :
                f1 = F1[line[i]]
            elif line[i] in F2 :
                f2 = F2[line[i]]
            elif line[i] in F3 :
                f3 = F3[line[i]]
            elif line[i] in CD :
                cd = CD[line[i]]
            elif line[i] in BR :
                br = BR[line[i]]
            elif line[i] == 'NEXT' :
                ad = dec_to_bin(int(line[-1]+1))
            elif line[i] in oprands :
                ad = dec_to_bin(int(oprands[line[i]]))
        output_code.append(f'{f1} {f2} {f3} {cd} {br} {ad} {line[-1]}')
    return output_code
        
def microProgramAssembler() :
    code = read_microProgramMemory()
    code = align(code)
    fill_oprands_table(code)
    return translate_to_binary(code)
# code=microProgramAssembler() 
# print(oprands)
# print(code)