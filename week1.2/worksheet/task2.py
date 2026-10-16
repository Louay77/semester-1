# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys
import statistics
num = read_numbers()
if len(num)== 0 :
    sys.exit("Error: no numbers provided")

minimum = min(num)
maximum = max(num)
mean = sum(num)/len(num)
median = (statistics.median(num))
print (f"Minimum = {minimum}")
print (f" Maximum = {maximum}")
print (f"Mean = {mean}")
print (f"Median = {median}")

