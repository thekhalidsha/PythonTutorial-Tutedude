# Task 1: Check if a Number is Even or Odd
def main():
    num = int(input("Enter a Number: "))
    print(f"\n")
    
    if num % 2 == 0:
        print(f"{num} is an Even Number.")
    else:
        print(f"{num} is an Odd Number.")
        
main()