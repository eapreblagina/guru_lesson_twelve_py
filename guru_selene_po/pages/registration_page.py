import os

from selene import have, command
from selene.support.shared import browser


class RegistrationForm:
    def open(self):
        browser.open('/automation-practice-form')
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')

    def fill_first_name(self, value):
        browser.element('#firstName').click().type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').click().type(value)

    def fill_email(self, email):
        browser.element('#userEmail').click().type(email)

    def choose_gender(self):
        browser.element('[name=gender][value=Female] + label').click()

    def fill_number(self, number):
        browser.element('#userNumber').click().type(number)

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subjects(self, subjects):
        browser.element('#subjectsInput').type(subjects).press_enter()

    def choose_hobbies(self, hobbies):
        browser.all('.custom-checkbox').element_by(have.text(hobbies)).click()

    def add_picture(self, file_name):
        return browser.element('#uploadPicture').set_value(os.path.abspath(f'resources/{file_name}'))

    def current_address(self, address):
        browser.element('#currentAddress').type(address).perform(command.js.scroll_into_view)

    def choose_state(self, state):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(state)).click()

    def choose_city(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(city)).click()

    def sumbit(self):
        browser.element('#submit').press_enter()

    def should_be_my_data(self, full_name, email, gender, number, birthday, subjects, hobbies, picture, current_address,
                          state_and_city):
        browser.element('.modal-header').should(have.exact_text('Thanks for submitting the form'))
        browser.element('.table-responsive').all('td:nth-of-type(2)').should(have.texts(
            full_name,
            email,
            gender,
            number,
            birthday,
            subjects,
            hobbies,
            picture,
            current_address,
            state_and_city
        ))
