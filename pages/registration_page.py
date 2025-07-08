import os
from selene import browser, have

class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.phone = browser.element('#userNumber')
        self.subject = browser.element('#subjectsInput')
        self.hobby = browser.all('#hobbiesWrapper label')
        self.picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')
        self.submit = browser.element('#submit')
        self.registered_user = browser.element('.table-responsive').all('td')

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def choose_gender(self, value):
        self.gender.element_by(have.value(value)).element('..').click()
        return self

    def fill_phone_number(self, value):
        self.phone.type(value)
        return self

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def choose_subject(self, value):
        self.subject.type(value).press_enter()
        return self

    def choose_hoobies(self, value):
        self.hobby.element_by(have.exact_text(value)).click()
        return self

    def upload_picture(self, value):
        self.picture.send_keys(os.path.abspath(value))
        return self

    def fill_current_address(self, value):
        self.current_address.type(value)
        return self

    def choose_state(self, value):
        self.state.type(value).press_enter()
        return self

    def choose_city(self, value):
        self.city.type(value).press_enter()
        return self

    def submit_form(self):
        self.submit.click()
        return self

    def should_registered_user_with(self, full_name, email, gender, phone, date_of_birth, subject, hobby, picture,
                                    address, state_and_city):
        self.registered_user.even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date_of_birth,
                subject,
                hobby,
                picture,
                address,
                state_and_city
            )
        )
        return self