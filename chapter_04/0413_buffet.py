pratos = ("Arroz com feijão", "Omelete", "Macarrão alho e óleo", "Salada de folhas", "Sanduíche de presunto e queijo")

print("Os pratos simples que temos hoje são: ")
for prato in pratos:
  print(prato, end=", ")
print('\n\n')

# não se pode modificar uma tupla apenas sobscrever
# pratos(0] = "new value" CODIGO É REJEITADO NO PYTHON E LOGO DA ERRO 

# SOBSCREVE A TUPLA pratos ANTERIOR E CRIA UMA NOVA TUPLA DO 0 COM O MESMO NOME
pratos = ("Sopa de legumes", "Frango grelhado com batatas", "Feijoada", "Pizza\
 Margherita", "Risoto de cogumelos")
print("Os pratos simples que temos hoje são: ")
for prato in pratos:
  print(prato, end=", ")

