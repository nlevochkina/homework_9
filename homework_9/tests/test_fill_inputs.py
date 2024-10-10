from homework_9.pages.registration_page import RegistrationPage
from homework_9.data import users


def test_fill_out_the_form():
    registration_page = RegistrationPage()
    registration_page.open_form()

    # WHEN
    registration_page.register_user(users.user)

    # registration_page.fill_full_name('Natalia', 'La')
    # registration_page.fill_email('natalia@mail.ru')
    # registration_page.choose_gender('label[for="gender-radio-2"]')
    # registration_page.fill_phone('1234567890')
    # registration_page.select_date_of_birth('react-datepicker__day--012',
    #                                        "//*[@class='react-datepicker__month-select']//option[@value='0']",
    #                                        "//*[@class='react-datepicker__year-select']//option[@value='1990']")
    # registration_page.fill_subject('Computer Science')
    # registration_page.choose_hobby('label[for="hobbies-checkbox-1"]')
    # registration_page.fill_adress('Moscow Street, 56, Moscow, Russia')
    # registration_page.upload_picture('../tests/resources/sun.jpeg')
    # registration_page.select_state_and_city('Haryana', 'Karnal')
    # registration_page.submit()

    # THEN
    registration_page.should_registered_user_with(
        'Natalia La',
        'natalia@mail.ru',
        'Female',
        '1234567890',
        '12 January,1990',
        'Computer Science',
        'sun.jpeg',
        'Moscow Street, 56, Moscow, Russia',
        'Sports',
        'Haryana Karnal'
    )
