from glimpse.glab import *
from glimpse.models.ml import Model
from glimpse.pools import MulticorePool

SetTrainTestSplitFromDirs('train','test')

ImprintS2Prototypes(200)
train_acc, test_acc = RunSvm()

print("Training accuracy: " + str(train_acc) + "\nTesting accuracy: " + str(test_acc))

StoreExperiment('experiment_train75_test25_n200.dat')
