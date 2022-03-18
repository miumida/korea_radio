"""Config flow for Korea Radio."""
import logging
import json

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers.aiohttp_client import async_create_clientsession

from .const import DOMAIN, TITLE

_LOGGER = logging.getLogger(__name__)

class KoreaRadioConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Korea Radio."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        """Initialize flow."""
        self._token: Required[str] = None

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        #if self._async_current_entries():
        #    return self.async_abort(reason="single_instance_allowed")

        uniqid = 'korea-radio-service'
        await self.async_set_unique_id(uniqid)

        if user_input is None:
            return self.async_show_form(step_id="user")

        return self.async_create_entry(title=TITLE, data=user_input)


    async def async_step_import(self, import_info):
        """Handle import from config file."""
        return await self.async_step_user(import_info)

