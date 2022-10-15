
print(""""
Welcome to Mad Libs
Lets Play a game
Type in two adjectives and one noun
A Madlib response will be displayed.

**An adjective denotes a descriptive word that illustrates the noun used in a sentence.
**A noun is a word that connotes a particular name, place, idea, or object.
      """)


def read_template(path):
    try:
        with open(path,'r') as story:
            return story.read()
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(my_str):
    stripped = ''
    parts = []
    capture = False
    current = ''

    for char in my_str:
        if char == '{':
            stripped += char
            capture = True
            current = ''
        elif char == '}':
            stripped += char
            capture = False
            parts.append(current)
        elif capture:
            current += char
        else:
            stripped += char

    return stripped, tuple(parts)


def merge(string, user_input):
    merge_output = string.format(*user_input)
    return merge_output

