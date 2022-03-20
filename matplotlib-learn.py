# %%
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-whitegrid")

# %%
fig = plt.figure()
x = np.linspace(0, 10, 1000)

# plot data to plt
plt.plot(x, np.sin(x), "-", color="red")
plt.plot(x, np.cos(x), "--")

# give X and Y axes limit
plt.xlim(-1, 12)
plt.ylim(-1.5, 1.5)

# save image to local file
# * fig.savefig("my_figure.png")
plt.show()

# %%
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 11)


plt.plot(x, x + 1, "-", color="red")
plt.plot(x, x**2, "--")


fig.savefig("my_figure.png")
plt.show()

# %%
plt.figure()
plt.subplot(2, 1, 2)
plt.plot(x, np.sin(x))

plt.subplot(2, 1, 1)
plt.plot(x, np.cos(x))
# %%
print("fig", fig)
print("ax", ax)
