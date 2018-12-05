# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules

# import datetime
# import time
from validator import validate_email
from camelcase import CamelCase
from datetime import date
from time import time

# today = datetime.date.today()
today = date.today()

timestamp = time()

print(timestamp)

# Pip module

c = CamelCase()
print(c.hump('hello there world'))


# Import custom module

email = 'test@test.com'

if validate_email(email):
    print('email is valid')
else:
    print('email is bad')
