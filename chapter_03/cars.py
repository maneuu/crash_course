print("--" * 20, "\nsort()\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort() 
print(cars)
# ['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)
print(cars)
#['toyota', 'subaru', 'bmw', 'audi']

# Ordenando umalistatemporariamentecomafunção sorted()
# reservar a ordem original de uma lista, mas apresentá-la de forma ordenada
print("--" * 20, "\nsorted()\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:") 
print(cars)
print("\nHere is the sorted list:") 
print(sorted(cars))
print("\nHere is the original list again:") 
print(cars)

# Exibindo umalistaemordeminversa
print("--" * 20, "\nreverse()\n")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() 
print(cars)

# Descobrindo o tamanho de umalista
print("--" * 20, "\nlen()\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))