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

#decimal to binary - print(bin(4).replace("0b",""))
f_oxy = open("puzzle3.txt", "r")
#f_oxy = ["00100", "11110", "10110", "10111", "10101", "01111",
 #"00111", "11100", "10000", "11001", "00010", "01010"]
new_f_oxy = []
#f_co2 = ["00100", "11110", "10110", "10111", "10101", "01111",
# "00111", "11100", "10000", "11001", "00010", "01010"]
new_f_co2 = []
f_co2 = open("puzzle3.txt", "r")
ones = 0 #[0,0,0,0,0]#,0,0,0,0,0,0,0]
zeros = 0 #[0,0,0,0,0]#,0,0,0,0,0,0,0]
oxy = ""
co2 = ""
a = 0
for x in f_oxy:
   new_f_oxy.append(x)
for x in f_co2:
   new_f_co2.append(x)

f_oxy = new_f_oxy
f_co2 = new_f_co2

while a < 12:
   if len(f_oxy) != 1:
      new_f_oxy = []
      for x in f_oxy:
         if int(x[a]) == 1:
            ones += 1
         else:
            zeros += 1
         
      for x in f_oxy:
         if ones >= zeros:
            if int(x[a]) == 1:
               new_f_oxy.append(x)
         else:
            if int(x[a]) == 0:
               new_f_oxy.append(x) 
      f_oxy = new_f_oxy
      
   a += 1
   ones = 0
   zeros = 0
   
oxy = int(f_oxy[0],2)

a = 0
ones = 0
zeros = 0
while a < 12:
   if len(f_co2) != 1:
      new_f_co2 = []
      for x in f_co2:
         if int(x[a]) == 1:
            ones += 1
         else:
            zeros += 1
      
      for x in f_co2:
         if zeros <= ones:
            if int(x[a]) == 0:
               new_f_co2.append(x)
         else:
            if int(x[a]) == 1:
               new_f_co2.append(x)
         f_co2 = new_f_co2
         
   a += 1
   ones = 0
   zeros = 0
   
co2 = int(f_co2[0],2)

print("Day 3, Puzzle 2: ",oxy*co2)


###################################DAY 4: PUZZLE 1####################################################
f = open("puzzle4.txt", "r")
nums = []
boards = []
board = []
row_count = 0
winning_board = []
for x in f:  #one line in f
   if len(board) < 5:
      if x != '\n': #skipping blank lines
         if len(x) > 15: #grabbing the numbers called
            for a in x.split(","):
               nums.append(a.replace("\n",""))
         else: #grabbing a row of the board
            row = []
            while len(row) < 5:
               for b in x.split(" "):
                  if b != '':
                     row.append([b.replace("\n",""),"no"])
            board.append(row)
   else:
      boards.append(board)
      board = []
#append the last board
boards.append(board)

winner = 0
number_drawn = 0

for x in nums:
   number_drawn = int(x)
   for board in boards:
      for row in board:
         for val in row:
            if int(val[0]) == int(x): #if the value in the row matches the number called
               val[1]= "yes"
         #check the rows for all yeses
            if row[0][1] == "yes" and row[1][1] == "yes" and row[2][1] == "yes" and row[3][1] == "yes" and row[4][1] == "yes":
               winner = 1
               winning_board = board
               break            
         if winner == 1:
            break
      i = 0 
      while i < 5:
         if board[0][i][1] == "yes" and board[1][i][1] == "yes" and board[2][i][1] == "yes" and board[3][i][1] == "yes" and board[4][i][1] == "yes":
            winner = 1
            winning_board = board
            break
         i += 1
      if winner == 1:
         break
   if winner == 1:
      break     

score = 0
for row in winning_board:
   for val in row:
      if val[1] == "no":
         score += int(val[0])
print("Day 4, Puzzle 1: ", score*number_drawn)
         
###################################DAY 4: PUZZLE 2####################################################
f = open("puzzle4.txt", "r")
nums = []
boards = []
board = []
row_count = 0
winning_board = []
for x in f:  #one line in f
   if len(board) < 5:
      if x != '\n': #skipping blank lines
         if len(x) > 15: #grabbing the numbers called
            for a in x.split(","):
               nums.append(a.replace("\n",""))
         else: #grabbing a row of the board
            row = []
            while len(row) < 5:
               for b in x.split(" "):
                  if b != '':
                     row.append([b.replace("\n",""),"no"])
            board.append(row)
   else:
      boards.append(board)
      board = []
#append the last board
boards.append(board)

number_drawn = -1
board_completion = []

for x in nums:
   for board in boards:
      for row in board:
         for val in row:
            if int(val[0]) == int(x): #if the value in the row matches the number called
               val[1]= "yes"
         #check the rows for all yeses
            if row[0][1] == "yes" and row[1][1] == "yes" and row[2][1] == "yes" and row[3][1] == "yes" and row[4][1] == "yes":
               if boards.index(board) not in board_completion:
                  board_completion.append(boards.index(board))
                  if len(board_completion) == len(boards) and winning_board == []:
                     winning_board = board
                     number_drawn = x
                     break
               if number_drawn != -1:
                  break
            if number_drawn != -1:
               break
         if number_drawn != -1:
               break
      if number_drawn != -1:
            break
      i = 0 
      while i < 5:
         if board[0][i][1] == "yes" and board[1][i][1] == "yes" and board[2][i][1] == "yes" and board[3][i][1] == "yes" and board[4][i][1] == "yes":
            if boards.index(board) not in board_completion:
               board_completion.append(boards.index(board))
               if len(board_completion) == len(boards) and winning_board == []:
                  winning_board = board
                  number_drawn = x
                  break
            if number_drawn != -1:
               break
         if number_drawn != -1:
               break

         i += 1
      if number_drawn != -1:
         break
   if number_drawn != -1:
      break
    
score = 0
for row in winning_board:
   for val in row:
      if val[1] == "no":
         score += int(val[0])
print("Day 4, Puzzle 2: ", score*int(number_drawn))
