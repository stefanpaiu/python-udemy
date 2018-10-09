import json
with open('exercise_1_linux_scripting_and_admin/input.json', 'r') as input:
    obj = json.load(input)
    print('Hello, ' +  obj['name'])
    with open('exercise_1_linux_scripting_and_admin/output.txt', 'w') as output:
        output.write(obj['name'] + "'s Hobbies are:\n")
        for hobby in obj['hobbies']:
                output.write(hobby + "\n")