print("How many weeks do you have left till 90?")


def life_in_weeks(time):
    life_span = 90 * 52
    current_life = time * 52
    time_left = life_span - current_life
    print(f"You have {time_left} weeks left to reach 90.")


age = int(input("How old are you? "))
# age is assigned to time, time = age and used in function
life_in_weeks(age)
