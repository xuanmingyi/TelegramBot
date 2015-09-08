# -*- coding: utf-8 -*-
from plugins.base import BasePlugin

import sys, urllib, urllib2, json


class IpPlugin(BasePlugin):
    command = "/ip"

    def __init__(self, bot):
        self.bot = bot

    def _data(self, ip):
        url = "http://apis.baidu.com/apistore/iplookupservice/iplookup?ip={0}".format(ip)
        req = urllib2.Request(url)
        req.add_header("apikey", "47baaed88bd9bf016a3cbab4ab687b9b")
        resp = urllib2.urlopen(req)
        content = resp.read()
        return json.loads(content)

    def run(self, update):
        chat_id = update.message.chat_id
        text = update.message.text.encode('utf-8')
        ip = text[len(IpPlugin.command):].strip()
        data = self._data(ip)
        ret_text = ""
        if data['errNum'] == 0:
            ret_text += data['retData']['ip']
            ret_text += ": "
            for i in [data['retData']['country'],
                      data['retData']['province'],
                      data['retData']['city'],
                      data['retData']['district']]:
                if i and i != 'None':
                    ret_text += i
            if data['retData']['carrier'] != u"未知":
                ret_text += u" {0}".format(data['retData']['carrier'])
        self.bot.sendMessage(chat_id=chat_id,
                             text=ret_text.encode("utf8"))
