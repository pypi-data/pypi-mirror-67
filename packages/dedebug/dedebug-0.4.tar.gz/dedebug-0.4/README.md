Library for sending telegram debug messages

### Install
```python
pip3 install dedebug
```

### How to use
```python
from dedebug import sendDebug

# variant 1
res = sendDebug(project_name='demo').message('Hello')

# variant 2
res = sendDebug(project_name='demo').message([1, 2, 3])
```