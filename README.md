# Dexonline.ro API

A simple API that queries dexonline.ro, it returns the definitions of the words.

#

How to install, using pip install?

>pip install -i https://test.pypi.org/simple/ dexonlineBK

#

### Functionality
```python
from dexonlineBK import dexonlineBK as DO

definitions = DO.getWordDefinition("neexplicabil")

for defs in definitions:
	print(defs[0])
	print(defs[1] + "\n")
	
Out:
NEEXPLICÁBIL
adj. v. inexplicabil.

NEEXPLICABIL
adj. inexplicabil, neînțeles. (Un fapt ~.)

Neexplicabil
≠ explicabil
```
