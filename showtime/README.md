# Add new modules

This program needs Python >=3.8 to run. If your version of Python is Python 2.X, use the following:

# Execution

```
alias py=python3
py ???
```

# Add pip modules

Add new modules using:

```
py -m pip install <NAME OF THE MODULE>
```

# Migrations

After changing the model, run:

```
py manage.py makemigrations
py manage.py migrate
```
