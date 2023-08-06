# OSIRIS VALIDATOR

Osiris Validator is a set of decorators for validation in Flask-restless and SQLAlchemy

(Readme is under construction...)

## Getting Started

### Installing

```
pip install osirisvalidator
```

### Usage
The parameter *validation_exceptions* in **APIManager.create_api()**  from Flask-restless must be set to use osiris' **ValidationException**.

```python
from osirisvalidator.exceptions import ValidationException

[...]

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(User, validation_exceptions=[ValidationException], methods=['GET', 'POST'])
```

To use the decorators, the **validates()** decorator from SQLAlchemy must be used before, and the pattern must be followed.


See about in: https://flask-restless.readthedocs.io/en/stable/customizing.html#capturing-validation-errors


The parameter "field" is required and you can set a custom message.
```python
from sqlalchemy.orm import validates
from osirisvalidator.string import *
from osirisvalidator.internet import valid_email

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(60), nullable=False)

    @validates('name')
    @not_blank(field='name', message='Custom message')
    @is_alpha_space(field='name')
    @string_len(field='name', min=3, max=100)
    def validate_name(self, key, name):
        return name

    @validates('email')
    @not_blank(field='email')
    @valid_email(field='email')
    def validate_email(self, key, email):
        return email

``` 

## List of validators

### osirisvalidator.string
- not_empty
- not_blank
- is_alpha
- is_alpha_space (alpha characters and space)
- is_alnum
- is_alnum_space (alphanumeric characters and space)
- is_digit
- string_len (mandatory parameters: **min** and **max**)
- match_regex (mandatory parameter: **regex**) 

### osirisvalidator.number
- min_max (mandatory parameters: **min** and **max**)

### osirisvalidator.internet
- valid_email

## osiris.intl.br
- valid_cpf
- valid_cnpj
