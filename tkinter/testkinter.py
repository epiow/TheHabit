import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

def generate_fake_data(start_date, end_date):
    """
    Generate fake data for the heatmap.
    """
    date_range = end_date - start_date
    num_days = date_range.days + 1
    data = np.random.rand(num_days)  # Generate random values
    num_weeks = num_days // 7
    data = data[:num_weeks*7]  # Trim excess days
    return data.reshape(num_weeks, 7)  # Reshape into weeks

def plot_calendar_heatmap(data, start_date):
    """
    Plot a calendar heatmap.
    """
    fig, ax = plt.subplots()
    cmap = plt.cm.Greens  # Choose colormap
    ax.imshow(data, cmap=cmap, aspect='auto', alpha=0.5)

    # Customize ticks and labels
    num_weeks, num_days = data.shape
    ax.set_xticks(np.arange(num_days))
    ax.set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    ax.set_yticks(np.arange(num_weeks))
    ax.set_yticklabels([start_date.strftime("%b %d")] + [(start_date + timedelta(days=7 * i)).strftime("%b %d") for i in range(1, num_weeks)])

    plt.show()

# Define start and end date
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

# Generate fake data
data = generate_fake_data(start_date, end_date)

# Plot calendar heatmap
plot_calendar_heatmap(data, start_date)
