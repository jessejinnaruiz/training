
qs = open('questions.txt', 'r')
print(qs)
questions = [element.strip() for element in qs.readlines()]
print(questions)

prompts = []
for element in questions:
    r.()