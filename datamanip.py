import pandas
import matplotlib.pyplot as plotter

dataset = pandas.read_csv('data4.txt', delimiter = ',', names = ['humidity', 'tempC', 'tempF', 'heatC', 'heatF', 'gasContent'])
# print(dataset['gasContent'])
indices = list()
for _ in dataset.iterrows():
	indices.append(_[0])

plotter.plot(indices, dataset['gasContent'], label = 'gasContent')
plotter.legend()
plotter.show()