# LTPlugins - Lite plugins for simple Python 3 projects

## Installation
```shell script
pip install ltplugins
```

## Usage examples
Imagine there is a directory **plugins** with two scripts: **ltp_example.py** and **ltp_test.py**
For simplicity they contain a single **main** function:

```python
def main(*args, **kwargs):
    print(args, kwargs)
```

LTPlugins could dynamically load them and unload during the runtime of the main script:

```python
import ltplugins

p = ltplugins.LTPlugins(prefix='ltp_', path='plugins')
p.load('example')
p.load('test')
p.list(state='a', status=True)
p.name['example'].main('123', a=456)
p.run('test', 'main', '789', a=123)
p.unload('test')
p.reload('example')
```

## Changelog

| Date       | Version  | Remarks                                    |
| ---------- | -------- | ------------------------------------------ |
| 2020.04.29 | v1.0.0   | Initial release                            |
| 2020.04.29 | v1.0.1   | setup.py fix for README.md                 |
| 2020.05.01 | v1.1.0   | List modules: all, loaded and unloaded     |
| 2020.05.01 | v1.1.1   | Readme update                              |
| 2020.05.07 | v1.1.2   | Default status='a' in LTPlugins.list()     |
| 2020.05.07 | v1.1.3   | LTPlugins.list() now returns module names  |
| 2020.05.07 | v1.1.4   | LTPlugins.list(state='a', status=False)    |
| 2020.05.07 | v1.1.4.1 | fnmatch module reference removed           |
| 2020.05.07 | v1.1.5   | Dummy release to make PyPI happy           |

On any issues, questions and suggestions contact me: Mikhail Zakharov <zmey20000@yahoo.com> 
