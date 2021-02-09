import re
import sys

email = '{{ cookiecutter.email}}'

if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
    print(f'{email} is not a valid email.')
    sys.exit(1)
