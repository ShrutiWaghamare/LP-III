def knapsack(capacity, weights, values, n):
    # Base case: no items or no capacity left
    if n == 0 or capacity == 0:
        return 0
    
    # If weight of the nth item is more than the capacity, skip this item
    if weights[n - 1] > capacity:
        return knapsack(capacity, weights, values, n - 1)
    
    # Otherwise, choose the maximum of either:
    # 1. Including the nth item
    # 2. Excluding the nth item
    include = values[n - 1] + knapsack(capacity - weights[n - 1], weights, values, n - 1)
    exclude = knapsack(capacity, weights, values, n - 1)
    return max(include, exclude)

def get_input():
    n = int(input("Enter the number of items: "))
    capacity = int(input("Enter the capacity of the knapsack: "))
    weights = []
    values = []
    
    for i in range(n):
        value = int(input(f"Enter value of item {i + 1}: "))
        weight = int(input(f"Enter weight of item {i + 1}: "))
        values.append(value)
        weights.append(weight)
    
    return capacity, weights, values, n

def main():
    capacity, weights, values, n = get_input()
    max_value = knapsack(capacity, weights, values, n)
    print(f"Maximum value that can be carried is: {max_value}")

main()
