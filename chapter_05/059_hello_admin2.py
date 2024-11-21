usernames = [
    "SussyExplorer",
    "CodeEndemic",
    "BicycleNomad",
    "VectorHunter",
    "PixelPathfinder",
    "HelioRider",
    "DailyQuestor",
    "admin"
]
usernames.clear()
print(usernames)
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see the relatory status?")
        else:
            print(f"Welcome {username}")
else:
    print("The list is empty")
    print("We need to find some users.!")