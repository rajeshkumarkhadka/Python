#Write a program that prints a multiplication table for numbers up to 12.
def main() :
    n = int(raw_input("enter the number to gerenate table"))
    for x in range (1, n+1):
        print("table of **** {0} **** ".format(x) + "\n")
        for y in range(1, 11):
            print("{0} * {1} = {2}".format(x, y, x*y))
        print("\n")
main()
