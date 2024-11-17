players = ['charles', 'martina', 'michael', 'florence', 'eli']

# Fatiando uma lista

print(players[0:3]) # 0 1 2 
print(players[1:4]) # 1 2 3 
print(players[:4]) # 0 1 2 3 
print(players[2:]) # 2 3 4 
print(players[-3:],end="\n"*3) # 2  3 4 ou -3 -2 -1 

# Percorrendo uma fatia com um laço 
print("Here are the first three players on my team:")
for player in players[:3]:
  print(player.title())
