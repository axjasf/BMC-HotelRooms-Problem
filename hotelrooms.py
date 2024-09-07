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
        values = [f(n), g(n), h(n)]
        
        found_group = False
        for group in value_groups:
            if any(value in group for value in values):
                group.update(values)
                found_group = True
                break
        
        if not found_group:
            value_groups.append(set(values))
        
        group_counts.append(len(value_groups))

    return group_counts, value_groups

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