class Solution:
    def toHex(self, val: int) -> str:
        dict_key = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        res = ""
        if val == 0:
            return "0"
        if val<0:
            val = (1<<32)+val
        while val>0:
            if val%16<10:
                res+=str(val%16)
            else:
                res+=str(dict_key[val%16])
            val=val//16
        return res[::-1]
