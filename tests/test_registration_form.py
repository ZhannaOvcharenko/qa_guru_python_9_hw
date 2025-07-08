from pages.registration_page import RegistrationPage


def test_registration_form():
    # Открыть форму регистрации
    registration_page = RegistrationPage()
    registration_page.open()
    # Заполнить поля формы регистрации
    (
        registration_page
        .fill_first_name('Test')
        .fill_last_name('Testov')
        .fill_email('test.testov@gmail.com')
        .choose_gender('Male')
        .fill_phone_number('9839583958')
        .fill_date_of_birth('08', 'July', '1996')
        .choose_subject('Computer Science')
        .choose_hoobies('Sports')
        .upload_picture('demoqa.jpg')
        .fill_current_address('St. Petersburg, Lomanosovskaya street')
        .choose_state('Uttar Pradesh')
        .choose_city('Agra')
        # Подтвердить регистрацию
        .submit_form()
    )

    # Проверить данные в таблице
    registration_page.should_registered_user_with(
        'Test Testov',
        'test.testov@gmail.com',
        'Male',
        '9839583958',
        '08 July,1996',
        'Computer Science',
        'Sports',
        'demoqa.jpg',
        'St. Petersburg, Lomanosovskaya street',
        'Uttar Pradesh Agra'
    )
