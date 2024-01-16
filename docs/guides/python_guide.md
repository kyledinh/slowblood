## Restart the kernel in Python Notebook

```
import IPython

IPython.Application.instance().kernel.do_shutdown(True)

## In Jupyter notebook
%reset -f
```

## Reimport a module/package

```
import importlib
importlib.reload(slowblood)
print("version: ", slowblood.lib_settings.VERSION)

%pip freeze | grep slowblood
```

## Notebook Import a local version of module/package

```
# %pip install -q -U slowblood
## IMPORTING THE UPLOADED module from pypi/src/slowblood to /workspace/slowblood
import os
os.chdir(os.path.expanduser("/workspace"))
import slowblood
print("Loaded local VERSION: ", slowblood.lib_settings.VERSION)
```