import asyncio

from engines.base import BrowserEngine


async def check_kasada_bypass(engine: BrowserEngine) -> bool:
    """
    Check if the Kasada bypass is successful (Canada Goose)

    :param engine: BrowserEngine instance
    """

    await asyncio.sleep(10)

    element_found, element_html = await engine.locator('div[id="site-banner-container"]')

    return element_found
