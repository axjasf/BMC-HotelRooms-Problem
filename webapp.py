import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify
import io
import base64
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

def f(n):
    return n

def g(n):
    return 3 * n + 1

def h(n):
    return n + 81

def calculate_value_groups(max_n):
    value_groups = []
    group_counts = []
    all_groups = []

    for n in range(1, max_n + 1):
        values = set([f(n), g(n), h(n)])
        
        matching_groups = []
        for i, group in enumerate(value_groups):
            if group & values:
                matching_groups.append(i)
        
        if matching_groups:
            lowest_group_index = min(matching_groups)
            value_groups[lowest_group_index].update(values)
            for i in sorted(matching_groups[1:], reverse=True):
                value_groups[lowest_group_index].update(value_groups[i])
                del value_groups[i]
        else:
            value_groups.append(values)
        
        group_counts.append(len(value_groups))
        all_groups.append([sorted(list(group)) for group in value_groups])

    return group_counts, all_groups

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    app.logger.info('Received calculate request')
    max_n = int(request.form['max_n'])
    app.logger.info(f'Calculating for max_n: {max_n}')
    
    group_counts, all_groups = calculate_value_groups(max_n)
    
    # Generate plot
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, max_n + 1), group_counts, marker='o')
    plt.title(f"Number of Groups for n = 1 to {max_n}")
    plt.xlabel("n")
    plt.ylabel("Number of Groups")
    plt.grid(True)
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    response = {
        'max_n': max_n,
        'group_counts': group_counts,
        'all_groups': all_groups,
        'plot': plot_data
    }
    
    app.logger.info(f'Sending response for max_n={max_n}')
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)