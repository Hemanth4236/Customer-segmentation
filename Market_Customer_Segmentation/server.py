from flask import Flask, render_template_string
import pandas as pd
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Customer Segmentation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 10px;
        }
        h2 {
            color: #555;
            margin-top: 30px;
        }
        img {
            max-width: 100%;
            border-radius: 4px;
            margin: 20px 0;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .warning {
            background-color: #fff3cd;
            color: #856404;
            padding: 15px;
            border-radius: 4px;
            margin: 20px 0;
            border-left: 4px solid #ffc107;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Customer Segmentation Dashboard</h1>
        
        <h2>Cluster Visualization</h2>
        {% if plot_exists %}
            <img src="/plot" alt="Cluster Plot">
        {% else %}
            <div class="warning">⚠️ Cluster plot not found. Run main.py first.</div>
        {% endif %}
        
        <h2>Customer Segments Data</h2>
        {% if data_exists %}
            <table>
                <tr>
                    <th>Customer ID</th>
                    <th>Recency</th>
                    <th>Frequency</th>
                    <th>Monetary</th>
                    <th>Cluster</th>
                </tr>
                {% for idx, row in data.iterrows() %}
                <tr>
                    <td>{{ idx }}</td>
                    <td>{{ "%.2f"|format(row['Recency']) }}</td>
                    <td>{{ "%.2f"|format(row['Frequency']) }}</td>
                    <td>{{ "%.2f"|format(row['Monetary']) }}</td>
                    <td><strong>{{ row['Cluster'] }}</strong></td>
                </tr>
                {% endfor %}
            </table>
        {% else %}
            <div class="warning">⚠️ Data file not found. Run main.py first.</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    plot_exists = os.path.exists("outputs/cluster_plot.png")
    data_exists = os.path.exists("outputs/customer_segments.csv")
    data = None
    
    if data_exists:
        data = pd.read_csv("outputs/customer_segments.csv")
    
    return render_template_string(HTML_TEMPLATE, plot_exists=plot_exists, data_exists=data_exists, data=data)

@app.route('/plot')
def plot():
    return open("outputs/cluster_plot.png", 'rb').read(), 200, {'Content-Type': 'image/png'}

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=8000)
