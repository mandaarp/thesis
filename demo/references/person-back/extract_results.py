from glimpse.glab import *

exp = LoadExperiment('experiment_train75_test25_n200.dat')

f = open('results.csv','w')

for i in range(len(exp.test_images)):
	for j in range(len(exp.test_images[i])):
		f.write(exp.test_images[i][j] + ',' + str(exp.test_results['predicted_labels'][i+j]) + '\n')

f.close()

