[![PyPI version](https://badge.fury.io/py/jif.svg)](https://badge.fury.io/py/jif)

# jif

jif is a small CLI tool to store and run bash scripts.

## Usage

1. Create a jif file (`jif.json` or `jif.yml`).
2. Add a scripts object. E.g. 
```
{
  "start": "python app.py",
  "lint": "black myapp"
}
```

or

```
start: python app.py
lint: black myapp
```

3. Use jif to run your scripts. E.g. `jif start`, `jif lint`

4. Profit???

---
jif will initially try to load the `jif.json` file in the current directory, if it is not found then it will try to load the `jif.yaml` file.