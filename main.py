def black_red():
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "Black"
        if i % 5 == 0:
            output += "Red"
        print(output if output else i)

if __name__ == "__main__":
    black_red()