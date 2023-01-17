import json
import numpy as np
import os
from tools.plotting import plot_letter

if not os.path.isdir("pngs"):
    os.system("mkdir pngs")

for letter in "0ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    with open(f"letters/{letter}.json") as f:
        plot_letter(np.array(json.load(f)), f"pngs/{letter}.png")
