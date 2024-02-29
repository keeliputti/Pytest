# Pytest
https://pypi.org/project/pytest/

## Installion <br>

### Install the latest version
```
pip install pytest
```


### Install a specific version
```
pip install pytest==5.4.3
```
<br>

## Venv and requirements.txt creation:
### create venv:
```
python -m venv <venv_name>
```

### activate a venv:
```
source <venv_name>/bin/activate
```

### deactivate a venv:
```
deactivate 
```

### create requriements.txt from your venv:
```
pip freeze > requirements.txt
```

### See all pkgs in your python installation:
```
pip3 list
pip list
```

### Put all pkgs list in a file:
```
pip freeze > requirements.txt
```

## Running tests:
```
pytest <folder-name>
pytest <file-name>
```
Note: Enable virtual env first if running from cmd

### Pytest options:
```
-v : verbode mode. increases the verbosity level. 
       Prints a message each time module is initialized, 
       showing the place (filename or built-in) from which it is loaded.

--if, --last-failed:  only re-run the failures

--ff, --failed-first: to run the failures first and then the rest of the tests.
```
