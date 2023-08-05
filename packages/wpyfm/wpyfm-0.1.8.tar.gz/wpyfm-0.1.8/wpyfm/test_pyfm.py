import numpy as np
import pyfm

print("A")
m = pyfm.PyFM("als", [1,1,8])
print("B")
t = pyfm.Data(np.eye(3), np.ones(3), has_xt=True)
t2 = pyfm.Data(np.ones((2, 3)), np.ones(2), has_xt=True)
print("C")
m.train(t)

print("D")
print(m.predict(t2))
print("EEEE")
