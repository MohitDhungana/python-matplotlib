# %%
import matplotlib.pyplot as plt

plt.style.use("seaborn-whitegrid")
import numpy as np

# %%
# A simple scatter plot
x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x, y, "o", color="black")

# %%
# simple scatterplot using different plot labels
rng = np.random.RandomState(0)
for marker in ["o", ".", ",", "x", "+", "v", "^", "<", ">", "s", "d"]:
    plt.plot(rng.rand(5), rng.rand(5), marker, label=f"marker={marker}")

plt.legend(numpoints=1)
plt.xlim(0, 1.8)


# %%
# scatterplot using plt.scatter
plt.scatter(x, y, marker="o")

# %%
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap="viridis")
plt.colorbar()  # show color scale

# %%
from sklearn.datasets import load_iris

iris = load_iris()
features = iris.data.T
plt.scatter(
    features[0],
    features[1],
    alpha=0.2,
    s=100 * features[3],
    c=iris.target,
    cmap="viridis",
)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

# %%
print(iris.data.T)

# %%
