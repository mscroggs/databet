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
    plt.figure(figsize=(0.4 + 4 * len(word), 4.4))
    for i, letter in enumerate(word):
        pts = load_letter(letter)
        plt.plot(i + pts[:, 0], pts[:, 1], "o", color="#2EA3D0")
    plt.xlim([-0.05, len(word) + 0.05])
    plt.ylim([-0.05, 1.05])
    plt.axis("off")
    plt.gca().set_position((0, 0, 1, 1))
    if fname is None:
        plt.show()
    else:
        plt.savefig(fname)
    plt.clf()
    plt.close()
