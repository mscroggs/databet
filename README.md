# The databet
![The alphabet](img/all.png)

This repo contains 27 datasets: 26 of these resemble the letters of the alphabet, the 27th is a star:

![The starting dataset](img/star.png)

For each of the datasets (to 2 decimal places):

- The mean of the x-values is 0.50
- The mean of the y-values is 0.52
- The standard deviation of the x-values is 0.17
- The standard deviation of the y-values is 0.18
- The correlation coefficient is 0.16

The dataset for each letter of the alphabet can be found in JSON format in the [letters](letters) folder.

You can read more about these datasets at [mscroggs.co.uk/blog/101](https://mscroggs.co.uk/blog/101).

## Databet Python package
### Installing with pip
If you want to experiment with these datasets using Python, you can install the databet package
by running:

```bash
pip install databet
```

Alternatively, you can install databet directly from this repo by running:

```bash
pip install git+https://github.com/mscroggs/databet
```

### Using the databet package
Once you've installed the databet Python package, 
you can load a letter or create a plot of a letter using the `load_letter` and `plot_letter`
functions:

```python
import databet

a = databet.load_letter("A")

databet.plot_letter("B", "b.png")
```

You can also plot words using the `plot_word` function:

```python
import databet

databet.plot_word("DATABET", "databet.png")
```
