from data.users import User, Gender, Hobby, State
from pages.registration_page import RegistrationPage


def test_registration_form():

    registration_page = RegistrationPage()
    test_user = User()

    registration_page.open()
    registration_page.register_user(test_user)
    registration_page.should_registered_user_with(test_user)
