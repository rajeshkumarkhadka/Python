def main():
    print("**********Program to take input from standard input")

    a = int(input("enter first number "))
    b = int(input("enter second number "))
    s = "One two three"
    spilitted_string = s.split()
    print(spilitted_string[0]+" "+spilitted_string[1]+" " +spilitted_string[2])
    print("the sum of {0} and {1} is {2}".format(a, b, (a+b)))

main()
