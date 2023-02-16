import numpy as np

rows = int(input("How many rows?"))
columns = int(input("How many columns?"))

while 5 > rows > 10:
    if 5 > rows:
        rows = input("There should be more than 5 rows. Try again: ")
    elif rows > 10:
        rows = input("There should be less than 10 rows. Try again: ")

while 5 > columns > 10:
    if 5 > columns:
        rows = input("There should be more than 5 columns. Try again: ")
    elif columns > 10:
        rows = input("There should be less than 10 column. Try again: ")

nums = np.random.randint(100,999, (rows, columns))

sum = 0
counter = 0

for i in nums:
    for num in i:
        sum += num
        print(num, end=" ")
    print("")
avg = sum/(rows*columns)
print("The sum is ",sum)
print("The average is ",avg)

if rows < columns:
    print("There are ", int(rows/2)," concentric rings.")
else:
    print("There are ", int(columns/2)," concentric rings.")

print("The numbers in the concentric ring are: ")
print(*nums[:,-1])
print(*list(reversed(nums[-1,:-1])))
print(*list(reversed(nums[:-1,0])))
print(*nums[0,:-1])

a = np.sum(nums[:,-1])
b = np.sum(nums[-1,:-1])
c = np.sum(nums[:-1,0])
d = np.sum(nums[0,:-1])
sum = a+b+c+d
print("The sum of the ring is ", sum)
print("The average of the ring is: ", sum/((rows+columns-1)*2))
