# -*- coding: utf-8 -*-
"""
Support for AIS knowledge

For more details about this component, please refer to the documentation at
https://www.ai-speaker.com
"""
import asyncio
import logging
import voluptuous as vol
from homeassistant.components.ais_dom import ais_global
from homeassistant.helpers import config_validation as cv
from homeassistant.components import ais_cloud

aisCloud = ais_cloud.AisCloudWS()

DOMAIN = "ais_knowledge_service"
SERVICE_ASK = "ask"
SERVICE_ASK_WIKI = "ask_wiki"
ATTR_TEXT = "text"
ATTR_SAY_IT = "say_it"
SERVICE_ASK_SCHEMA = vol.Schema(
    {vol.Required(ATTR_TEXT): cv.string, vol.Optional(ATTR_SAY_IT): cv.boolean}
)
_LOGGER = logging.getLogger(__name__)
GKS_URL = "https://kgsearch.googleapis.com/v1/entities:search"
G_GKS_KEY = None


@asyncio.coroutine
def async_setup(hass, config):
    """Register the service."""
    config = config.get(DOMAIN, {})
    yield from get_key_async(hass)

    @asyncio.coroutine
    def ask(service):
        """ask service about info"""
        query = service.data[ATTR_TEXT]
        yield from process_ask_async(hass, query)

    @asyncio.coroutine
    def ask_wiki(service):
        """ask wikipedia service about info"""
        query = service.data[ATTR_TEXT]
        yield from process_ask_wiki_async(hass, query)

    # register services
    hass.services.async_register(DOMAIN, SERVICE_ASK, ask, schema=SERVICE_ASK_SCHEMA)

    hass.services.async_register(
        DOMAIN, SERVICE_ASK_WIKI, ask_wiki, schema=SERVICE_ASK_SCHEMA
    )

    return True


@asyncio.coroutine
def process_ask_async(hass, query):
    import requests

    global G_GKS_KEY
    """Ask the service about text."""

    full_message = ""
    image_url = None
    if G_GKS_KEY is None:
        try:
            ws_resp = aisCloud.key("kgsearch")
            json_ws_resp = ws_resp.json()
            G_GKS_KEY = json_ws_resp["key"]
        except:
            yield from hass.services.async_call(
                "ais_ai_service",
                "say_it",
                {"text": "Nie udało się wykonać, sprawdź połączenie z Intenetem"},
            )
            return

    req = requests.get(
        GKS_URL,
        params={
            "query": query,
            "limit": 1,
            "indent": True,
            "key": G_GKS_KEY,
            "languages": "pl",
        },
    )
    try:
        response = req.json()
        element = response["itemListElement"][0]
        result = element["result"]
        full_message = result["description"]
        # try to get more info
        try:
            full_message = (
                full_message + "\n\n" + result["detailedDescription"]["articleBody"]
            )
        except Exception:
            pass
        # try to get image
        try:
            image_url = result["image"]["contentUrl"]
        except Exception:
            pass

    except Exception:
        full_message = "Brak wyników"

    yield from hass.services.async_call(
        "ais_ai_service", "say_it", {"text": full_message, "img": image_url}
    )

    return full_message


@asyncio.coroutine
def process_ask_wiki_async(hass, query):
    import wikipedia

    wikipedia.set_lang("pl")
    """Ask the service about text."""
    image_url = None
    try:
        full_message = wikipedia.summary(query)
    except Exception:
        full_message = "Brak wyników"

    try:
        images = wikipedia.page(query).images
        for image in images:
            if not image.endswith(".svg"):
                image_url = image

    except Exception:
        full_message = "Brak wyników"

    yield from hass.services.async_call(
        "ais_ai_service", "say_it", {"text": full_message, "img": image_url}
    )

    return full_message


@asyncio.coroutine
def get_key_async(hass):
    def load():
        global G_GKS_KEY
        try:
            ws_resp = aisCloud.key("kgsearch")
            json_ws_resp = ws_resp.json()
            G_GKS_KEY = json_ws_resp["key"]
        except:
            ais_global.G_OFFLINE_MODE = True

    yield from hass.async_add_job(load)
