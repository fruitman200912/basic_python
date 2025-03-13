c = ord(input("c:"))
print(c)
print(chr(c+1))

s1, s2 = input("s1 s2:").split()
print(s1[0:2] + s2[1] * 3)

n1, n2, n3 = input("n1 n2(16) -n3:").split()
print('%x'%int(n1), '%X'%int(n1))
print('%o'%int(n2,16))
print(-int(n3))

f1, f2 = input("f1:f2:").split(':')
print('\"', f1, f2, '\'', sep='\\')
print('\"', format(float(f1) + float(f2)), format((float(f1) + float(f2)) / 2, ".0f"),'\'', sep='\\')
print('\"', format(float(f1) - float(f2), ".1f"),'\'', sep='\\')
print('\"', format(float(f1) * float(f2), ".2f"),'\'', sep='\\')
print('\"', format(float(f1) // float(f2), ".3f"),'\'', sep='\\')
print('\"', format(float(f1) % float(f2),".4f"),'\'', sep='\\')
print('\"', format(float(f1) ** float(f2),".5f"),'\'', sep='\\')

b1, b2 = input("b1 b2:").split()
print(int(b1) if int(b1) <= int(b2) else int(b2))
print((bool(b1) and (not bool(b2))) or ((not bool(b1)) and bool(b2)))

if int(b1) > int(b2):
    print(">")
elif int(b1) == int(b2):
    print("==")
elif int(b1) < int(b2):
    print("<")

r = 1
while r != 0:
    r = int(input("r:"))
    if -1 >= r:
        break
    for i in range(r,-1,-1):
        if i % 2 == 0:
            continue
        print(i)

bit1, bit2 = input("bit1 bit2:").split()
print(int(bit1)>>1, int(bit1)<<int(bit1))
print(~int(bit1))
print(int(bit1) & int(bit2))
print(int(bit1) | int(bit2))
print(int(bit1) ^ int(bit2))