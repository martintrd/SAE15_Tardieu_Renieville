import matplotlib.pyplot as plt

data = [49, 20, 37, 28, 20]
jours = ["", "15/02/2016", "", "28/05/2016", ""]

plt.plot(data)  #1 seul argument: 'data'
plt.xticks(range(len(data)), jours, rotation=0)
plt.show()

