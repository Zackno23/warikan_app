def calculation(amount, number_of_people):
    price = amount // number_of_people
    rest = amount % number_of_people
    return price, rest


amount = int(input("合計金額は："))
number_of_people = int(input('人数は'))

result = calculation(amount, number_of_people)
print(result)
print(result[0])
print(result[1])
