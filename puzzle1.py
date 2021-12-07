###################################DAY 1: PUZZLE 1####################################################
f = open("puzzle1.txt", "r")
##f = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
final = 0 #final count
y = -1 #the before value
for x in f: #x is the after value
   if int(y) != -1:
      if int(x) > int(y): #if after is bigger than before
         final+=1
   y = x
    
print("Day 1, Puzzle 1: ", final)

###################################DAY 1: PUZZLE 2####################################################
f = open("puzzle1.txt", "r")
#f = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
final = 0 #final count
y = -1 #the first value
z = -1 #the second value
a = -1 #the third value
for x in f: #x is the fourth value
    if int(y) != -1:
        if int(z) != -1:
            if int(a) != -1:
                if (int(y)+int(z)+int(a)) < (int(z)+int(a)+int(x)): #if after is bigger than before
                    final+=1
                y = z
                z = a
                a = x
            else:
                a = x
        else:
            z = x
    else:
        y = x    
    
print("Day 1, Puzzle 2: ",final)

###################################DAY 2: PUZZLE 1####################################################

horizontal = 0
depth = 0
#f = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
f = open("puzzle2.txt", "r")
for x in f:
    cmd = -1
    for val in x.split():
        if cmd != -1:
            if cmd == "forward":
                horizontal += int(val)
            elif cmd == "up":
                depth -= int(val)
            else:
                depth += int(val)
            cmd = -1
        else:
            cmd = val
print("Day 2, Puzzle 1: ",horizontal*depth)

###################################DAY 2: PUZZLE 2####################################################

horizontal = 0
depth = 0
aim = 0
#f = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
f = open("puzzle2.txt", "r")
for x in f:
    cmd = -1
    for val in x.split():
        if cmd != -1:
            if cmd == "forward":
                if int(aim) != 0:
                    depth = depth +(aim*int(val))
                horizontal += int(val)
            elif cmd == "up":
                aim -= int(val)
            else:
                aim += int(val)
            cmd = -1
        else:
            cmd = val
print("Day 2, Puzzle 2: ", horizontal*depth)

###################################DAY 3: PUZZLE 1####################################################

#decimal to binary - print(bin(4).replace("0b",""))
#f = ["00100", "11110", "10110", "10111", "10101", "01111",
  #   "00111", "11100", "10000", "11001", "00010", "01010"]
f = open("puzzle3.txt", "r")
ones = [0,0,0,0,0,0,0,0,0,0,0,0]
zeros = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma = ""
eplison = ""
for x in f:
    a = 0
    while a < len(x)-1:
        if int(x[a]) == 1:
            ones[a] += 1
        else:
            zeros[a] += 1
        a += 1
a = 0
while a < len(ones):
    if int(ones[a]) > int(zeros[a]):
        gamma += "1"
        eplison += "0"
    else:
        gamma += "0"
        eplison += "1"
    a += 1
final = int(gamma,2)*int(eplison,2)
print("Day 3, Puzzle 1: ",final)

###################################DAY 3: PUZZLE 2####################################################

