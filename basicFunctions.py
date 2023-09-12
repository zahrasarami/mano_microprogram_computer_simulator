

def dec_to_bin(num , bit):
    ans = bin(num)[2:]
    ans = '0'*(bit-len(ans)) + ans
    return ans


def bin_to_bin(num , bit=12):
    ans = '0'*(bit-len(num)-1) + num
    return ans

def hex_to_bin(num):
    ans = bin(int(num, 16))[2:]
    ans = '0'*(16-len(ans)) + ans
    return ans