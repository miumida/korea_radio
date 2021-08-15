import logging
import functools
import json
import requests
import os
from urllib.parse import quote

import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, EBS_ARTWORK, EBS_URL, FM4U_ARTWORK, CBS_URL, _MBC_CH, _MBC_CH_PARAM, MBC_BSE_URL, MBC_CALL_URL

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    """Set up the Korea Radio."""

    def radio_handle(service):
        """Service handle for Play Radio."""
        entity_ids = service.data["entity_id"]
        ch = service.data.get("channel")

        if not isinstance(entity_ids, list):
            entity_ids = [entity_ids]

        for entity_id in entity_ids:

            try:
                if ch == "EBS":
                    play_media(entity_id,EBS_URL, 'EBS FM Radio', EBS_ARTWORK)

                if ch == "mbcfm4u" or ch == "mbcfm" or ch == "allthat":
                    url = get_mbc_ch_url(ch)

                    play_media(entity_id, url, _MBC_CH_PARAM[ch][0], _MBC_CH_PARAM[ch][1])

                #if ch == "cbs":
                #    play_media(entity_id, CBS_URL, 'CBS MUSIC FM Radio', EBS_ARTWORK)

            except Exception as ex:
                _LOGGER.error("[Korea Radio] call Servie Exception : %s", ex )

    def play_media(entity_id, url, title, thumb):
        payload = {
            "entity_id": entity_id,
            "media_content_id": url,
            "media_content_type": "music",
            "extra":
                {"metadata" :
                    {"metadataType" : 3 ,
                     "title" :  title,
                     "images" :[{"url" : thumb}]
                    }
                }
            }

        try:
            hass.services.call("media_player", 'play_media', payload, False)
        except Exception as ex:
            _LOGGER.error("[Korea Radio] call Servie Exception : %s", ex )


    def get_mbc_ch_url(ch):
        header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36', 'Referer' : 'http://mini.imbc.com/', 'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7', 'Accept-Encoding' : 'gzip, deflate'}

        html = requests.get(MBC_BSE_URL.format(_MBC_CH[ch]), headers=header)
        text = str(html.text)

        text = 'http://' + text.split('"http://')[1].split('"')[0]

        html2 = str(requests.get(text, headers=header).text)
        text2 = html2.split('m3u8?')[1].strip()

        urls = MBC_CALL_URL.format( _MBC_CH[ch], _MBC_CH[ch], text2)

        #_LOGGER.error( "[Korea Radio] get_mbc_ch_url() urls : %s", urls )

        return urls

    hass.services.register(DOMAIN, "play_radio", radio_handle)
    return True
