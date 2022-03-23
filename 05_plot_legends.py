# %%
import matplotlib.pyplot as plt

plt.style.use("classic")
import numpy as np

# %%
x = np.linspace(0, 10, 1000)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), "-b", label="Sine")
ax.plot(x, np.cos(x), "--r", label="Cosine")
ax.axis("equal")
leg = ax.legend()

# %%
ax.legend(loc="upper left", frameon=False)
fig

# %%
ax.legend(frameon=False, loc="lower center", ncol=2)
fig

# %%
ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
fig

# %%
# choosing elements for the legend
y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
lines = plt.plot(x, y)

# lines is a list of plt.Line2D instances
plt.legend(lines[:2], ["first", "second"])

# %%
plt.plot(x, y[:, 0], label="first")
plt.plot(x, y[:, 1], label="second")
plt.plot(x, y[:, 2:])
plt.legend(framealpha=1, frameon=True)

# %%
# legend for size of points
import pandas as pd

cities = pd.read_csv("data/california_cities.csv")
# Extract the data we're interested in
lat, lon = cities["latd"], cities["longd"]
population, area = cities["population_total"], cities["area_total_km2"]
# Scatter the points, using size and color but no label
plt.scatter(
    lon,
    lat,
    label=None,
    c=np.log10(population),
    cmap="viridis",
    s=area,
    linewidth=0,
    alpha=0.5,
)
plt.axis(aspect="equal")
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.colorbar(label="log$_{10}$(population)")
plt.clim(3, 7)
# Here we create a legend:
# we'll plot empty lists with the desired size and label
for area in [100, 300, 500]:
    plt.scatter([], [], c="k", alpha=0.3, s=area, label=str(area) + " km$^2$")
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title="City Area")
plt.title("California Cities: Area and Population")

# %%
# multiple legends
fig, ax = plt.subplots()
lines = []
styles = ["-", "--", "-.", ":"]
x = np.linspace(0, 10, 1000)
for i in range(4):
    lines += ax.plot(x, np.sin(x - i * np.pi / 2), styles[i], color="black")
ax.axis("equal")
# specify the lines and labels of the first legend
ax.legend(lines[:2], ["line A", "line B"], loc="upper right", frameon=False)
# Create the second legend and add the artist manually.
from matplotlib.legend import Legend

leg = Legend(ax, lines[2:], ["line C", "line D"], loc="lower right", frameon=False)
ax.add_artist(leg)

# %%
