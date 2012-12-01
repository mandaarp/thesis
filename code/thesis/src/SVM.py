'''
Created on Nov 30, 2012

@author: mandar
'''

from glimpse.glab import *

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
        SetTrainTestSplitFromDirs(self.training_images_path, self.testing_images_path)
        self.experiment = GetExperiment()
        
    def configure_svm(self, num_of_prototypes):
        self.num_of_prototypes = num_of_prototypes
        ImprintS2Prototypes(self.num_of_prototypes)
        
    def train(self):
        
        print "training the SVM ..."
        self.training_accuracy = self.experiment.TrainSvm()
        print "training accuracy: " + str(self.training_accuracy)
        
    def test(self):
        
        print "testing the SVM ..."
        self.testing_accuracy = self.experiment.TestSvm()
        self.testing_decision_values = self.experiment.test_results['decision_values']
        print "testing accuracy: " + str(self.testing_accuracy)
        
        return self.testing_decision_values
    
    def generate_image_decision_value_pairs(self):
        
        pass
        