'''
Created on Nov 30, 2012

@author: mandar
'''
from SVM import *

TRAIN_PERSON_BACK = '/home/mandar/thesis/demo/images/train/person-back'
TRAIN_PERSON_FORWARD = '/home/mandar/thesis/demo/images/train/person-forward'
TRAIN_PERSON_LEFT = '/home/mandar/thesis/demo/images/train/person-left'
TRAIN_PERSON_RIGHT = '/home/mandar/thesis/demo/images/train/person-right'

TEST_PERSON_BACK = '/home/mandar/thesis/demo/images/test/person-back'
TEST_PERSON_FORWARD = '/home/mandar/thesis/demo/images/test/person-forward'
TEST_PERSON_LEFT = '/home/mandar/thesis/demo/images/test/person-left'
TEST_PERSON_RIGHT = '/home/mandar/thesis/demo/images/test/person-right'

NUM_OF_PROTOTYPES = 200

if __name__ == '__main__':
    
    svm_back = SVM(TRAIN_PERSON_BACK, TEST_PERSON_BACK)
    
    svm_back.configure_svm(NUM_OF_PROTOTYPES)
    
    svm_back.train()
    
    decision_values = svm_back.test()
    
    print decision_values