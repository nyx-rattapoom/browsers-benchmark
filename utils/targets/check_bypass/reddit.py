from engines.base import BrowserEngine


async def check_reddit_bypass(engine: BrowserEngine) -> bool:
    """
    Check if the Reddit bypass is successful

    :param engine: BrowserEngine instance
    """

    element_found, element_html = await engine.locator(
        'a[href^="https://support.reddithelp.com/hc/en-us/requests/new?ticket_form_id="]'
    )

    return not element_found
