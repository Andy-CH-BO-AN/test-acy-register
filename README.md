# ACY regyster automation test
Create an automated testing script for "https://www.acy.com/en/open-live-account" register.
Use pytest with selenium to test if we can register ACY succesfully or not.

# Structure
### Locators.py
Contains HTML element which used in the test scrpit.
### main.py
Control the browser to stimulate the step to register the user account.
### test_acy_register.py
Contains test case to register the user account.
### valid_country.py
A tool to check those countries that can't register the ACY user account.

# Set up
git clone https://github.com/Andy-CH-BO-AN/test-acy-register.git
pip install -r requirement.txt
pytest test_acy_register.py
