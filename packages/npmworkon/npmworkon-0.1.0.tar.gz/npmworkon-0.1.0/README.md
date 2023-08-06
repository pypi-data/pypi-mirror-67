# npmworkon

Quick script to handle nodeenv outside of the virtualenv wrapper.

If you want it in the same virtualenv wrapper, `nodeenv -p` is what you want and you don't need npmworkon.

## Installation

```
pip install npmworkon
```

The npm virtualenv will be created in the home directory `.npmvirtualenvs`. For now, this value is hardcoded.

## Usage

Create a Python virtualenv
```
➜ mkvirtualenv py_venv
[...]
```

Install npmworkon
```
(py_venv) ➜ pip install npmworkon
[...]
```

Create a npm virtualenv
```
(py_venv) ➜ $(npmworkon node_venv)
```

List npm virtualenv
```
(node_venv) (py_venv) ➜ npmworkon
node_venv
```

Desactivate npm virtualenv
```
(node_venv) (py_venv) ➜ deactivate_node
```

Remove npm virtualenv
```
(py_venv) ➜ npmworkon --rm node_venv

(py_venv) ➜ npmworkon
# node_venv is gone :)
```
