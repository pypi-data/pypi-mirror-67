auto_self_params
----------------

A python package to automatically assign parameters to self. This enables
replacing code such as:

```python
class A:
    """ Typical Code. """
    def __init__(self, param1, param2, kwparam1=0, kwparam2=0):
        """ Create Example Class."""
        self.param1 = param1
        self.param2 = param2
        self.kwparam1 = kwparam1
        self.kwparam2 = kwparam2
        # etc.
```

With code more like:

```python
from auto_self_params import auto_self_params

class A:
    """ Revised Code. """
    def __init__(self, param1, param2, kwparam1=0, kwparam2=0):
        """ Create Example Class."""
        auto_self_params.auto_self_params(locals())  # Assign all parameters to self
        # etc.
```

**Only** use this package if you need the paramters passed to `__init__` to
produce matching names in self when called.

You can, _however_, create a dictionary with locals and remove unwanted
paramters before passing it to `auto_self_params` so as to exclude unwanted
parameters.

If you would like to use the:
 `def __init__(self, *args, **kwargs):`
format then you may wish to use a pattern such as:

```python
from auto_self_params import auto_self_params

class A:
    """ Revised Code. """
    def __init__(self,  *args, **kwargs):
        """ Create Example Class."""
        param_dict = {'self': self, 'args': args, **kwargs}
        auto_self_params.auto_self_params(param_dict)  # Assign parameters to self
        # etc.
```

