## STRING
name = "ada lovelace"

#manipulação de strings
print(name.title()) #Ada Lovelace
name = "Ada Lovelace"
print(name.upper()) #ADA LOVELACE
print(name.lower()) #ada lovelace

#concatenação
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

# caracteres de escape ou sequências de escape
print('Python')
print('\tPython')
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#manipulação de strings
favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#comment
import this