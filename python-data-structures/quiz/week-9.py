questions = [
    {
        "question": "How are Python dictionaries different from Python lists?",
        "options": [
            "Python lists are indexed using integers and dictionaries can use strings as indexes",
            "Python dictionaries are a collection and lists are not a collection",
            "Python lists can store strings and dictionaries can only store words",
            "Python lists store multiple values and dictionaries store a single value"
        ],
        "answer": "Python lists are indexed using integers and dictionaries can use strings as indexes"
    },
    {
        "question": "What is a term commonly used to describe the Python dictionary feature in other programming languages?",
        "options": [
            "Closures",
            "Sequences",
            "Associative arrays",
            "Lambdas"
        ],
        "answer": "Associative arrays"
    },
    {
        "question": "What would the following Python code print out?",
        "code": "stuff = dict()\nprint(stuff['candy'])",
        "options": [
            "The program would fail with a traceback",
            "0",
            "-1",
            "candy"
        ],
        "answer": "The program would fail with a traceback"
    },
    {
        "question": "What would the following Python code print out?",
        "code": "stuff = dict()\nprint(stuff.get('candy',-1))",
        "options": [
            "The program would fail with a traceback",
            "'candy'",
            "0",
            "-1"
        ],
        "answer": "-1"
    },
    {
        "question": "(T/F) When you add items to a dictionary they remain in the order in which you added them.",
        "options": [
            "False",
            "True"
        ],
        "answer": "False"
    },
    {
        "question": "What is a common use of Python dictionaries in a program?",
        "options": [
            "Computing an average of a set of numbers",
            "Sorting a list of names into alphabetical order",
            "Building a histogram counting the occurrences of various strings in a file",
            "Splitting a line of input into words using a space as a delimiter"
        ],
        "answer": "Building a histogram counting the occurrences of various strings in a file"
    },
    {
        "question": "Which of the following lines of Python is equivalent to the following sequence of statements assuming that counts is a dictionary?",
        "code": "if key in counts:\n    counts[key] = counts[key] + 1\nelse:\n    counts[key] = 1",
        "options": [
            "counts[key] = counts.get(key,0) + 1",
            "counts[key] = counts.get(key,-1) + 1",
            "counts[key] = (key in counts) + 1",
            "counts[key] = key + 1",
            "counts[key] = (counts[key] * 1) + 1"
        ],
        "answer": "counts[key] = counts.get(key,0) + 1"
    },
    {
        "question": "In the following Python, what does the for loop iterate through?",
        "code": "x = dict()\n...\nfor y in x :\n    ...",
        "options": [
            "It loops through the integers in the range from zero through the length of the dictionary",
            "It loops through all of the dictionaries in the program",
            "It loops through the values in the dictionary",
            "It loops through the keys in the dictionary"
        ],
        "answer": "It loops through the keys in the dictionary"
    },
    {
        "question": "Which method in a dictionary object gives you a list of the values in the dictionary?",
        "options": [
            "items()",
            "keys()",
            "values()",
            "all()",
            "each()"
        ],
        "answer": "values()"
    },
    {
        "question": "What is the purpose of the second parameter of the get() method for Python dictionaries?",
        "options": [
            "An alternate key to use if the first key cannot be found",
            "The value to retrieve",
            "To provide a default value if the key is not found",
            "The key to retrieve"
        ],
        "answer": "To provide a default value if the key is not found"
    }
]

for i, q in enumerate(questions, 1):
    print(f"Question {i}: {q['question']}")
    if "code" in q:
        print(q["code"])
    for j, option in enumerate(q["options"], 1):
        print(f"{j}. {option}")
    print(f"Answer: {q['answer']}")
    print("\n" + "-"*50 + "\n")
