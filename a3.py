x = int(input("Enter the value of x"))
y = int(input("Enter the value of y"))
if x > y:
    print("x must be greater than y")
else:
    total_sum = sum(range(x,y))
    print("The sum of the numbers from x to y is:", total_sum)