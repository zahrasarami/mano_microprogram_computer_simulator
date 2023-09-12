
Memory = [16*'0']*2048

def fill_main_memory( assembled_code ) :
    for line in assembled_code :
        Memory[line[-1]] = line[0]+line[1]+line[2]
