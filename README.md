# Introduction

This project is a REST API + web application that is taking input number, then returning the prettified, truncated version of this number, making the number more readable. Built with Django framework using Python.

# Requirements

- Python 3.x
- Django
- Django REST Framework
- Requests

# Installation

1. Clone the repository
   
   ```bash
   git clone https://github.com/YasinOkat/CyberneticTrial.git
3. Navigate to the repo path

   ```bash
   cd CyberneticTrial
5. Install the requirements

   ```bash
   pip install requirements.txt
  
# Usage
1. Navigate to to file where manage.py is located, in this case it's cybernetic_trial
   
   ```bash
   cd cybernetic_trial
2. Start the server
   
   ```bash
   python manage.py runserver
3. Now the server is running, go on the following URL for web application
   
   ```bash
   http://localhost:8000/
4. The home endpoint will return an UI, you can type the number there
5. If you want to take JSON response:
    
   ```bash
   http://localhost:8000/number
6. To prettify 1000000 for example, type in the browser:
    
   ```bash
   http://localhost:8000/1000000
   ```
7. This will return '1M'

# Algorithm
* If the number is less than 4 digits, it will just remove the decimal points, remains unchanged if it's integer
* If the number has 4 to 6 digits, the 'k' suffix will be added after the number is divided by 1000, e.g. 3.5k for 3500
* If the number has 7 to 9 digits, the 'M' suffix will be added after the number is divided by 1000000, e.g. 1M for 1000000
* If the number has 10 to 12 digits, the 'B' suffix will be added after the number is divided by 1 billion, e.g. 1.1B for 1123456789
* If the number has more than 12 digits, the 'T' suffix will be added after the number is divided by 1 trillion, e.g. 34.3T for 34253453445345
* Decimal points from the input will be always removed, there will be one number after the decmimal point in the prettified number, there won't be any number if the truncutad number is integer.


