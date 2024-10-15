__author__ = "Prayas"

questions = [
    {
        "question": "What is the difference between a Python tuple and Python list?",
        "options": [
            "Lists are mutable and tuples are not mutable",
            "Tuples can be expanded after they are created and lists cannot",
            "Lists maintain the order of the items and tuples do not maintain order",
            "Lists are indexed by integers and tuples are indexed by strings"
        ],
        "answer": "Lists are mutable and tuples are not mutable"
    },
    {
        "question": "Which of the following methods work both in Python lists and Python tuples?",
        "options": [
            "reverse()",
            "sort()",
            "append()",
            "pop()",
            "index()"
        ],
        "answer": "index()"
    },
    {
        "question": "What will end up in the variable y after this code is executed?",
        "code": "x , y = 3, 4",
        "options": [
            "3",
            "A two item tuple",
            "4",
            "A dictionary with the key 3 mapped to the value 4",
            "A two item list"
        ],
        "answer": "4"
    },
    {
        "question": "In the following Python code, what will end up in the variable y?",
        "code": "x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}\ny = x.items()",
        "options": [
            "A list of integers",
            "A list of strings",
            "A list of tuples",
            "A tuple with three integers"
        ],
        "answer": "A list of tuples"
    },
    {
        "question": "Which of the following tuples is greater than x in the following Python sequence?",
        "code": "x = (5, 1, 3)\nif ??? > x :\n   ...",
        "options": [
            "(6, 0, 0)",
            "(4, 100, 200)",
            "(5, 0, 300)",
            "(0, 1000, 2000)"
        ],
        "answer": "(6, 0, 0)"
    },
    {
        "question": "What does the following Python code accomplish, assuming the c is a non-empty dictionary?",
        "code": "tmp = list()\nfor k, v in c.items() :\n    tmp.append( (v, k) )",
        "options": [
            "It sorts the dictionary based on its key values",
            "It creates a list of tuples where each tuple is a value, key pair",
            "It computes the largest of all of the values in the dictionary",
            "It computes the average of all of the values in the dictionary"
        ],
        "answer": "It creates a list of tuples where each tuple is a value, key pair"
    },
    {
        "question": "If the variable data is a Python list, how do we sort it in reverse order?",
        "options": [
            "data = data.sort(-1)",
            "data.sort(reverse=True)",
            "data.sort.reverse()",
            "data = sortrev(data)"
        ],
        "answer": "data.sort(reverse=True)"
    },
    {
        "question": "Using the following tuple, how would you print 'Wed'?",
        "code": "days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')",
        "options": [
            "print(days[1])",
            "print(days(2))",
            "print(days{2})",
            "print(days.get(1,-1))",
            "print(days[2])"
        ],
        "answer": "print(days[2])"
    },
    {
        "question": "In the following Python loop, why are there two iteration variables (k and v)?",
        "code": "c = {'a':10, 'b':1, 'c':22}\nfor k, v in c.items() :\n    ...",
        "options": [
            "Because for each item we want the previous and current key",
            "Because the items() method in dictionaries returns a list of tuples",
            "Because there are two items in the dictionary",
            "Because the keys for the dictionary are strings"
        ],
        "answer": "Because the items() method in dictionaries returns a list of tuples"
    },
    {
        "question": "Given that Python lists and Python tuples are quite similar - when might you prefer to use a tuple over a list?",
        "options": [
            "For a list of items that want to use strings as key values instead of integers",
            "For a list of items that will be extended as new items are found",
            "For a temporary variable that you will use and discard without modifying",
            "For a list of items you intend to sort in place"
        ],
        "answer": "For a temporary variable that you will use and discard without modifying"
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
