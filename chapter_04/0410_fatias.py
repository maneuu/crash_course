colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black"]

print(colors)
print("\nOs 3 primeiros elementos: ")
for color in colors[:3]:
  print(color)

print("\nOs 3 elementos do meio:")
for color in colors[3:6]:
  print(color)

print("\nOs 3 últimos elementos:")
for color in colors[-3:]:
  print(color)