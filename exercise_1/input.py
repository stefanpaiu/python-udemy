import json
with open('exercise_1/input.json', 'r') as input:
    obj = json.load(input)
    print('Hello, ' +  obj['name'])
    with open('exercise_1/output.txt', 'w') as output:
        output.write(obj['name'] + "'s Hobbies are:\n")
        for hobby in obj['hobbies']:
                output.write(hobby + "\n")