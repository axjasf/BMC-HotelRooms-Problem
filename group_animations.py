import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def f(n):
    return n

def g(n):
    return 3 * n + 1

def h(n):
    return n + 81

def animate_group_development(max_n, animation_speed, show_members):
    fig, ax = plt.subplots(figsize=(12, 6))
    value_groups = []
    
    def animate(n):
        nonlocal value_groups
        ax.clear()
        values = set([f(n), g(n), h(n)])
        
        # Update value_groups
        matching_groups = [i for i, group in enumerate(value_groups) if group & values]
        if matching_groups:
            lowest_group_index = min(matching_groups)
            value_groups[lowest_group_index].update(values)
            for i in sorted(matching_groups[1:], reverse=True):
                value_groups[lowest_group_index].update(value_groups[i])
                del value_groups[i]
        else:
            value_groups.append(values)
        
        # Create bar chart
        group_sizes = [len(group) for group in value_groups]
        bars = ax.bar(range(1, len(value_groups) + 1), group_sizes, align='center')
        
        # Color coding
        for bar in bars:
            bar.set_color('lightblue')
        if matching_groups:
            bars[lowest_group_index].set_color('yellow')
        else:
            bars[-1].set_color('lightgreen')
        
        # Annotations
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
        
        # Add text box for new values
        textstr = f'New values: {values}'
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
                verticalalignment='top', bbox=props)
    
    ani = animation.FuncAnimation(fig, animate, frames=range(1, max_n + 1), 
                                  interval=animation_speed, repeat=False)
    plt.tight_layout()
    plt.show()

# Get user inputs
max_n = int(input("Enter the maximum value for n: "))
animation_speed = int(input("Enter the animation speed in milliseconds (e.g., 1000 for 1 second): "))
show_members = input("Show group members? (y/n): ").lower() == 'y'

# Call the function with user inputs
animate_group_development(max_n, animation_speed, show_members)