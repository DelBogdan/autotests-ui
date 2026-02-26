from playwright.sync_api import expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверить наличие и текст заголовка "Courses"
    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    # Проверить наличие и текст блока "There is no results"
    courses_list_empty_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_list_empty_title).to_be_visible()
    expect(courses_list_empty_title).to_have_text("There is no results")

    # Проверить наличие и видимость иконки пустого блока
    courses_list_empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_list_empty_view_icon).to_be_visible()

    # Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    courses_list_empty_view_description = chromium_page_with_state.get_by_test_id(
        'courses-list-empty-view-description-text')
    expect(courses_list_empty_view_description).to_be_visible()
    expect(courses_list_empty_view_description).to_have_text(
        "Results from the load test pipeline will be displayed here")
