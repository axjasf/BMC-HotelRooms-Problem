import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def f(n):
    return n

def g(n):
    return 3 * n + 1

def h(n):
    return n + 81

def calculate_value_groups(max_n, show_development=False):
    value_groups = []
    group_counts = []

    for n in range(1, max_n + 1):
        values = set([f(n), g(n), h(n)])
        
        if show_development:
            print(f"\n--- Step n = {n} ---")
            print(f"New values: {values}")
        
        matching_groups = []
        colliding_values = set()
        for i, group in enumerate(value_groups):
            common_values = group & values
            if common_values:
                matching_groups.append(i)
                colliding_values.update(common_values)
        
        if matching_groups:
            lowest_group_index = min(matching_groups)
            if show_development:
                print(f"Collisions found in groups: {[i+1 for i in matching_groups]}")
                print(f"Colliding values: {colliding_values}")
                print(f"Merging into group {lowest_group_index + 1}")
            
            value_groups[lowest_group_index].update(values)
            for i in sorted(matching_groups[1:], reverse=True):
                if show_development:
                    print(f"Folding group {i + 1} into group {lowest_group_index + 1}")
                value_groups[lowest_group_index].update(value_groups[i])
                del value_groups[i]
        else:
            if show_development:
                print("No collisions. Creating new group.")
            value_groups.append(values)
        
        group_counts.append(len(value_groups))
        
        if show_development:
            print(f"Current groups:")
            for i, group in enumerate(value_groups, 1):
                print(f"Group {i}: {sorted(group)}")
            print(f"Total groups: {len(value_groups)}")

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

def animate_group_development(max_n, animation_speed, show_members):
    fig, ax = plt.subplots(figsize=(12, 6))
    value_groups = []
    
    def animate(n):
        nonlocal value_groups
        ax.clear()
        values = set([f(n), g(n), h(n)])
        
        matching_groups = [i for i, group in enumerate(value_groups) if group & values]
        folded_groups = []
        if matching_groups:
            lowest_group_index = min(matching_groups)
            value_groups[lowest_group_index].update(values)
            for i in sorted(matching_groups[1:], reverse=True):
                folded_groups.append(i)
                value_groups[lowest_group_index].update(value_groups[i])
                del value_groups[i]
        else:
            value_groups.append(values)
        
        group_sizes = [len(group) for group in value_groups]
        bars = ax.bar(range(1, len(value_groups) + 1), group_sizes, align='center')
        
        for bar in bars:
            bar.set_color('lightblue')
        if matching_groups:
            bars[lowest_group_index].set_color('yellow')  # Merging
            for i in folded_groups:
                if i < len(bars):
                    bars[i].set_color('red')  # Folding
        elif value_groups:
            bars[-1].set_color('lightgreen')  # New group
        
        for i, (bar, group) in enumerate(zip(bars, value_groups)):
            if show_members:
                text = f"{sorted(group)}"
            else:
                text = str(len(group))
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                    text, ha='center', va='bottom', rotation=45, fontsize=8)
        
        ax.set_xlabel('Group Number')
        ax.set_ylabel('Group Size')
        ax.set_title(f'Value Groups at n = {n}')
        ax.set_ylim(0, max(max(group_sizes) + 1, 10))
        ax.set_xlim(0, max(len(value_groups) + 1, 10))
        
        textstr = f'New values: {values}'
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
                verticalalignment='top', bbox=props)
    
    ani = animation.FuncAnimation(fig, animate, frames=range(1, max_n + 1), 
                                  interval=animation_speed, repeat=False)
    plt.tight_layout()
    plt.show()

def main():
    print("Hotel Rooms Problem Solver and Visualizer")
    
    # Gather all inputs upfront
    max_n = int(input("Enter the maximum value for n: "))
    print_choice = input("Print output? (n: no output / g: print groups / s: print sizes / d: show development): ").lower()
    plot_diagram = input("Plot the group count diagram? (y/n): ").lower() == 'y'
    animate = input("Show animation? (y/n): ").lower() == 'y'
    
    if animate:
        animation_speed = int(input("Enter animation speed in milliseconds: "))
        show_members = input("Show group members in animation? (y/n): ").lower() == 'y'
    
    # Execute based on inputs
    group_counts, value_groups = calculate_value_groups(max_n, show_development=(print_choice == 'd'))
    
    # Print output based on user choice
    if print_choice == 'g':
        print("\nFinal value groups:")
        for i, group in enumerate(value_groups, 1):
            print(f"Group {i}: {sorted(group)}")
    elif print_choice == 's':
        print("\nFinal group sizes:")
        for i, group in enumerate(value_groups, 1):
            print(f"Group {i}: {len(group)} members")
    
    if plot_diagram:
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, max_n + 1), group_counts, marker='o')
        plt.title(f"Growth of Value Groups up to n={max_n}")
        plt.xlabel("n")
        plt.ylabel("Number of Groups")
        plt.grid(True)
        plt.show()
    
    print(f"\nTotal number of groups: {len(value_groups)}")
    
    # Perform integrity check
    check_group_integrity(value_groups)
    
    if animate:
        animate_group_development(max_n, animation_speed, show_members)

if __name__ == "__main__":
    main()