
data = []
with open('input.txt', "r") as file:
    for line in file.readlines():
        l = []
        for word in line.split():
            l.append(''.join(filter(lambda x: x.isalnum(), word)))
        data.append(tuple(l))

print(data)
dict = {data[i]: i for i in range (0,len(data), 1)}
print(dict)
