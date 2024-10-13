def calculate_love_score(name1, name2):
    name = (name1 + name2).lower()

    t = name.count("t")
    r = name.count("r")
    u = name.count("u")
    e = name.count("e")

    true = t + r + u + e

    l = name.count("l")
    o = name.count("o")
    v = name.count("v")
    e = name.count("e")

    love = l + o + v + e

    score = str(true) + str(love)

    print(score)


print("Calculate your love score!")

first_name = input("Type your name: ")
second_name = input("Type your match: ")


print(f"{first_name} and {second_name} you have a Grand Match of : ")
calculate_love_score(name1=first_name, name2=second_name)
