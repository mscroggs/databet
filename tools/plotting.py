import matplotlib.pylab as plt
from .letters import load_letter

plt.rcParams["font.family"] = "Comfortaa"
plt.rcParams["axes.edgecolor"] = "#333333"
plt.rcParams["xtick.color"] = "#333333"
plt.rcParams["ytick.color"] = "#333333"


def plot_letter(letter, fname=None):
    pts = load_letter(letter)
    plt.figure(figsize=(5, 5))
    plt.plot(pts[:, 0], pts[:, 1], "o", color="#2EA3D0")
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    if fname is None:
        plt.show()
    else:
        plt.savefig(fname)
    plt.clf()
    plt.close()


def plot_word(word, fname=None):
    pass
