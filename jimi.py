import matplotlib.pyplot as plt
import numpy as np

n = 10000000
g = 9.8
obs = [[56, 66], [110, 120], [26, 36], [172, 182]]
v = np.random.uniform(35.0,45.0,n)
theta = np.random.uniform(0, np.pi/2.0, n)
ans = [v]

for o in obs:
    d = v**2*np.sin(2*theta)/g
    temp = (d>=o[0]) & (d<=o[1])
    v = v[temp]
    v = np.random.choice(v,n)
    ans.append(v)

plt.figure()
i = 0
for v in ans:
    i += 1
    plt.hist(v, normed=True, label="{}".format(i))
plt.legend()
plt.savefig("jimi.pdf")
