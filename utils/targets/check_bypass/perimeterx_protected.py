import asyncio

from engines.base import BrowserEngine


async def check_perimeterx_bypass(engine: BrowserEngine) -> bool:
    """
    Check if the PerimeterX (HUMAN Security) bypass is successful (Target.com)

    :param engine: BrowserEngine instance
    """

    await asyncio.sleep(10)  # time to load

    element_found, element_html = await engine.locator('iframe[id="px-captcha-modal"]')

    return not element_found
