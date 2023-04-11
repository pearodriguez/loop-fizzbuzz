# A loop that asks the user to enter a number. 
# The loop iterates 10 times and keeps a running total of the numbers entered.

print("\n") 
total = 0
for nums in range(1, 11):
    num1 = int(input("enter a number: "))
    total += num1
print("the total value is: ", total)

# A program that loops through numbers starting at 20 and ending at 0. For every odd number, the program  
# prints "Buzz" instead of the number, and for every even number, print "Fizz" instead of the number.

print("\n")
for nums in range (20, 0, -1):
    if nums % 2 == 0:
        print(nums, "Fizz")
    else: 
        print(nums, "Buzz")
