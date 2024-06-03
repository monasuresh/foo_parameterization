# foo_parameterization

A software package that calculates the complex (yet entirely fictitious) Foo et al. parameterization.

## Installation

```bash
$ pip install foo
```

## Usage

System Requirements:

- poetry.
- anaconda
- python3.9 and above

==============================

How to run the CLI:

Extract the tarball:

```bash
$ tar xvf foo-0.1.0.tar.gz
```

prime your python environment:

```bash
$ conda create --name foo python=3.9 -y
$ conda init
$ conda activate foo
```

To run foo_parameterization_cli.py:


```bash
$ cd foo-0.1.0
$ poetry install
$ python3 src/foo/foo_parameterization_cli.py
```


The user will see the prompt:



Available shape properties:

1. volume

Enter the number corresponding to the shape property(1): 



After entering the desired shape property the user  will see the prompt:



Available shapes:

1. sphere

Enter the number corresponding to the shape (1):



After entering the desired shape, the user will see the prompt:

Enter the radius:

=============================



To run tests, clone github repository and follow the above instructions to setup the environment:


```bash
$ cd foo-0.1.0
$ poetry run pytest tests/
```


=======================================

For external consumption:

- Create a python project with a main with the following lines of code

```python
from foo.foo_parameterization_core import FooParameterization
if __name__ == "__main__":
    print(FooParameterization.calculate_volume("sphere", 3))
```

- install the wheel onto the newly created python project - pip install foo-0.1.0-py3-none-any.whl

- execute the main
The user will be prompted to select a shape and provide necessary parameters (e.g., radius).
    The CLI then calculates and displays the volume of the selected shape using FooParameterization.


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`foo_parameterization` was created by Monica Suresh. It is licensed under the terms of the MIT license.

## Credits

`foo_parameterization` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
