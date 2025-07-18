
# Variable define

size=int(input("Enter the size of the pattern: "))
i=1

# Nested loop to print the pattern

while i<=size:
    for j in range(1, size+1):
      print("*", end="")
    print()
    i += 1
