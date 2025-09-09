import sys

data = sys.stdin.read()
print("You entered:")
print(data)

n = int(data.split()[0])

lst = list(map(int,data.split()[1:]))
rev_array=lst[::-1]

print("Reversed array :"," ".join(map(str,rev_array)))
