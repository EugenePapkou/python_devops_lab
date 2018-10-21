n = int(input("Please enter n:"))
while 1 > n or n > 99:
    n = int(input("Please enter n in a range 1 <= n <= 99:"))


width_raw = len("{0:b}".format(n))

for i in range(1, n + 1):
    dec_num = format(i, "d")
    octal_num = format(i, "o")
    hex_num = format(i, "x").upper()
    bin_num = format(i, "b")
    print("{0:^{width}} {1:^{width}} {2:^{width}} {3:{width}}"
          .format(dec_num, octal_num, hex_num, bin_num, width=width_raw))
