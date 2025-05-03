import plotly.graph_objects as go
import numpy as np

# Data
X = np.array([0.5, 2.0, 1.0])
Y = np.array([0, 1, 0])

# Color map: 0 -> bright red, 1 -> bright green
colors = ['#ff4c4c' if y == 0 else '#00cc96' for y in Y]

# Create scatter plot
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=X,
    y=Y,
    mode='markers',
    marker=dict(
        size=18,
        color=colors,
        line=dict(width=2, color='black'),
        symbol='circle'
    ),
    text=[f"x: {x}, y: {y}" for x, y in zip(X, Y)],
    hoverinfo='text'
))

# Aesthetic layout
fig.update_layout(
    title='Logistic Regression Data Points',
    xaxis_title='Feature x',
    yaxis_title='Label y',
    xaxis=dict(range=[0, 2.5], gridcolor='lightgray'),
    yaxis=dict(range=[-0.2, 1.2], tickmode='array', tickvals=[0, 1], gridcolor='lightgray'),
    plot_bgcolor='white',
    font=dict(family="Arial", size=16),
    height=500,
    width=700
)

# Use this instead of fig.show()
fig.write_html("/tmp/logistic_plot.html", auto_open=True)
