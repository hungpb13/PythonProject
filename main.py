# Exception = an event that interrupts the flow of a program
# TypeError, ValueError, ZeroDivisionError
# try --> except --> finally

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ValueError:
    print("Enter only number, please!")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except Exception: # Too broad exception clause
    print("Something went wrong!")
finally:
    print("Thanks! Have a nice day!")
