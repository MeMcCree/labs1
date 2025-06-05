largest = int(input())
medium = int(input())
smallest = int(input())

if (largest < medium):
	largest, medium = medium, largest

if (medium < smallest):
	medium, smallest = smallest, medium

if (largest < smallest):
	largest, smallest = smallest, largest

if (largest < medium):
	largest, medium = medium, largest

if (medium < smallest):
	medium, smallest = smallest, medium

if (largest < smallest):
	largest, smallest = smallest, largest

print(largest, medium, smallest, sep='\n')