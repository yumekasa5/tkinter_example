# How to build python script by cx_Freeze

1. install
```bash
pip install cx_Freeze
```

2. setup.py
```python
from cx_Freeze import setup, Executable

setup(
    name="YourAppName",
    version="1.0",
    description="Your application description",
    executables=[Executable("Main.py")],
)
```
3. build
```bash
python setup.py build
```