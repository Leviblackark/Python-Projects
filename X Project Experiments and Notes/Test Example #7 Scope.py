enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies outside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope


def drink_potion():
    # the variables in this function are only valid in this function. Local scope
    # so potion_strength is local
    potion_strength = 2
    print(potion_strength)


drink_potion()

# Outside the function, so you get a Name Error
# print(potion_strength)

# Global scope
# player_health is a global variable
player_health = 10


def drink_potion():
    potion_strength = 2
    # using a global variable
    print(player_health)


drink_potion()
