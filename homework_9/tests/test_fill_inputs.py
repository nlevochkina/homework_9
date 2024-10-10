from homework_9.pages.registration_page import RegistrationPage
from homework_9.data import users


def test_fill_out_the_form():
    registration_page = RegistrationPage()
    registration_page.open_form()

    # WHEN
    registration_page.register_user(users.user)

    # THEN
    registration_page.should_registered_user_with(users.user)

