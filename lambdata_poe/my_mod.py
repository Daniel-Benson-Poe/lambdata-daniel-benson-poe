


def enlarge(n):
    return int(n) * 100

if __name__ == "__main__":
    # Only run the following code
    # when we run this script from
    # the command-line
    # Otherwise don't invoke this 
    # code (for example when import
    # from another file)

    x = 5
    print(enlarge(x))

    z = input("Please choose a number to enlarge (ex. 4): ")
    print(enlarge(int(z)))