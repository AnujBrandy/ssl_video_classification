from __future__ import division
from numpy import *
from dataFile import reduced_matrix
from dataFile import unlabeled_instances
#AdaBoost Algorithm
#let us assume that training set is empty intially.

training_set = [ ]
n_training_set = 0 #n_training_set represents the length of the training set
weights = [] 

#code to simplify the three class of inputs as -1, 0 , +1
training_output = []
for i in xrange( 34 ) : 
    if unlabeled_instances[ i ][ 0 ] == 1 :
        training_output.append( -1 )
    if unlabeled_instances[ i ][ 1 ] == 1 :
        training_output.append( 0 )
    if unlabeled_instances[ i ][ 2 ] == 1 :
        training_output.append( 1 )

#in this loop we append the training output as -1 if the videos belong to the first 
#class, 0 if the video sample belong to the second class and +1 if they belong to the 
#third class
print training_output    
#code done ...

'''
In AdaBoost Algorithm the initial weights are assumed to be 1
for each of the element in the training_set.
And since we want it as a distribution, we normalize it by
dividing it with total sum of all the weights.

Also, AdaBoost algorithm builds a classifier on top of many 
weak classifiers so that finally we have a boosted 
classifier algorithm.

Remember in the AdaBoost Algorithm, the classifier with
accuracy less than 50 percent are given a negative values and 
with 50 percent accuracy a zero and more than fifty percent 
a positive value is assigned for the classifier. We are talking
about the weak classifiers here. 

RULES_CLASSIFIERS is the variable that holds the function that is 
the various weak classifiers in it.

ALPHA_CLASSIFIERS is the variable that is gonna store the score
for each of the weak classifiers.
'''

# changes in the adaboost algorithm for the multiclass classifier
# paper suggests that there will be two terms added .. 
# one in the log to add log k -1  
# this term is not understood
# and the other to check if the error increases above by a ceratin threshold
# then we have to ignore that weak classifier, which is quite acceptable 

def rule_classifier( func_classifier ) :
    k = 3
    # one can change the number of classes of videos here ..
    global weights
    errors_classifier = [ ]
    
    for training_example in training_set :
    
        if training_example[ 9 ] != func_classifier( training_example ) :
            errors_classifier.append( 1 )
        else :
            errors_classifier.append( 0 )

    e_classifier = 0.000001
    for i in xrange( n_training_set ) :
        e_classifier = e_classifier + errors_classifier[ i ] * weights[ i ]  

    log_value_classifier = log( ( 1 - e_classifier ) / e_classifier ) + log( k - 1 )
    # the term to the log has been added ..
    # 
    
    alpha_classifier = 0.5 * log_value_classifier

    w_classifier = []

    for i in xrange( n_training_set ) :
        w_classifier.append( 0 )

    for i in xrange( n_training_set ) :
        if errors_classifier[ i ] == 1 :
            w_classifier[ i ] = weights[ i ] * exp( alpha_classifier )
        else :
            w_classifier[ i ] = weights[ i ] * exp( -alpha_classifier )
        
    weights = w_classifier / sum( w_classifier )
        
    RULES_CLASSIFIERS.append( func_classifier )
    ALPHA_CLASSIFIERS.append( alpha_classifier )
        

def evaluating_classifiers( ) :

    n_classifiers = len( RULES_CLASSIFIERS )

    for training_example in training_set :

        final_adaboost_classifier = [ ALPHA_CLASSIFIERS[ i ] * RULES_CLASSIFIERS[ i ]( training_example ) for i in xrange( n_classifiers ) ]
        print x_parameter, sign( check ) == sign( sum( final_adaboost_classifier ) )



'''

---------- OUR DATA SET IS INJECTED ----------
need to figure out a final to way to understand how the output is gonna come
WAY :
arg max k sum m=1 α(m) · I(T(m)(x) = k).

'''



RULES_CLASSIFIERS = [] 
ALPHA_CLASSIFIERS = []

if __name__ == '__main__' :
    training_examples = []

    #fitting our data into the code

    for i in xrange( 34 ) :
        training_examples.append( reduced_matrix[ i ] )
        training_examples[ i ].append( training_output[ i ] )

    for i in xrange( 34 ) :
        print training_examples[ i ]

    # training_examples.append(((1,  2  ), 1))
    # training_examples.append(((1,  4  ), 1))
    # training_examples.append(((2.5,5.5), 1))
    # training_examples.append(((3.5,6.5), 1))
    # training_examples.append(((4,  5.4), 1))
    # training_examples.append(((2,  1  ),-1))
    # training_examples.append(((2,  4  ),-1))
    # training_examples.append(((3.5,3.5),-1))
    # training_examples.append(((5,  2  ),-1))
    # training_examples.append(((5,  5.5),-1))
    training_set = training_examples

    n_training_set = len( training_set )
    print n_training_set
    for i in xrange( n_training_set ) :
        weights.append( 1 / n_training_set )
    training_set = training_examples
    
    # rule_classifier(lambda x: 2*(x[0] < 1.5)-1)
    # rule_classifier(lambda x: 2*(x[0] < 4.5)-1)
    # rule_classifier(lambda x: 2*(x[1] > 5)-1)
    # evaluating_classifiers( )
    
