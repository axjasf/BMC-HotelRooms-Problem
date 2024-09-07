import matplotlib.pyplot as plt

def f(n):
    return n

def g(n):
    return 3 * n + 1

def h(n):
    return n + 81

def calculate_value_groups(max_n):
    value_groups = []
    group_counts = []

    for n in range(1, max_n + 1):
        values = set([f(n), g(n), h(n)])
        
        matching_groups = [i for i, group in enumerate(value_groups) if group & values]
        
        if matching_groups:
            lowest_group_index = min(matching_groups)
            value_groups[lowest_group_index].update(values)
            for i in sorted(matching_groups[1:], reverse=True):
                value_groups[lowest_group_index].update(value_groups[i])
                del value_groups[i]
        else:
            value_groups.append(values)
        
        group_counts.append(len(value_groups))

    return group_counts, value_groups

def check_group_integrity(value_groups):
    all_values = {}
    integrity_failed = False
    for i, group in enumerate(value_groups, 1):
        for value in group:
            if value in all_values:
                print(f"Integrity check failed: Value {value} is in both group {all_values[value]} and group {i}.")
                integrity_failed = True
            else:
                all_values[value] = i
    
    if not integrity_failed:
        print("Integrity check passed: All groups are mutually exclusive.")
    return not integrity_failed

# User input
max_n = int(input("Enter the maximum value for n: "))
print_choice = input("Print output? (n: no output / g: print groups / s: print sizes): ").lower()
plot_choice = input("Plot the diagram? (y/n): ").lower() == 'y'

# Run the calculation
group_counts, value_groups = calculate_value_groups(max_n)

# Print output based on user choice
if print_choice == 'g':
    print("\nFinal value groups:")
    for i, group in enumerate(value_groups, 1):
        print(f"Group {i}: {sorted(group)}")
elif print_choice == 's':
    print("\nFinal group sizes:")
    for i, group in enumerate(value_groups, 1):
        print(f"Group {i}: {len(group)} members")

if plot_choice:
    # Create the graph
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, max_n + 1), group_counts, marker='o')
    plt.title(f"Growth of Value Groups up to n={max_n}")
    plt.xlabel("n")
    plt.ylabel("Number of Groups")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

print(f"\nTotal number of groups: {len(value_groups)}")

# Perform integrity check
check_group_integrity(value_groups)