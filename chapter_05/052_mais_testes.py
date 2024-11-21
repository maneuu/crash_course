# conditional_tests.py

# Testes de igualdade e de não igualdade com strings
animal = 'dog'
print("Is animal == 'dog'? I predict True.")
print(animal == 'dog')  # True

print("\nIs animal != 'cat'? I predict True.")
print(animal != 'cat')  # True

print("\nIs animal == 'cat'? I predict False.")
print(animal == 'cat')  # False

# Testes usando a função lower()
name = 'Emanoel'
print("\nIs name.lower() == 'emanoel'? I predict True.")
print(name.lower() == 'emanoel')  # True

print("\nIs name.lower() == 'emanuel'? I predict False.")
print(name.lower() == 'emanuel')  # False

# Testes numéricos
age = 30
print("\nIs age == 30? I predict True.")
print(age == 30)  # True

print("\nIs age != 25? I predict True.")
print(age != 25)  # True

print("\nIs age > 25? I predict True.")
print(age > 25)  # True

print("\nIs age < 25? I predict False.")
print(age < 25)  # False

print("\nIs age >= 30? I predict True.")
print(age >= 30)  # True

print("\nIs age <= 29? I predict False.")
print(age <= 29)  # False

# Testes usando and e or
speed = 60
print("\nIs speed > 50 and speed < 70? I predict True.")
print(speed > 50 and speed < 70)  # True

print("\nIs speed > 50 or speed > 70? I predict True.")
print(speed > 50 or speed > 70)  # True

print("\nIs speed > 70 and speed < 90? I predict False.")
print(speed > 70 and speed < 90)  # False

# Testes para verificar se um item está em uma lista
colors = ['red', 'blue', 'green']
print("\nIs 'red' in colors? I predict True.")
print('red' in colors)  # True

print("\nIs 'yellow' in colors? I predict False.")
print('yellow' in colors)  # False

# Testes para verificar se um item não está em uma lista
print("\nIs 'purple' not in colors? I predict True.")
print('purple' not in colors)  # True

print("\nIs 'blue' not in colors? I predict False.")
print('blue' not in colors)  # False
