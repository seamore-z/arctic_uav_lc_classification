#    Author: Ankit Kariryaa, University of Bremen

from tensorflow.keras.optimizers import Adam, Adadelta, Adagrad, Nadam

# Testing new approach because decay has been deprecated for tensorflow > 2.3

#adaDelta = Adadelta(learning_rate=lr_schedule)

# Optimezers; https://keras.io/optimizers/
adaDelta = Adadelta(learning_rate=1.0, rho=0.95, epsilon=None)
adam = Adam(learning_rate= 5.0e-05, beta_1= 0.9, beta_2= 0.999, epsilon= 1.0e-8)
nadam = Nadam(learning_rate=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, weight_decay=0.004)
adagrad = Adagrad(learning_rate=0.01, epsilon=None)
#adaDelta = Adadelta(lr=1.0, rho=0.95, epsilon=None)
#adam = Adam(lr= 5.0e-05, beta_1= 0.9, beta_2= 0.999, epsilon= 1.0e-8)
#nadam = Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=None, weight_decay=0.004)
#adagrad = Adagrad(lr=0.01, epsilon=None)
