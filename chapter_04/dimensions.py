dimensions =(200, 50)  
print(dimensions[0]) 
print(dimensions[1]) 
# não se pode alterar valores de tuplas
# dimensions[0] = 250

print("\n\n")

print("Original dimensions:") 
for dimension in dimensions: 
  print(dimension)


#  Criando uma nova tupla e sobrescrevendo a variável
#  Isso não altera a tupla existente, mas sim cria uma nova tupla e atribui a ela o mesmo nome, dimensions
dimensions = (400, 100) 
print("\nModified dimensions:") 
for dimension in dimensions: 
  print(dimension)