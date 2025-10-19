import random

names = input("Give me everybody's names, separated by a comma: ")
name_list = names.split(", ")

random_choice = random.randint(0, len(name_list) - 1)
person_who_will_pay = name_list[random_choice]

print(f"{person_who_will_pay} is going to buy the meal today!")