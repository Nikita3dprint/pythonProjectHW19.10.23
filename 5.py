for n in range(1, 200):
    b = bin(2 * n)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    r = int(b, 2)
    if r > 123:
        print(n)
        break
