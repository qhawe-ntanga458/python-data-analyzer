# Python Data Analyzer
# A beginner project for analyzing numerical data.

from statistics import median


def analyze_data(numbers):
"""Calculate summary statistics for a list of numbers."""

if not numbers:
raise ValueError("The data list cannot be empty.")

if not all(
isinstance(number, (int, float)) and not isinstance(number, bool)
for number in numbers
):
raise TypeError("All values must be numbers.")

total = sum(numbers)
average = total / len(numbers)
highest = max(numbers)
lowest = min(numbers)
middle = median(numbers)
data_range = highest - lowest

return {
"count": len(numbers),
"total": total,
"average": average,
"median": middle,
"highest": highest,
"lowest": lowest,
"range": data_range,
}


def main():
numbers = [120, 250, 180, 300, 150]

results = analyze_data(numbers)

print("=== PYTHON DATA ANALYZER ===")
print(f"Data: {numbers}")
print(f"Number of values: {results['count']}")
print(f"Total: {results['total']}")
print(f"Average: {results['average']:.2f}")
print(f"Median: {results['median']}")
print(f"Highest value: {results['highest']}")
print(f"Lowest value: {results['lowest']}")
print(f"Range: {results['range']}")


if __name__ == "__main__":
main()
