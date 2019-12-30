#This is basic code to walk through the tutorials as I learn python.
print("Hello Chip")

#Combing Text
p1 = "This is a"
p2 = " test of combining text"

print(p1+p2)

#Getting substring
print(p1[0:4])

#Begining to letter
print(p1[:3])

#End letter
print(p1[4:])

#Create a basic list, get length

baseball_numbers = [11, 21, 31, 0, 99]
print(len(baseball_numbers))

# Basic loop
print("Starting loop")
i = 0
while i<10:
    print(i)
    i=i+1
print("All Done with loop")

print("\n ---------------Testing a if statement--------------")
x = int(input("Please enter an integer: "))

if x > 50:
    print("Greater than 50")

elif x > 20 and x < 50:
    print("Your number is between 20 & 50")

else:
    print("< 20")

print("\n ---------------Testing a for statement--------------")
i=1
for a in baseball_numbers:
    i+=1
    print("Number choice "+ str(i) + " is " + str(a))
