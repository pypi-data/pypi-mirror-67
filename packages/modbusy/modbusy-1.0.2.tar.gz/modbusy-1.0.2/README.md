# Modbusy - Modbus for mortals

Modbusy simplifies the creation of Modbus slaves. It is a Python library
providing a simple interface to reduce boilerplate code when interfacing with
uModbus. It requires only rudimentary knowledge of the Modbus protocol.

Additional helper methods are also provided to further accelerate development.

## Example

The following example uses the `modbusy.tcp_app()` helper to create a slave
that provides access to a single signed, 32-bit integer.

Execute the script using the following command:

`python modbusy_example.py --address 127.0.0.1 --port 5020 12345`

**modbusy_example.py**
```python
import contextlib

import click
import modbusy


# The order of decorators is important
@modbusy.tcp_app()
@click.argument('value', type=int)  # require a command-line argument to initialize value
@contextlib.contextmanager
def slave(app, value) -> None:
    '''Modbus emulator to expose a single signed 32-bit integer.'''

    @app.register(0, modbusy.INT32)
    def read_value(for_write):
        return value

    @read_value.setter
    def write_value(new_value):
        nonlocal value
        value = new_value

    yield


if __name__ == '__main__':
    slave()
```

Initialization should occur before the `yield` and cleanup should occur after.

## Description

Modbusy is 100% compatible with uModbus and can be used in existing code to
simplify and extend it. Values are exposed on the slave by decorating getter
and setter functions/methods. Function codes, address spaces, and address
ranges are automatically determined based on the base address and the type
registered for the getter and on whether or not a setter is provided.

### Address spaces

`BOOL` types are considered Modbus coils and use one address space. All other
Modbusy types are treated as Modbus registers and use another address space.

### Extends uModbus

Modbusy is designed to work with an already exceptional Modbus library:
uModbus.  The `patch_server()` function is designed to add the `register()`
decorator and the `update_defaults()` method to the server object returned by
either `umodbus.server.tcp.get_server()` or `umodbus.server.serial.get_server()`.

```python
def patch_server(server, slave_id: int = 1, byteorder: str = 'big', mixed: bool = False):  # returns server
    ...
```

It may also be passed default slave ID and endianness (byte order and mixed
mode). This may be updated later using `update_defaults()`.

```python
def update_defaults(self, slave_id: int = None, byteorder: str = None, mixed: bool = None) -> None:
    ...
```

#### TCP server example

```python
from socketserver import TCPServer
from umodbus.server.tcp import RequestHandler, get_server

import modbusy

TCPServer.allow_reuse_address = True
app = get_server(TCPServer, ('localhost', 502), RequestHandler)
modbusy.patch_server(app, slave_id=2, byteorder='little', mixed=True)
```

### Registering getters and setters

The `register()` decorator is used to define points that are exposed by the
slave. It is a high-level wrapper around uModbus's `route()` decorator.

```python
def register(self, address: Union[int, Iterable[int]], kind: RegisterType, *,
             slave_id: int = None, byteorder: str = None, mixed: bool = None) -> None:
    ...
```

The *address* parameter should typically be the base Modbus address for the
value. The full address range will be computed based on the size of the value
defined by the *kind* parameter, but it may be overridden by passing a list.
If not provided, the *slave_id*, *byteorder*, and *mixed* parameters will use
the server defaults. The available operations (function codes) are defined by
the *kind*.

```python
@app.register(100, modbusy.UINT64)
def read_value(for_write):
    return value
```

The `register()` decorator is used to define getters. The wrapped function is
also used when performing a partial update of a value (i.e., updating a word).
In that case, the *for_write* parameter will be True, and may be used to
suppress calculations that might normally occur on a read. Use the `setter()`
decorator of the read function to decorate the write function, similar to how
the built-in `property()` decorator works.

```python
@read_value.setter
def write_value(new_value):
    value = new_value
```

If the second word of the value is being written, `read_value(True)` is
called, bytes 3 and 4 are updated, and the new value is passed to
`write_value()`. Writes are atomic for a single TCP request.

### Read/write object attributes

The `attribute()` helper method is used to make object attributes accessible
via Modbus without a bunch of boilerplate code. 

```python
class Settings:
    knob = 123
    flag = False

app.register(104, modbusy.INT32).attribute(Settings, 'knob', writable=False)
app.register(10, modbusy.BOOL).attribute(Settings, 'flag')
```

The *writable* parameter defaults to True. It may also be a callable that can
override the default behavior. For instance, if writes should be allowed on
read-only values without an error, then *writable* could be passed a no-op.

```python
app.register(104, modbusy.INT32).attribute(Settings, 'knob', writable=lambda _: None)
```

### Predefined types

`BOOL`:
A boolean type implemented as a bit value or Modbus coil

`INT16`:
Signed, 16-bit integer

`INT32`:
Signed, 32-bit integer

`INT64`:
Signed, 64-bit integer

`INT128`:
Signed, 128-bit integer

`UINT16`:
Usigned, 16-bit integer

`UINT32`:
Usigned, 32-bit integer

`UINT64`:
Usigned, 64-bit integer

`UINT128`:
Usigned, 128-bit integer

`FLOAT`:
4-byte, floating-point integer

`FLOAT`:
8-byte, floating-point integer

`String(N)`:
N-byte string (address is rounded up to a 2-byte boundary)

### Extending types

Custom integers may be created using `modbusy.Integer`. All modbusy types
subclass `modbusy.RegisterType`. Additional types may be created by
subclassing `modbusy.RegisterType` as well.

### Address validation

uModbus and, by extension, modbusy, do no validation of addresses to prevent
overlap. The `assert_unque_addresses()` helper can perform that validation.

```python
modbusy.assert_unique_addresses(app)
```

### Easy application creation

`modbus.tcp_app()` is a helper function to avoid writing boilerplate code for
parsing arguments and instantiating and running a TCP slave server. It
decorates a Python context manager, typically created using the
`contextlib.contextmanager` decorator, with optional click command-line
parsing. See the example at the top of this file for an example.

## Creating a slave from a CSV file

A Modbus slave can be easily created from a CSV time series file. 

**sample_pv_1min.csv**
```csv
utc_timestamp,active_power_total,dc_voltage,dc_unclipped_power
2018-03-01 00:00:00,71431,686.505555555555,72056
2018-03-01 00:01:00,70676,687.975925925926,71287
2018-03-01 00:02:00,69835,687.888888888889,70436
2018-03-01 00:05:00,67641,687.964814814815,68207
2018-03-01 00:06:00,67039,688.537037037037,67603
2018-03-01 00:07:00,66345,688.925925925926,66898
2018-03-01 00:08:00,65831,689.492592592593,66375
2018-03-01 00:10:00,64436,690.283333333333,64957
...
```

**pv.yaml**
```yaml
registers:
  - address: 0
    column: active_power_total
    type: float
    trigger: yes
  - address: 2
    column: dc_voltage
    type: float
  - address: 4
    column: dc_unclipped_power
    type: float
  - address: 100
    type: string[19]
    column: utc_timestamp
```

Given the CSV data file and the YAML configuration file above, a slave can be
started using the following command:

`python -m modbusy.csvslave --address 127.0.0.1 --port 5020 pv.yaml sample_pv_1min.csv`

When the first register, at address 0, is read, it will cause the next row in
the CSV file to be read because it is a trigger register. After the entire file
is read, it will start back at the beginning looping infinitely.

See the source code for more information. Check out the `validate()` function
for the schema describing the YAML configuration.

## License

Modbusy is licensed under a BSD 3-clause license found [here](LICENSE).
