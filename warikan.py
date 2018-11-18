def warikan(amount, number_of_people):
    return f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円"


print(warikan(amount=1500, number_of_people=3))
print(warikan(amount=2000, number_of_people=3))
print(warikan(amount=3000, number_of_people=4))
