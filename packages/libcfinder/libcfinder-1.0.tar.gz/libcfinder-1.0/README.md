# libcfinder

Libcfinder is a tool for finding the libc version used when compiling an executable.

## Installation

Use the package manager pip to install libcfinder

```bash
pip install libcfinder
```

## Usage

```python
import libcfinder

libcv = find_libcv({"puts": 0xf7d8fb40, "gets": 0xf7d8f2b0})
system_addr = find_fun_addr(libcv[0], "puts", 4158511936, "system")
```