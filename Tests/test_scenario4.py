import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    # Navigate to the page
    page.goto("https://bissafety.com/request-a-demo/")

    # Wait for the iframe to load (Adjust the timeout as necessary)
    iframe_locator = page.locator("iframe[title='Form 0']")
    iframe_locator.wait_for(state="visible", timeout=5000)  # Wait for the iframe to be visible

    # Access the iframe content using .content_frame()
    iframe = iframe_locator.content_frame()

    # Now you can interact with the form fields inside the iframe
    iframe.locator('label:has-text("Email*")').click()  # Click on the email label if necessary
    iframe.locator('input[name="email"]').fill("ahgdj")  # Fill the email field
   