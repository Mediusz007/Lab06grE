
# Kalkulator

import sys

if len(sys.argv) != 4:
    print("Uzycie: calc.py <num1> <op +-> <num2>")
    sys.exit(1)


num1, op, num2 = sys.argv[1], sys.argv[2], sys.argv[3]


num1 = float(num1)
num2 = float(num2)


result = None


if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
else:
    print("Zly operator")
    sys.exit(1)


with open("/tmp/wynik.txt", "w") as file: 
    file.write(str(result))

print("wynik {}".format(result))

