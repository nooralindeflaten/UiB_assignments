from pwn import*

e = ELF('/home/sarahlindeflaten/226/00')
print(e.functions.main)
print(e.section('.rodata'))
print(e.symbols)