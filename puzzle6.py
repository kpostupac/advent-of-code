#####################################DAY 6, PUZZLE 1########################
file = open("puzzle6.txt", "r")
fish = []
for f in file:
    fish = f.split(",")
a = 0
while a < 80:
    new_fish = []
    for f in fish:
        if int(f) > 0:
            new_fish.append(int(f)-1)
        else:
            new_fish.append(6)
            new_fish.append(8)
    a += 1
    fish = new_fish
print("Day 6, Puzzle 1:", len(fish))

#####################################DAY 6, PUZZLE 2########################
file = open("puzzle6.txt", "r")
fish = [0,0,0,0,0,0,0,0,0]
for f in file:
    for x in f.split(","):
        fish[int(x)] += 1
a = 0
while a < 256:
    new_fish = [0,0,0,0,0,0,0,0,0]
    i = 0
    while i < 8:
        new_fish[i] = fish[i+1]
        i += 1
    new_fish[6] += fish[0]
    new_fish[8] += fish[0]
    a += 1
    fish = new_fish
i = 1
total = fish[0]
while i < 9:
    total += fish[i]
    i += 1
print("Day 6, Puzzle 2:", total)
    
