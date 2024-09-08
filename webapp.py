import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def f(n):
    return n

def g(n):
    return 3 * n + 1

def h(n):
    return n + 81

# Modify the calculate_value_groups function to distinguish between merges and folds
def calculate_value_groups(max_n):
    value_groups = []
    group_counts = []
    development_data = []

    for n in range(1, max_n + 1):
        new_values = set([f(n), g(n), h(n)])
        
        matching_groups = []
        for i, group in enumerate(value_groups):
            if not new_values.isdisjoint(group):
                matching_groups.append(i)
        
        if matching_groups:
            lowest_group_index = min(matching_groups)
            if len(matching_groups) == 1:
                action = f"Merged new values into group {lowest_group_index + 1}"
                value_groups[lowest_group_index].update(new_values)
            else:
                folded_groups = [value_groups[i] for i in matching_groups[1:]]
                action = f"Folded groups {', '.join(map(str, matching_groups[1:]))} (members: {folded_groups}) into group {lowest_group_index + 1}"
                for i in sorted(matching_groups[1:], reverse=True):
                    value_groups[lowest_group_index].update(value_groups[i])
                    del value_groups[i]
                value_groups[lowest_group_index].update(new_values)
        else:
            value_groups.append(new_values)
            action = "Created new group"
        
        group_counts.append(len(value_groups))
        
        development_data.append({
            'n': n,
            'new_values': new_values,
            'action': action,
            'groups': [sorted(group) for group in value_groups],
            'total_groups': len(value_groups)
        })

    return group_counts, value_groups, development_data

def check_group_integrity(value_groups):
    all_values = {}
    integrity_failed = False
    for i, group in enumerate(value_groups, 1):
        for value in group:
            if value in all_values:
                st.warning(f"Integrity check failed: Value {value} is in both group {all_values[value]} and group {i}.")
                integrity_failed = True
            else:
                all_values[value] = i
    
    if not integrity_failed:
        st.success("Integrity check passed: All groups are mutually exclusive.")
    return not integrity_failed

st.set_page_config(layout="wide")

st.title("Hotel Rooms Problem Solver and Visualizer")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Input", "Development", "Diagram"])

# Input section
if page == "Input":
    st.header("Input Parameters")
    max_n = st.number_input("Enter the maximum value for n:", min_value=1, value=10)
    if st.button("Calculate"):
        st.session_state.group_counts, st.session_state.value_groups, st.session_state.development_data = calculate_value_groups(max_n)
        st.session_state.calculated = True
        st.success("Calculation complete! Navigate to Development or Diagram to see results.")

# Development section
elif page == "Development":
    if 'calculated' not in st.session_state or not st.session_state.calculated:
        st.warning("Please calculate the results first in the Input section.")
    else:
        st.header("Development of Groups")
        
        # Filter options
        filter_option = st.selectbox("Filter steps:", ["All", "Merges only", "Folds only", "Merges and Folds"])
        
        for i, step in enumerate(st.session_state.development_data):
            # Determine the type of action
            is_merge = "Merged new values" in step['action']
            is_fold = "Folded groups" in step['action']
            is_new = "Created new group" in step['action']
            
            # Apply filter
            if filter_option == "Merges only" and not is_merge:
                continue
            if filter_option == "Folds only" and not is_fold:
                continue
            if filter_option == "Merges and Folds" and not (is_merge or is_fold):
                continue
            
            # Create a header with action information
            if is_fold:
                header = f"⚠️ Step n = {step['n']} (Fold)"
            elif is_merge:
                header = f"🔀 Step n = {step['n']} (Merge)"
            elif is_new and i > 0:
                header = f"➕ Step n = {step['n']} (New Group)"
            else:
                header = f"Step n = {step['n']}"
            
            # Add group count change information
            if i > 0:
                prev_count = st.session_state.development_data[i-1]['total_groups']
                curr_count = step['total_groups']
                if curr_count != prev_count:
                    header += f" (Groups: {prev_count} → {curr_count})"
            
            with st.expander(header):
                st.write(f"New values: {step['new_values']}")
                st.write(f"Action: {step['action']}")
                st.write("Current groups:")
                for j, group in enumerate(step['groups'], 1):
                    st.write(f"Group {j}: {sorted(group)}")
                st.write(f"Total groups: {step['total_groups']}")
        
        st.subheader(f"Total number of groups: {len(st.session_state.value_groups)}")
        check_group_integrity(st.session_state.value_groups)

# Diagram section
elif page == "Diagram":
    if 'calculated' not in st.session_state or not st.session_state.calculated:
        st.warning("Please calculate the results first in the Input section.")
    else:
        st.header("Group Count Diagram")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(range(1, len(st.session_state.group_counts) + 1), st.session_state.group_counts, marker='o')
        ax.set_title(f"Growth of Value Groups up to n={len(st.session_state.group_counts)}")
        ax.set_xlabel("n")
        ax.set_ylabel("Number of Groups")
        ax.grid(True)
        st.pyplot(fig)

st.sidebar.info("This app solves and visualizes the Hotel Rooms Problem.")