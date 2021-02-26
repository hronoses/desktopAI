import keys as k
import numpy as np
import time


mouse = k.Mouse()

time.sleep(2)
mouse.lb_press()
for t in range(300):
    alpha = 0.01
    A = 15 * np.exp(-t * alpha)
    w = 0.1
    x = int(round(A * np.cos(w * t)))
    y = int(round(A * np.sin(w * t)))
    mouse.move(x, y)
    time.sleep(0.01)

mouse.lb_release()







