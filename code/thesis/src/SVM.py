'''
Created on Nov 30, 2012

@author: mandar
'''

from glimpse.glab import *
from glimpse.util import svm

class SVM(object):
    '''
    classdocs
    '''

    def __init__(self, training_images_path, testing_images_path):
        '''
        Constructor
        '''
        self.training_images_path = training_images_path
        self.testing_images_path = testing_images_path
        
        self.training_accuracy = None
        self.testing_accuracy = None
        self.testing_decision_values = None
        self.image_to_decision_value = {}
        self.experiment = SetExperiment()
        self.experiment.SetTrainTestSplitFromDirs(self.training_images_path, self.testing_images_path)
        
    def configure_svm(self, num_of_prototypes):
        self.num_of_prototypes = num_of_prototypes
        self.experiment.ImprintS2Prototypes(self.num_of_prototypes)
        
    def train(self):
        
        print "training the SVM ..."
        self.training_accuracy = self.experiment.TrainSvm()
        print "training accuracy: " + str(self.training_accuracy)
        
    def test(self):
        
        print "testing the SVM ..."
        test_features, test_labels = svm.PrepareFeatures(self.experiment.test_features)
        self.testing_decision_values = self.experiment.classifier.decision_function(test_features)
        
        self.testing_decision_values = self.testing_decision_values.tolist()
        for index in range(len(self.testing_decision_values)):
            self.image_to_decision_value[self.experiment.test_images[1][index]] = self.testing_decision_values[index][0]
        
        return self.image_to_decision_value
    
    def generate_image_decision_value_pairs(self):
        
        pass
        