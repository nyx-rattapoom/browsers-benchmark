from engines.base import BrowserEngine


async def check_akamai_bypass(engine: BrowserEngine) -> bool:
    """
    Check if the Akamai Bot Manager bypass is successful (Best Buy)

    :param engine: BrowserEngine instance
    """

    element_found, element_html = await engine.locator('icon[aria-label="Search"]')

    return element_found
