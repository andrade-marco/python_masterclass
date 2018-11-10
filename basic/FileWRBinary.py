# Using bytes is capped at 256
with open('../data/binary', 'bw') as binFile:
    binFile.write(bytes(range(17)))

with open('../data/binary', 'br') as readBin:
    for b in readBin:
        print(b)

# Beyond 256
a = 65534  # FF FE
b = 65535  # FF FF
c = 65536  # 00 01 00 00
d = 2998302  # 02 2D C0 1E

with open('binary2', 'bw') as binFile:
    binFile.write(a.to_bytes(2, 'big'))
    binFile.write(b.to_bytes(2, 'big'))
    binFile.write(c.to_bytes(4, 'big'))
    binFile.write(d.to_bytes(4, 'big'))
    binFile.write(d.to_bytes(4, 'little'))

with open('binary2', 'br') as binFile:
    e = int.from_bytes(binFile.read(2), 'big')
    f = int.from_bytes(binFile.read(2), 'big')
    g = int.from_bytes(binFile.read(4), 'big')
    h = int.from_bytes(binFile.read(4), 'big')
    i = int.from_bytes(binFile.read(4), 'big')
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)
