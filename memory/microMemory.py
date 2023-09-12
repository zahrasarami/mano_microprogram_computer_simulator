
microMemory = [20*'0']*128

def fill_micro_memory( assembled_code ) :
    for line in assembled_code :
        microMemory[line[-1]] = line[0]+line[1]+line[2]+line[3]+line[4]+line[5]
