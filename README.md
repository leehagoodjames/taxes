# taxes
A lightweight Python Repo for calculating personal income taxes. Contributions are welcome.

## Installing
```shell
python3 -m pip install easytax
```

## Example Usage
```shell
python3 examples/example.py
```

## Contributing
1. Clone the [taxes](https://github.com/leehagoodjames/taxes) repo with:
```shell
git clone https://github.com/leehagoodjames/taxes.git
```
2. Change directories to the project's root with:
```shell
cd taxes
```
3. Ensure tests pass with:
```shell
python3 -m unittest discover tests
```
4. Make awesome changes!


## Releasing New Modules
1. Increment the version in `pyproject.toml`
2. Build with:
```shell
rm -rf dist; python3 -m build
```
3. Upload to pypi with:
```shell
python3 -m twine upload --repository pypi dist/*
```
