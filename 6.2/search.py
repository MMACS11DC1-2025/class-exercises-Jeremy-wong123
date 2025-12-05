file = open("6.2/spotify.csv")
junk = file.readline()

drake_data = []
data = []
song = []
for line in file:
	items = line.strip().split(",")
	artist = str(items[-1])
	songtitle = str(items[-2])
	danceability = float(items[1])
	
	if artist == "Drake":
		drake_data.append([danceability, songtitle, artist])
		data.append(danceability)
		song.append(songtitle)


for i in range(len(data)):
	current = data[i]
	index = i

	for j in range(i+1, len(data)):
		if data[j] < current:
			current = data[j]
			index = j
	
	data[index], data[i] = data[i], data[index]

top5 = data[-5:]
topf = song[-5:]
inde = 4
print("Dance score \tSong")
for item in top5:
	print(str(top5[inde]) + '\t' + str(topf[inde]))
	inde -= 1

