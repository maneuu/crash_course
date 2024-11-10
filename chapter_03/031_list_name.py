names = ["Lucas", "Ana", "Gabriel"]
print(f"{names[0]} {names[1]} {names[2]}")


print('-' * 10)
for i in names:
  print(i, end=' ')
print(" ")
for i in range(len(names)):
    print(names[i], end=" ")
