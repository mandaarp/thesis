'''
Created on Nov 30, 2012

@author: mandar
'''

import Constants as value
import SVM as svm
import os

class DirectionEstimator(object):
    '''
    classdocs
    '''

    def __init__(self, training_images_path, testing_images_path):
        '''
        Constructor
        '''
        self.training_images_path = training_images_path
        self.testing_images_path = testing_images_path
        
        self.svm_person_left = None
        self.svm_person_right = None
        self.svm_person_back = None
        self.svm_person_forward = None
        
    def generate_svm(self, testing_images_path=None):
        
        print "generating SVMs - one for each direction ..."
        
        if testing_images_path is None:
            
            print "in validation mode ..."
            
            print "generating " + value.STR_PERSON_BACK + " SVM ..."
            self.svm_person_back = svm.SVM(os.path.join(self.training_images_path, value.STR_PERSON_BACK), 
                                       os.path.join(self.testing_images_path, value.STR_PERSON_BACK))
        
            print "generating " + value.STR_PERSON_FORWARD + " SVM ..."
            self.svm_person_forward = svm.SVM(os.path.join(self.training_images_path, value.STR_PERSON_FORWARD),
                                              os.path.join(self.testing_images_path, value.STR_PERSON_FORWARD))
            
            print "generating " + value.STR_PERSON_LEFT + " SVM ..."
            self.svm_person_left = svm.SVM(os.path.join(self.training_images_path, value.STR_PERSON_LEFT),
                                           os.path.join(self.testing_images_path, value.STR_PERSON_LEFT))
            
            print "generating " + value.STR_PERSON_RIGHT + " SVM ..."
            self.svm_person_right = svm.SVM(os.path.join(self.training_images_path, value.STR_PERSON_RIGHT),
                                            os.path.join(self.testing_images_path, value.STR_PERSON_RIGHT))
        
        else:
            
            print "in test mode ..."
            
            print "generating " + value.STR_PERSON_BACK + " SVM ..."
            self.svm_person_back = svm.SVM(os.path.join(self.training_images_path, value.STR_PERSON_BACK), 
                                           os.path.join(testing_images_path, value.STR_PERSON_BACK))
        
            print "generating " + value.STR_PERSON_FORWARD + " SVM ..."
            self.svm_person_forward = svm.SVM(os.path.join(self.training_images_path, value.STR_PERSON_FORWARD),
                                              os.path.join(testing_images_path, value.STR_PERSON_FORWARD))
            
            print "generating " + value.STR_PERSON_LEFT + " SVM ..."
            self.svm_person_left = svm.SVM(os.path.join(self.training_images_path, value.STR_PERSON_LEFT),
                                           os.path.join(testing_images_path, value.STR_PERSON_LEFT))
            
            print "generating " + value.STR_PERSON_RIGHT + " SVM ..."
            self.svm_person_right = svm.SVM(os.path.join(self.training_images_path, value.STR_PERSON_RIGHT),
                                            os.path.join(testing_images_path, value.STR_PERSON_RIGHT))
        
    def imprint_s2_prototypes(self, num_of_prototypes):
        
        print "imprinting S2 prototypes for each SVM ..."
        
        print "imprinting " + str(num_of_prototypes) + " S2 prototypes for " + value.STR_PERSON_BACK + " SVM ..."
        self.svm_person_back.configure_svm(num_of_prototypes)
        
        print "imprinting " + str(num_of_prototypes) + " S2 prototypes for " + value.STR_PERSON_FORWARD + " SVM ..."
        self.svm_person_forward.configure_svm(num_of_prototypes)
        
        print "imprinting " + str(num_of_prototypes) + " S2 prototypes for " + value.STR_PERSON_LEFT + " SVM ..."
        self.svm_person_left.configure_svm(num_of_prototypes)
        
        print "imprinting " + str(num_of_prototypes) + " S2 prototypes for " + value.STR_PERSON_RIGHT + " SVM ..."
        self.svm_person_right.configure_svm(num_of_prototypes)
        
    def train(self):
        
        print "training each SVM ..."
        
        print "training " + value.STR_PERSON_BACK + " SVM ..."
        self.svm_person_back.train()
        
        print "training " + value.STR_PERSON_FORWARD + " SVM ..."
        self.svm_person_forward.train()
        
        print "training " + value.STR_PERSON_LEFT + " SVM ..."
        self.svm_person_left.train()
        
        print "training " + value.STR_PERSON_RIGHT + " SVM ..."
        self.svm_person_right.train()
    
    def validate(self):
        
        print "validating each SVM ..."
        
        print "validating " + value.STR_PERSON_BACK + "SVM ..."
        self.svm_person_back.test()
        
        print "validating " + value.STR_PERSON_FORWARD + "SVM ..."
        self.svm_person_forward.test()
        
        print "validating " + value.STR_PERSON_LEFT + "SVM ..."
        self.svm_person_left.test()
        
        print "validating " + value.STR_PERSON_RIGHT + "SVM ..."
        self.svm_person_right.test()
    
    def test(self):
        
        print "testing each SVM ..."
        
        print "running " + value.STR_PERSON_BACK + "SVM on test images ..."
        self.svm_person_back.test()
        
        print "running " + value.STR_PERSON_FORWARD + "SVM on test images ..."
        self.svm_person_forward.test()
        
        print "running " + value.STR_PERSON_LEFT + "SVM on test images ..."
        self.svm_person_left.test()
        
        print "running " + value.STR_PERSON_RIGHT + "SVM on test images ..."
        self.svm_person_right.test()
    
    def print_decision_values(self):
        
        print "printing image-to-decision-values ..."
        
        print "image-to-decision-values for SVM: " + value.STR_PERSON_BACK
        print self.svm_person_back.image_to_decision_value
        
        print "image-to-decision-values for SVM: " + value.STR_PERSON_FORWARD
        print self.svm_person_forward.testing_decision_values

        print "image-to-decision-values for SVM: " + value.STR_PERSON_LEFT
        print self.svm_person_left.testing_decision_values
        
        print "image-to-decision-values for SVM: " + value.STR_PERSON_RIGHT
        print self.svm_person_right.testing_decision_values
        
    def dump_experiments(self, file_path):
        
        print "dumping experiments at " + file_path + " ..."
        self.svm_person_back.experiment.Store(os.path.join(file_path, value.STR_PERSON_BACK))
        self.svm_person_forward.experiment.Store(os.path.join(file_path, value.STR_PERSON_FORWARD))
        self.svm_person_left.experiment.Store(os.path.join(file_path, value.STR_PERSON_LEFT))
        self.svm_person_right.experiment.Store(os.path.join(file_path, value.STR_PERSON_RIGHT))
        
    def generate_decision_data(self):
        pass