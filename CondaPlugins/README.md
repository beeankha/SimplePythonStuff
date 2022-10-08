# `conda` Subcommand Plugin Examples!

## C Plugins

From the top-level directory (_i.e._, `CondaPlugins/c_plugins/[plugin]`), run:

```
$ cc -fPIC -shared -o [program_name].so [program_name].c
```

... in order to create a shared library file (with the `.so` extension) using the C compiler. For example, in the `temp_converter` example, you would run:

```
$ cc -fPIC -shared -o c_to_f.so c_to_f.c
```

In the Python portion of the plugin (_i.e._, `CondaPlugins/c_plugins/temp_converter/temp_conv_c.py`), we've created a `ctypes.CDLL` instance from the shared file and can thus call the C function using the format 
`{CDLL_instance}.{function_name}({function_parameters})`.

### References

[**Calling C Functions from Python**](https://www.digitalocean.com/community/tutorials/calling-c-functions-from-python)


## Python Plugins

From the top-level directory (_i.e._, `CondaPlugins/python_plugins/[plugin]`) run the following to execute an editable install via `pip`:

```
$ pip install -e .
```

## Rust Plugins

> **Note:** Make sure you have `maturin` installed.

From the top-level directory (_i.e._, `CondaPlugins/rust_plugins/[plugin]`) run the following to execute an editable install via `pip`:

```
$ pip install -e .
```

... and then run:

```
$ maturin develop
```

### References

[**Maturin**](https://github.com/PyO3/maturin)

[**PyO3 User Guide**](https://pyo3.rs/v0.14.2/index.html)

[**Calling Rust from Python Using PyO3**](https://saidvandeklundert.net/learn/2021-11-18-calling-rust-from-python-using-pyo3/)
