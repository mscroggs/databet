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

plt.figure(figsize=(6, 5))
for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    row = i // 5
    col = i % 5
    if row == 5:
        row = 4
        col = 5
    with open(f"letters/{letter}.json") as f:
        pts = np.array(json.load(f))

    if i % 2 == 0:
        plt.plot(col + pts[:, 0], 4 - row + pts[:, 1], "o", color="#2EA3D0", markersize=2)
    else:
        plt.plot(col + pts[:, 0], 4 - row + pts[:, 1], "o", color="#FFA366", markersize=2)
    plt.xlim([-0.05, 6.05])
    plt.ylim([-0.05, 5.05])
    plt.axis("equal")
plt.savefig("img/all.png", dpi=133)
plt.clf()
plt.close()
