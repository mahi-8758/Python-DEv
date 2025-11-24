from statistics import mean, median, mode

numbers = [10, 20, 20, 30, 40, 40, 40, 50, 60]

mean_value = mean(numbers)
median_value = median(numbers)
mode_value = mode(numbers)
print("MEAN, MEDIAN, MODE")
print(f"Numbers: {numbers}")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
