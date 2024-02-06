a=5
b=0

try:
    print(a/b)
except Exception:
    print("cannot divide by zero")

print ("hello")

a=5
b=0

try:
    print(a/b)
except Exception as e:
    print("cannot divide by zero",e)
    # when we print "e" it gives what type of exception error(division by zero)

print ("hello")

a=5
b=0

try:
    print("resources open")
    print(a/b)
except Exception as e:
    print("cannot divide by zero",e)
    # when we print "e" it gives what type of exception error(division by zero)

finally:
    print("resources closed")

# finally block will be executed if we get error as well as, if we don't get the error.


a=5
b=2
# Take the value b=2 to execute the user input in try block

try:
    print("resources open")
    print(a/b)
    # taking an user input
    k=int(input("Enter the num"))
    print(k)
except ZeroDivisionError as e:
    print("cannot divide by zero",e)
except ValueError as e:
    print("Invalid Input",e)
    # when user give the input as 'p' we get ValueError
except Exception as e:
    print("Something went wrong")
     # To resolve any other exceptions it

finally:
    print("resources closed")
