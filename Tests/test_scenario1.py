import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://bissafety.com/")
    page.get_by_role("link", name="Network").click()
    page.get_by_role("link", name="Course Owners", exact=True).click()
    page.locator("#et-button-184081").click()
    page.get_by_role("link", name="Discuss Your Project ").click()
    page.screenshot(path="test1.png")