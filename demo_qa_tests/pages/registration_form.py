from selene import browser, have, be

from pathlib import Path
from selene import browser, have, command
import demo_qa_tests


class RegistrationPage:
    def __init__(self):
        self.subject = browser.element('#subjectsInput')
        pass

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script(
            "document.querySelector('.body-height').style.transform='scale(.40)'")

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def pick_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    def fill_mobile_phone(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__header__dropdown.react-datepicker__header__dropdown--select').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value="{year}"]').click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--0{day}').click()

    def pick_subject(self, value_1, value_2):
        self.subject.type(value_1).press_tab()
        self.subject.type(value_2)
        browser.element('#react-select-2-option-0').click()

    def pick_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-2"]').click()

    def set_picture(self, file: str):
        browser.element('#uploadPicture').type(
            str(Path(demo_qa_tests.__file__).parent.parent.joinpath(f'resources/{file}'))
        )

        return self

    def fill_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)

    def pick_state_and_city(self):
        browser.element('#state').click().element('#react-select-3-option-3').click()
        browser.element('#city').click().element('#react-select-4-option-0').click()

    def click_submit(self):
        browser.element('#submit').click()

    def assert_submit_user_info(self, first_and_last_name, email, gender, phone, birthday, subject, hobbies, picture, address, state_and_city):
        browser.element('.modal-content').element('table').all('tr').all('td').even.should(
            have.exact_texts(
                first_and_last_name,
                        email,
                        gender,
                        phone,
                        birthday,
                        subject,
                        hobbies,
                        picture,
                        address,
                        state_and_city))
