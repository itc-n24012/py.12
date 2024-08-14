import math
import random

total = 0
num_a = 0
sim_pi = 0
while not math.isclose(sim_pi, math.pi, abs_tol=1e-5):
    c = random.random()
    d = random.random()
    L = pow(c**2 + d**2, 0.5)
    total += 1
    if L <= 1:
        num_a += 1
        sim_pi = 4 * num_a / total
print(sim_pi)
print(total)
