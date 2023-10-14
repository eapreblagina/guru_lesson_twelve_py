
from selene.support.shared import browser
from selene import have, by
from selene import command
import os



def test_valid_Practice_Form():
    #when
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')
    browser.element('#firstName').click().type('Kate')
    browser.element('#lastName').click().type('Preblagina')
    browser.element('#userEmail').click().type('Katitoporova@bk.ru')
    browser.element('[name=gender][value=Female] + label').click()
    browser.element('#userNumber').click().type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('August')
    browser.element('.react-datepicker__year-select').type('2000')
    browser.element('.react-datepicker__day--009').click()

# ручной ввод даты
    #browser.element('#dateOfBirthInput').perform(command.js.set_value('9 Aug 2000'))

    browser.element('#subjectsInput').type('Economics').press_enter()

    browser.all('.custom-checkbox').element_by(have.text('Sports')).click()

    browser.element('#uploadPicture').set_value(os.path.abspath('resources/foto.jpg'))

    browser.element('#currentAddress').type('Пушкина 15').perform(command.js.scroll_into_view)

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Karnal')).click()

    browser.element('#submit').press_enter()

    #then

    browser.element('.modal-header').should(have.exact_text('Thanks for submitting the form'))
    browser.element('.table-responsive').all('td:nth-of-type(2)').should(have.texts(
        'Kate Preblagina',
        'Katitoporova@bk.ru',
        'Female',
        '1234567890',
        '09 August,2000',
        'Economics',
        'Sports',
        'foto.jpg',
        'Пушкина 15',
        'Haryana Karnal'
    ))