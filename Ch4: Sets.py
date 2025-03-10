# use parameter to make display nicer according to the # string the user is inputting.
def getInput(num):
    string_num = "1st" if num == 1 else "2nd"
    inputted_string = input(f'Please enter your {string_num} string: ')
    return inputted_string


def uncommonConcat(inp_string_one, inp_string_two):
    # Create sets of characters from both strings
    set_one = set(inp_string_one)
    set_two = set(inp_string_two)

    uncommon_one = []
    uncommon_two = []
    # Find common characters: we can use the intersection to find the common characters in our sets.
    common_chars = set_one.intersection(set_two)

    # Get uncommon characters from the first string
    for char in inp_string_one:
        if char not in common_chars:
            uncommon_one.append(char)

    # Get uncommon characters from the first string
    for char in inp_string_two:
        if char not in common_chars:
            uncommon_two.append(char)

    # Concatenate string with the uncommon characters of our two input strings.
    return ''.join(uncommon_one) + ''.join(uncommon_two)


if __name__ == "__main__":
    string_one = getInput(1)
    string_two = getInput(2)

    output_string = uncommonConcat(string_one, string_two)
    print(output_string)
