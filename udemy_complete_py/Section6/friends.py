
# ask user for a list of 3 friends
# for each friend, we'll tell the user whether they are nearby
# for each nearby friend, we'll save their name to the 'nearby_friends.txt'

user_friends = input('Enter three friends names (separated by spaces only): ')

user_friends_list = user_friends.split(" ")

people_file = open('people.txt', 'r')
people_list = people_file.readlines()

people = [person.strip() for person in people_list]

people_file.close()

nearby_list = []

for element in user_friends_list:
    if element in people:
        nearby_list.append(element)
    else:
        continue

f = open('nearby_friends.txt', 'w')

for element in nearby_list:
    print(f'{element} is nearby!')
    f.write(f'{element}\n')
# [f.write(str(friend)+"\n") for friend in nearby_list]

f.close()