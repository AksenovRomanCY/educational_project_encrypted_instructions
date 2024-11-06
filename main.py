import sys


def decipher_instructions(
        encrypted_instructions: str
        ) -> str:
    pass


def main():
    cypher = sys.stdin.readline().rstrip()
    print(decipher_instructions(
        encrypted_instructions=cypher))


if __name__ == "__main__":
    main()
