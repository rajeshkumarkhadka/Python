# Write a program that asks the user for their name and greets them with their name.
# Modify the previous program such that only the users Alice and Bob are greeted with their names.
def main():
    my_name = raw_input("enter your name ")
    if (my_name.lower() == "Alice".lower()) or (my_name.lower() == "Bob".lower()) :
        print("hello {0}".format(my_name))
    else:
        print("your are spy")

main()
