file = open("2.4/responses.csv")

#junk = file.readline()

#data = file.readline()

#print(data)

#datalist = data.split(",")
#print(datalist)

for line in file:
    if"jeremy" in line.lower():
        liner = line.split(",")
        print(line)
        print(liner)
