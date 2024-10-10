import os

from selene import browser, be, have
from selenium.webdriver.common.by import By

from homework_9.data.users import User


class RegistrationPage:

    def open_form(self):
        browser.open('/automation-practice-form')

        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_full_name(self, first_name, last_name):
        browser.element('#firstName').should(be.blank).type(first_name)
        browser.element('#lastName').should(be.blank).type(last_name)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def choose_gender(self, value):
        browser.element(value).click()

    def fill_phone(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def select_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.driver.find_element(By.XPATH, month).click()
        browser.driver.find_element(By.XPATH, year).click()
        browser.driver.find_element(By.CLASS_NAME, day).click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_adress(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)

    def choose_hobby(self, value):
        browser.element(value).click()

    def upload_picture(self, path):
        image_path = os.path.abspath(path)
        browser.element('#uploadPicture').send_keys(image_path)

    def select_state_and_city(self, state, city):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(city)).click()

    def submit(self):
        browser.element('#submit').press_enter()

    def register_user(self, user: User):
        self.fill_full_name(user.first_name, user.last_name)
        self.fill_email(user.email)
        self.choose_gender(user.gender)
        self.fill_phone(user.phone)
        self.select_date_of_birth(user.day, user.month, user.year)
        self.fill_subject(user.subject)
        self.choose_hobby(user.hobbies)
        self.upload_picture(user.picture)
        self.fill_adress(user.address)
        self.select_state_and_city(user.state, user.city)
        self.submit()
        return self

    def should_registered_user_with(self, user: User, fill_full_name, fill_email, choose_gender, fill_phone,
                                    fill_subject, fill_adress, choose_hobby, upload_picture, select_state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                fill_full_name,
                fill_email,
                choose_gender,
                fill_phone,
                f"{user.day} {user.month},{user.year}",
                fill_subject,
                upload_picture,
                fill_adress,
                choose_hobby,
                select_state_and_city
            )
        )
        return self
