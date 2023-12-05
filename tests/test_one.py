import allure

from guru_selene_po.pages.registration_page import RegistrationForm


def test_valid_Practice_Form():
    with allure.step("Открыть страницу регистрации пользователей"):
        registration_page = RegistrationForm()
        registration_page.open()

    with allure.step("Заполнить форму регистрации тестовыми данными"):
        registration_page.fill_first_name('Kate')
        registration_page.fill_last_name('Preblagina')
        registration_page.fill_email('Katitoporova@bk.ru')
        registration_page.choose_gender()
        registration_page.fill_number('1234567890')
        registration_page.fill_birthday('2000', 'August', '09')
        # ручной ввод даты
        # browser.element('#dateOfBirthInput').perform(command.js.set_value('9 Aug 2000'))
        registration_page.fill_subjects('Economics')
        registration_page.choose_hobbies('Sports')
        registration_page.add_picture('foto.jpg')
        registration_page.current_address('Пушкина 15')
        registration_page.choose_state('Haryana')
        registration_page.choose_city('Karnal')
        registration_page.sumbit()

    with allure.step("Проверка, что пользователь зарегистрирован"):
        registration_page.should_be_my_data(
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
        )
