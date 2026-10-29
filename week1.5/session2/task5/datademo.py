# Week 1.5, Session 2: Task 5

from data import Dataset

filename = input("Enter a filename: ")

dataset = Dataset(filename)

print(f"Dataset size: {len(dataset)}")
print(f"Mean: {dataset.mean()}")
print(f"Median: {dataset.median()}")
print("Values:")
for value in dataset:
    print(value)
