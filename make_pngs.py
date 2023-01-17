import json
import matplotlib.pylab as plt
import numpy as np
import os

if not os.path.isdir("pngs"):
    os.system("mkdir pngs")

plt.rcParams["font.family"] = "Comfortaa"
plt.rcParams["axes.edgecolor"] = "#333333"
plt.rcParams["xtick.color"] = "#333333"
plt.rcParams["ytick.color"] = "#333333"


def make_png(data, fname):
    plt.figure(figsize=(5, 5))
    plt.plot(data[:, 0], data[:, 1], "o", color="#2EA3D0")
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.savefig(fname)
    plt.clf()
    plt.close()


for letter in "0ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    with open(f"letters/{letter}.json") as f:
        make_png(np.array(json.load(f)), f"pngs/{letter}.png")
