## imoport this modules to solve the error module not found
import os , sys
from os.path import dirname, join , abspath
sys.path.insert(0,abspath( join(dirname(__file__), '..')))

from payment import payment_details


def course():
    print("This is my course details")

## error is still coming because python cannot locate the function    
## file is not trackable
payment_details.payment()