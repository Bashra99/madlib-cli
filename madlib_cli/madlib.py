#define functions
def read_template(str):
    """
    Reads the file and return it
    """
    file = open(str, "r")
    read = file.read()
    file.close()
    return read.strip()

def parse_template(str):
    """
    Parse the template and return a tuple
    """
    final_string = ""
    final_list = []
    capturing = False
    captured_word = ""
    for x in str:
        if capturing:
            if x == "}":
                capturing = False
                final_list.append(captured_word)
                captured_word = ""
                final_string += x
            else:
                captured_word += x

        else:
            final_string += x
            if x == "{":
                capturing = True

    return final_string, tuple(final_list)

def merge(str, tup):
    """
    Merge the template with the user input
    """
    return str.format(*tup)

#create program
print("""
*************************************
**      Welcome to Mad Lib         **
**  *****************************  **
**  You will be prompted to enter  **
**  different parts of speech.     **
**  Your answers will be used to   **
**  complete sentences and then    **
**  display them once they are     **
**  complete. This will usually    **
**  create some silly results.     **
**  *****************************  **
**           Have fun!             **
*************************************
""")

filepath = "assets/story.txt"

stripped, parts = parse_template(read_template(filepath))

responses = []
for x in parts:
    if x.lower() == "adjective":
        print(f"Enter an {x}")
        response = input("> ")
        responses.append(response)

    else:
        print(f"Enter a {x}")
        response = input("> ")
        responses.append(response)

answer = merge(stripped, tuple(responses))
print(answer)

#write answer to new file
f = open("assets/response.txt", "w")
f.write(answer)
f.close()