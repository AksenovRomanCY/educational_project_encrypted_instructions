"""Decrypts compressed instructions for a Mars rover.

ID_YANDEX_CONTEST: 124005275

The Mars rover receives commands from Earth in a compressed format
to save bandwidth. Each instruction in the command string represents an action:
- с — take a photo;
- в — collect a soil sample;
- ш — take a step;
- о — turn on the lights;
- и — initiate a local scan.

Commands are compressed in a format where a number before square brackets
indicates the repetition of the sequence within. For example, 10[с] translates
to ten consecutive photo commands. Nested brackets represent deeper layers of
repetition, like 2[ш3[с]]10[с], which expands to "шсссшссссс".

This module provides a function to decode these compressed commands, producing
a full string of individual instructions for the rover.

Functions provided:
- decipher_instructions: Expands the compressed command string into the
  full sequence of rover instructions.
- main: Reads input from stdin, calls the decipher_instructions
  function, and prints the result.

Input format:
- A single string containing the compressed commands, e.g., "3[a]2[bc]".
  The string contains letters, numbers, and square brackets.

Output format:
- A string of expanded commands, e.g., "aaabcbc".

Constraints:
- Input string length: 0 to 30 characters.
- Numbers in the string are between 1 and 300.
- The input is guaranteed to be valid with well-formed brackets.

This module can be used in communications systems where command strings
are compressed and need to be expanded before execution by a device.
"""
import sys


def decipher_instructions(
        encrypted_instructions: str
        ) -> str:
    """Decrypts compressed messages.

    Args:
        encrypted_instructions (str): Compressed command string.

    Returns:
        str: Encrypted message.
    """
    # Stack to store strings at each nesting level (before opening '[').
    string_stack = []

    # Stack for storing numbers that determine the number
    # of repetitions for the current sequence.
    number_stack = []

    # The current string being collected, which will be expanded
    # as characters are processed.
    current_string = ''

    # The current number for repeats, which is updated when
    # digits before '[' are found.
    current_number = 0

    for symbol in encrypted_instructions:
        if symbol.isdigit():
            # Update current_number for repeat.
            current_number = current_number * 10 + int(symbol)
        elif symbol == '[':
            # Save the current number and string to the stacks.
            number_stack.append(current_number)
            string_stack.append(current_string)

            # Reset the current ones.
            current_string = ''
            current_number = 0
        elif symbol == ']':
            # Terminate the current string using the last
            # number from the stack.
            repeat_num = number_stack.pop()
            last_str = string_stack.pop()
            current_string = last_str + current_string * repeat_num
        else:
            # Add symbol to current_string.
            current_string += symbol

    # Return the expanded commands.
    return current_string


def main():
    """Main function."""
    cipher = sys.stdin.readline().rstrip()
    print(decipher_instructions(
        encrypted_instructions=cipher))


if __name__ == '__main__':
    main()
