import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
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


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:  # type: ignore
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page
    browser.close()
