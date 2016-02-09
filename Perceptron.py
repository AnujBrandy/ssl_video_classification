#perceptron 

#it is a weak classifier that helps in predicting about the weights needed to assign
#the input vectors .. basically it depends upon the feature vector values and the
#weights that are assigned to it depending upon the error that has come out of it

#and it has been seen that the errors gets stabilised after a certain number of 
#iterations

#initial weights assigned randomly

#let us make a percepteron for A or B or C

from random import choice
from numpy import array, dot, random
from pylab import plot, ylim

weights = random.rand( 4 )

errors = [ ]

learning_rate = 0.3

number_of_iterations = 80

one_step_rule = lambda t: 0 if t < 0 else 1

training_data = [
    (array([0,0,0,1]), 0),
    (array([0,0,1,1]), 1),
    (array([0,1,0,1]), 1),
    (array([0,1,1,1]), 1),
    (array([1,0,0,1]), 1),
    (array([1,0,1,1]), 1),
    (array([1,1,0,1]), 1),
    (array([1,1,1,1]), 1),

]

#perceptron code

for iteration in xrange( number_of_iterations ) :
	x_vector , expected_output = choice( training_data )
	predicted_output = dot( x_vector , weights )
	error = expected_output - one_step_rule( predicted_output )
	errors.append( error )
	weights = weights + learning_rate * error * x_vector

for x_vector, doesnt_matter  in training_data :
	predicted_output = dot( x_vector , weights ) 
	print str( x_vector[ :3 ] ) + " " + str( predicted_output ) + " " + str( one_step_rule( predicted_output ) )  


ylim( [ -1, 1 ] )
plot( errors )