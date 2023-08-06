# ChomboPy

This package contains tools for running, analysing, and plotting [Chombo](https://commons.lbl.gov/display/chombo/Chombo+-+Software+for+Adaptive+Solutions+of+Partial+Differential+Equations) simulations.

## Examples

### Inputs
Chombo input files can be read and written using some utility functions
```python
from chombopy.inputs import read_inputs, write_inputs
inputs = read_inputs('/path/to/inputs')

# inputs is a dictionary, with the key values converted to appropriate python objects:
print(inputs['main.num_cells']) # e.g. [16, 16, 16]
print(inputs['main.verbosity']) # e.g. 3
print(inputs['main.plt_prefix']) # e.g. 'plt'

# You can alter the values
inputs['main.verbosity'] = 0

# And write the file back out
write_inputs('/path/to/new_inputs', inputs)
```

### Plot files
Chombo plot files can be read using the PltFile class:
```python
from chombopy.plotting import PltFile
import matplotlib.pyplot as plt

pf = PltFile('/path/to/file.hdf5')
pf.load_data()

# Get data for the temperature variable on level 2
temperature = pf.get_level_data('Temperature', 2)

# temperature is an xarray.DataSet object, which can be plotted using matplotlib
x = temperature.coords['x']
y = temperature.coords['y']
plt.pcolormesh(x, y, temperature)

# Or you can do some analysis using the xarray/numpy functionality
print(temperature.mean())
```

## Documentation
Further documentation can be found [online](https://chombopy.readthedocs.io/en/latest/). To compile the documentation locally, get the code and setup a virtual environment:
```bash
$ git clone https://github.com/jrgparkinson/chombopy.git
$ cd chombopy
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python setup.py install
```
Then to build the documentation with Sphinx:
```bash
$ cd docs
$ make html
```

## Testing
Unit tests can be run in a similar way to building the documentation. Having got a copy of the code and setup a virtual environment, from the root directory (i.e. `/path/to/chombopy`), simply run the following from your virtual environment
```bash
$ python setup.py install
$ py.test
```
Code coverage will be published to `chombopy/docs/test/coverage.html`, and test results to `chombopy/docs/test/report.html`.
