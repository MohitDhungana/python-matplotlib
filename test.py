# %%
import seaborn as sns
import numpy as np
import math

from matplotlib import pyplot as plt

iris = sns.load_dataset("iris")
iris.head()

# %%


sns.set()
sns.pairplot(iris, hue="species", size=1.5)

# %%
t = np.linspace(0, 2 * math.pi, 800)
a = np.sin(t)
plt.figure(figsize=(9, 6), dpi=75)
plt.plot(t, a, "r")
plt.show()
