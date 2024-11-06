import sys


def decipher_instructions(
        encrypted_instructions: str
        ) -> str:
    number_stack = []
    string_stack = []
    current_string = ""
    current_number = 0

    for char in encrypted_instructions:
        if char.isdigit():
            # Update current_number for repeat.
            current_number = current_number * 10 + int(char)
        elif char == '[':
            # Save the current number and string to the stacks.
            number_stack.append(current_number)
            string_stack.append(current_string)

            # Reset the current ones.
            current_string = ""
            current_number = 0
        elif char == ']':
            # Terminate the current string using the last
            # number from the stack.
            repeat_num = number_stack.pop()
            last_str = string_stack.pop()
            current_string = last_str + current_string * repeat_num
        else:
            # Add symbol to current_string.
            current_string += char

    return current_string


def main():
    cipher = sys.stdin.readline().rstrip()
    print(decipher_instructions(
        encrypted_instructions=cipher))


if __name__ == "__main__":
    main()
