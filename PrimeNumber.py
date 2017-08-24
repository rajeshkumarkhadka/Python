def main () :
    n = int (raw_input("enter the number"))
    for x in range(1, n+1):
        count = 0
        for y in range(1, x+1):
            if x%y == 0 : count += 1
        if count == 2:
            print("Number {0} is prime ".format(x))
main()
