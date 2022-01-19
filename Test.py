Response = "121080080000000720560000000"

playerlocs = []
shotlocs = []
for i in range(int(Response[1])):
    playerlocs.append([int(Response[3 + (12 * i):6 + (12 * i)]), int(Response[6 + (12 * i):9 + (12 * i)])])
    shotlocs.append([int(Response[9 + (12 * i):12 + (12 * i)]), int(Response[12 + (12 * i):15 + (12 * i)])])

print (playerlocs)
print (shotlocs)