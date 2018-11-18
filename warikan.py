def calculate_warikan(amount, number_of_people):
    return f"1人あたり: {amount // number_of_people}円, 端数: {amount % number_of_people}円"


print(calculate_warikan(amount=1500, number_of_people=3))
print(calculate_warikan(amount=2000, number_of_people=3))
print(calculate_warikan(amount=3000, number_of_people=4))
