# Janmansh and Coins
# anmansh received X coins of 10 rupees and Y coins of 5 rupees from Chingari.
# Since he is weak in math, can you find out how much total money does he have?
# Input Format
# The first line will contain T - the number of test cases. Then the test cases follow.
# The first and only line of each test case contains two integers X, Y - the number of 10 and 5 rupee coins respectively.
# Output Format
# For each test case, output how much total money does Janmansh have.
# Sample Input 1 
# 2 1
# 3 4
# Sample Output 1 
# 25
# 50

# Explanation
# Test case-1: He has 2 coins of 10 rupees and 1 coin of 5 rupees.
# Hence he has 2⋅10+5=25 rupees.
# Test case-2: He has 3 coins of 10 rupees and 4 coins of 5 rupees. 
# Hence he has 3⋅10+4⋅5=50 rupees.



def sub(x,y):
    z=x*10
    e=y*5
    f=z+e
    print(f)
x=int(input("enter the no:-"))
y=int(input("enter the no:-"))
sub(x,y)


