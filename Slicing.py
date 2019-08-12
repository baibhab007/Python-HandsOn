####
Try it Out - Slicing
Create a array x of shape (2, 3, 5), having first 30 natural numbers.

Create a boolean array b of shape (2,), having elements True, False.

Try the following expressions

x[b]

x[b,:,1:3]
####

import numpy as np
x = np.arange(1,31).reshape(2,3,5)
b = np.array([True,False]).reshape(2,)
print(x[b])
print(x[b,:,1:3])
