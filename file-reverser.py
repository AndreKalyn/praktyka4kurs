import os

def canBeReversed(file_path: str) -> bool:
    return os.path.exists(file_path) and os.path.isfile(file_path)

def reverse(file_path: str) -> None:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    reversed_file_name = f"reversed-{os.path.basename(file_path)}"
    reversed_file_path = os.path.join(os.path.dirname(file_path), reversed_file_name)

    with open(reversed_file_path, "w", encoding="utf-8") as file:
        file.write(content[::-1])

def main():
    file_path = input("Enter file path: ")

    if (canBeReversed(file_path)):
        reverse(file_path)
        print("Reversed file is in the same directory as given file")
    else:
        print("File not found")


if __name__ == "__main__":
    main()
    