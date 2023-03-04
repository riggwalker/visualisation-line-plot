import pandas as np
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'United Kingdom', 'Germany']
sales_2017 = [199826, 777000, 54479, 13597, 54470]
sales_2018 = [361307, 1256000, 56000, 15474, 67504]
sales_2019 = [329528, 1204000, 72000, 37850, 108431]
sales_2020 = [295313, 1367000, 68000, 108205, 194163]

# Create the line plot
plt.plot(countries, sales_2017, label='2017')
plt.plot(countries, sales_2018, label='2018')
plt.plot(countries, sales_2019, label='2019')
plt.plot(countries, sales_2020, label='2020')

# Add labels and title
plt.xlabel('Country')
plt.ylabel('EV Sales')
plt.title('Sales of Electric Vehicles in Developed Countries (2017-2020)')

# Add legend
plt.legend()

# Show the plot
plt.show()


