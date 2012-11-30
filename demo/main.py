import sys
import os
from glimpse.glab import *

TRAIN_PERSON_BACK = '/home/mandar/thesis/demo/images/train/person-back'
TRAIN_PERSON_FORWARD = '/home/mandar/thesis/demo/images/train/person-forward'
TRAIN_PERSON_LEFT = '/home/mandar/thesis/demo/images/train/person-left'
TRAIN_PERSON_RIGHT = '/home/mandar/thesis/demo/images/train/person-right'

TEST_PERSON_BACK = '/home/mandar/thesis/demo/images/test/person-back'
TEST_PERSON_FORWARD = '/home/mandar/thesis/demo/images/test/person-forward'
TEST_PERSON_LEFT = '/home/mandar/thesis/demo/images/test/person-left'
TEST_PERSON_RIGHT = '/home/mandar/thesis/demo/images/test/person-right'

NUM_OF_PROTOTYPES = 200

print "setting train and test directory paths for person-back ..."
SetTrainTestSplitFromDirs(TRAIN_PERSON_BACK, TEST_PERSON_BACK)
print "imprinting " + str(NUM_OF_PROTOTYPES) + " S2 prototypes for person-back ..."
ImprintS2Prototypes(NUM_OF_PROTOTYPES)
print "running SVM for person-back ..."
(train_acc, test_acc) = RunSvm()
print "SVM results"
print "training accuracy: " + str(train_acc)
print "testing accuracy: " + str(test_acc)
StoreExperiment('experiment_train75_test25_n200_person-back.dat')
'''
SetTrainTestSplitFromDirs(TRAIN_PERSON_FORWARD, TEST_PERSON_FORWARD)
ImprintS2Prototypes(NUM_OF_PROTOTYPES)
(train_acc, test_acc) = RunSvm()
print "SVM: Person-Forward"
print "training accuracy: " + train_acc
print "testing accuracy: " + test_acc
StoreExperiment('experiment_train75_test25_n200_person-forward.dat')

SetTrainTestSplitFromDirs(TRAIN_PERSON_LEFT, TEST_PERSON_LEFT)
ImprintS2Prototypes(NUM_OF_PROTOTYPES)
(train_acc, test_acc) = RunSvm()
print "SVM: Person-Left"
print "training accuracy: " + train_acc
print "testing accuracy: " + test_acc
StoreExperiment('experiment_train75_test25_n200_person-left.dat')

SetTrainTestSplitFromDirs(TRAIN_PERSON_RIGHT, TEST_PERSON_RIGHT)
ImprintS2Prototypes(NUM_OF_PROTOTYPES)
(train_acc, test_acc) = RunSvm()
print "SVM: Person-Right"
print "training accuracy: " + train_acc
print "testing accuracy: " + test_acc
StoreExperiment('experiment_train75_test25_n200_person-right.dat')
'''


