import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.parametrize("browser_type", ["chromium", "firefox"])
def test_check_title(browser_type):
    with sync_playwright() as playwright:
        browser = getattr(playwright, browser_type).launch(headless=False)
        page = browser.new_page()

        page.goto('https://playwright.dev/')

        main_page_title = page.locator('h1.hero__title.heroTitle_ohkl')
        expect(main_page_title).to_be_visible()
        expect(main_page_title).to_have_text('Playwright enables reliable end-to-end testing for modern web apps.')