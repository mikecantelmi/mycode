dogs = []
fish = []

pets = [{"type": "dog", "name": "mudge", "age": 4},
        {"type": "fish", "name": "dorothy", "age": "3 days"},
        {"type": "dog", "name": "bingo", "age": 12},
        {"type": "fish", "name": "nemo", "age": 2},
        {"type": "cat", "name": "fluffy", "age": 1}
        ]

# my code

for x in pets:
    if x["type"] == "dog":
        dogs.append(x)
        print(x["name"] + ' is my pet dog')
    elif x["type"] == "fish":
        fish.append(x)
        print(x["name"] + ' is my pet fish')
    else:
        print(x["name"] + ' is not my pet')


