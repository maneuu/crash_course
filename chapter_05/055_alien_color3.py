alien_color_list = ['green',
                    'yellow',
                    'red']

alien_color = alien_color_list[0]

if alien_color == 'green':
    num_points = 5
elif alien_color == 'yellow':
    num_points = 10
elif alien_color == 'red':
    num_points = 15

print(f"you chose {alien_color}, you won {num_points} points")
