# First TensorFlow program!
# Tutorial from https://www.datacamp.com/community/tutorials/tensorflow-tutorial?utm_source=adwords_ppc

import tensorflow as tf
import numpy as np
# Initialize Constants
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

# Multiply
result = tf.multiply(x1, x2)
 

# Initialize session and then close after running loop
with tf.Session() as sess:
    output = sess.run(result)
    print(output, "\n", "You did it! (again)")