import allure
import pytest

from playwright.sync_api import Playwright, Page
from _pytest.fixtures import SubRequest

from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill(
        email="user.name@gmail.com",
        username="username",
        password="password",
    )
    registration_page.click_registration_button()

    # Сохраняем состояние браузера
    context.storage_state(path="browser-state.json")


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright, request: SubRequest) -> Page:  # type: ignore
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state='browser-state.json'
    )

    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context(storage_state="browser-state.json", record_video_dir='./videos')
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # page = context.new_page()
    #
    # yield page
    #
    # context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    # browser.close()
    #
    # allure.attach.file(
    #     source=f'./tracing/{request.node.name}.zip',
    #     name='trace',
    #     extension='zip'
    # )
    #
    # allure.attach.file(
    #     source=page.video.path(),
    #     name='video',
    #     attachment_type=allure.attachment_type.WEBM
    # )


@pytest.fixture
def chromium_page(playwright: Playwright, request: SubRequest) -> Page: # type: ignore
    yield from initialize_playwright_page(playwright, test_name=request.node.name)
    #
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context(record_video_dir='./videos')
    # context.tracing.start(screenshots=True, snapshots=True, sources=True)
    # page = context.new_page()
    #
    # yield page
    #
    # context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    # browser.close()
    #
    # allure.attach.file(
    #     source=f'./tracing/{request.node.name}.zip',
    #     name='trace',
    #     extension='zip'
    # )
    #
    # allure.attach.file(
    #     source=page.video.path(),
    #     name='video',
    #     attachment_type=allure.attachment_type.WEBM
    # )
