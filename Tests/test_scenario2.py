import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://bissafety.com/")
    page.get_by_role("link", name="Book a Demo with an Expert").click()
    page.get_by_role("link", name="clicking here").click()
    page.get_by_role("link", name="return to the home page").click()