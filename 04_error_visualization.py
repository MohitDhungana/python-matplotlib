# %%
# %matplotlib inline
import matplotlib.pyplot as plt

plt.style.use("seaborn-whitegrid")
import numpy as np

# %%
# simple error bar
x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy + np.random.randn(50)

plt.errorbar(x, y, yerr=dy, fmt=".k")

# %%
# customized look of errorbar
plt.errorbar(x, y, yerr=dy, fmt="o", ecolor="lightgray", elinewidth=3, capsize=0)

# %%
# continuous errors
# from sklearn.gaussian_process import GaussianProcessRegressor

# # defind the model and draw some data
# model = lambda x: x * np.sin(x)
# xdata = np.array([1, 3, 5, 6, 8])
# ydata = model(xdata)

# # compute the Gaussian process fit
# gp = GaussianProcessRegressor(corr="cubic", theta0=1e-2, thetaU=1e-1, random_start=100)
# gp.fit(xdata[:, np.newaxis], ydata)

# xfit = np.linspace(0, 10, 1000)
# yfit, MSE = gp.predict(xfit[:, np.newaxis], eval_MSE=True)
# dyfit = 2 * np.sqrt(MSE)  # 2*sigma= 95% confidence region

# %%
# density and contour plots


def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contour(X, Y, Z, colors="black")

# %%
plt.contour(X, Y, Z, 20, cmap="RdGy")


# %%
plt.contourf(X, Y, Z, 20, cmap="RdGy")
plt.colorbar()

# %%
# show plot as img to improve effiency while displaying continuous contour area
plt.imshow(Z, extent=[0, 5, 0, 5], origin="lower", cmap="RdGy")
plt.colorbar()
plt.axis(aspect="image")
