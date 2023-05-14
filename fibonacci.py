def fibonacciByIndex(index: int) -> int:
    if index < 3:
        return index - 1

    a, b = 1, 1
    for _ in range(3, index + 1):
        a, b = b, a + b
    
    return b


def main():
    try:
        index = int(input("Enter fibonacci number index: "))
        if index > 0:
            print(f"Fibonnaci number undex index {index} is {fibonacciByIndex(index)}")
        else:
            print(f"{index} can not be used as an index for Fibinacci number")
    except:
        print("Only an integer can be used as a Fibonacci sequence index")


if __name__ == "__main__":
    main()