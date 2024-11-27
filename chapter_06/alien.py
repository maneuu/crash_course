alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25

alien_0['color'] = 'yellow'# Modificando valores em umdicionário
print(alien_0)

print('-'*30, end="\n\n\n")

alien_0 = {'x_position': 0,
    'y_position': 25,
    'speed': 'medium'
}
print("Original x-position: " + str(alien_0['x_position']))
# Move o alienígena para a direita 
# Determina a distância que o alienígena deve se deslocar de acordo com sua 
# velocidade atual 
if alien_0['speed'] == 'slow': 
    x_increment = 1

elif alien_0['speed'] == 'medium': 
    x_increment = 2

else:
    # Este deve ser um alienígena rápido 
    x_increment = 3
    
# A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))