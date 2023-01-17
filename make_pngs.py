import os
from tools.plotting import plot_letter

if not os.path.isdir("pngs"):
    os.system("mkdir pngs")

for letter in "0ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    plot_letter(letter, f"pngs/{letter}.png")
