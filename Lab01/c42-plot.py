import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#1. Prepare data
labels = ['Web', 'Android', 'iOS', 'React Native']
values = [40, 25, 20, 15]
colors = ['green', 'blue', 'orange', 'gold']
explode = [0, 0, 0, 0.2]

#2. Plot
plt.pie(values, labels = labels, explode = explode, colors = colors)
plt.axis('equal')

#3. Show
plt.show()