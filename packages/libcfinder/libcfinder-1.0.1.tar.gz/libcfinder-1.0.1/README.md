# libcfinder

Libcfinder is a pwn tool made for finding the libc version that was used when compiling an executable.

## Installation

Use the package manager pip to install libcfinder

```bash
pip3 install libcfinder
```

## Usage

```python
import libcfinder

libcv = find_libcv({"puts": 0xf7d8fb40, "gets": 0xf7d8f2b0})
system_addr = find_fun_addr(libcv[0], "puts", 0xf7dddb40, "system")
```