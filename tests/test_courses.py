from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполнить поле Email значением: user.name@gmail.com
        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.fill("user.name@gmail.com")

        # Заполнить поле Username значением: username
        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_username_input.fill("username")

        # Заполнить поле Password значением: password
        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_password_input.fill("password")

        # Нажать на кнопку Registration
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохраняем состояние браузера
        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверить наличие и текст заголовка "Courses"
        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")

        # Проверить наличие и текст блока "There is no results"
        courses_list_empty_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_list_empty_title).to_be_visible()
        expect(courses_list_empty_title).to_have_text("There is no results")

        # Проверить наличие и видимость иконки пустого блока
        courses_list_empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(courses_list_empty_view_icon).to_be_visible()

        # Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
        courses_list_empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(courses_list_empty_view_description).to_be_visible()
        expect(courses_list_empty_view_description).to_have_text(
            "Results from the load test pipeline will be displayed here")
