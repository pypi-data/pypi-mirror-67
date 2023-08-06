# PyLMD
Method of decomposing signal into Product Functions

# Examples
```python
>>> import numpy as np
>>> from PyLMD import LMD
>>> x = np.linspace(0, 100, 101)
>>> y = 2 / 3 * np.sin(x * 30) + 2 / 3 * np.sin(x * 17.5) + 4 / 5 * np.cos(x * 2)
>>> lmd = LMD()
>>> PFs, resdue = lmd.lmd(y)
>>> PFs.shape
(6, 101)
```