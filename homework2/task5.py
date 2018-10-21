n = int(input("Please enter n:"))
while 1 > n or n > 100000:
    n = int(input("Please enter n in a range 1 <= n <= 100 000:"))

m = int(input("Please enter m:"))
while 1 > m or m > 100000:
    m = int(input("Please enter m in a range 1 <= m <= 100 000:"))

nArray = [0] * n
for i in range(n):
    while 1 > nArray[i] or nArray[i] > 1000000000:
        nArray[i] = int(input("Please enter %d element of array with "
                              "n integers in a range "
                              "1 <= n[%d] <= 1 000 000 000: " % (i, i)))

listA = []
s = 0
for i in range(m):
    while True:
        s = int(input("Please enter %d element of set A with "
                      "m integers in a range"
                      " 1 <= n[%d] <= 1 000 000 000: " % (i, i)))

        if 1 <= s <= 1000000000:
            # checking for equal numbers in the same set (A),
            # set shouldn't consist the same numbers
            if s not in listA:
                listA.append(s)
                break
            else:
                print("You've entered a number which is already in set,"
                      " try again.\n")


listB = []
s = 0
for i in range(m):
    while True:
        s = int(input("Please enter %d element of set B with "
                      "m integers in a range 1 <= n[%d] "
                      "<= 1 000 000 000 "
                      "and which is not contained in set A: " % (i, i)))

        # 1. checking range
        # 2. checking if set B is disjoint with set A
        # 3. checking for equal numbers in the same set (B),
        # set shouldn't consist the same numbers
        if 1 <= s <= 1000000000 and s not in listA and s not in listB:
            listB.append(s)
            break
        elif s in listA:
            print("You've entered a number which is in set A, try again."
                  " \n Set A: ", listA)
        elif s in listB:
            print("You've entered a number which is already in set, "
                  "try again.\n")


# counting happiness
happiness = 0
for i in range(n):
    if nArray[i] in listA:
        happiness += 1
    if nArray[i] in listB:
        happiness -= 1

print("array n: ", nArray, "\nSet A: ", listA,
      "\nSet B: ", listB, "\nhappiness:", happiness)
