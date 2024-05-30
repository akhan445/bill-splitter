import random
# write your code here
def split_bill_equally(total, number_of_friends):
    return round(total / number_of_friends, 2)
number_of_friends = int(input("Enter the number of friends joining (including you):"))
friends = {}
lucky_one = ""

if (number_of_friends) <= 0:
    print("No one is joining for the party")

else:  
    print("Enter the name of every friend (including you), each on a new line:")
    for x in range(number_of_friends):
        name = input()
        friends[name] = 0
    
    
    total = int(input("Enter the total bill value:"))

    lucky_feature = input('Do you want to use "Who is lucky" feature? Write (Yes/No):')

    if lucky_feature == 'Yes':
        lucky_one = random.choice([*friends.keys()])
        print(f'{lucky_one} is the lucky one!')
        number_of_friends -= 1
    else:
        print('No one is going to be lucky')

    split_value = split_bill_equally(total, number_of_friends)

    for k, v in friends.items():
        if k == lucky_one:
            continue
        friends[k] = split_value

    print(friends)