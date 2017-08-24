#Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
#Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
n = 0
def sum_of(n):
    sum = 0
    for x in range (1, n+1):
        if x%3 == 0 or x%5 == 0 :
            sum = sum + x
    return sum

def product_of(n):
    sum = 1
    for x in range (1, n+1):
        if x%3 == 0 or x%5 == 0 :
            sum = sum * x
    return sum

def main():
    n = int(raw_input("enter value of n"))
    choice = raw_input("enter option to choose")
    my_dictionary = {"1":sum_of(n), "0":product_of(n)}
    print(my_dictionary[choice])

main()
