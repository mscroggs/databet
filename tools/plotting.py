import matplotlib.pylab as plt

plt.rcParams["font.family"] = "Comfortaa"
plt.rcParams["axes.edgecolor"] = "#333333"
plt.rcParams["xtick.color"] = "#333333"
plt.rcParams["ytick.color"] = "#333333"


def plot_letter(data, fname=None):
    plt.figure(figsize=(5, 5))
    plt.plot(data[:, 0], data[:, 1], "o", color="#2EA3D0")
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    if fname is None:
        plt.show()
    else:
        plt.savefig(fname)
    plt.clf()
    plt.close()
