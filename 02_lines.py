# %%
from cProfile import label
from turtle import color
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


plt.style.use("seaborn-whitegrid")

# %%
# adjusting line colors and styles
fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
# ax.plot(x, np.sin(x))
plt.plot(x, np.sin(x))

# %%
plt.plot(x, np.sin(x - 0), color="blue")
plt.plot(x, np.sin(x - 1), color="g")
plt.plot(x, np.sin(x - 2), color="0.75")
plt.plot(x, np.sin(x - 3), color="#FFDD44")
plt.plot(x, np.sin(x - 4), color=(1.0, 0.2, 0.3))
plt.plot(x, np.sin(x - 5), color="chartreuse")

# %%
# For short, you can use the following codes:
plt.plot(x, x + 4, linestyle="-")  # solid
plt.plot(x, x + 5, linestyle="--")  # dashed
plt.plot(x, x + 6, linestyle="-.")  # dashdot
plt.plot(x, x + 7, linestyle=":")  # dotted

# %%
# labelling plots
plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)")

# %%
# adding legend to plots
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")
plt.title("A Sine Curve")
plt.legend()

# %%
