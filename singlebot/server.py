# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re, json, requests, urllib

class LineServer(object):
    with open("data.json","r") as fp:
        data = json.load(fp)
    LINE_HOST_DOMAIN            = data["LINE_HOST_DOMAIN"]
    LINE_OBS_DOMAIN             = data["LINE_OBS_DOMAIN"]
    LINE_TIMELINE_API           = data["LINE_TIMELINE_API"]
    LINE_TIMELINE_MH            = data["LINE_TIMELINE_MH"]

    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'

    CHANNEL_ID = {
        'LINE_TIMELINE': '1341209950',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440'
    }

    USER_AGENT  = data["USER_AGENT"]
    APP_TYPE    = ApplicationType.IOS
    APP_NAME    = data["APP_NAME_IPAD"]
    PHONE_TYPE  = ApplicationType.IOS
    PHONE_NAME  = 'IOS\t7.14.0\tiPhone OS\t10.12.0'
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = data["SYSTEM_NAME"]
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    _session    = requests.session()
    channelHeaders  = {}
    Headers         = {}

    def __init__(self):
        self.Headers = {}
        self.channelHeaders = {}

    def parseUrl(self, path):
        return self.LINE_HOST_DOMAIN + path

    def urlEncode(self, url, path, params=[]):
        try:        # Works with python 2.x
            return url + path + '?' + urllib.urlencode(params)
        except:     # Works with python 3.x
            return url + path + '?' + urllib.parse.urlencode(params)

    def getJson(self, url, allowHeader=False):
        if allowHeader is False:
            return json.loads(self._session.get(url).text)
        else:
            return json.loads(self._session.get(url, headers=self.Headers).text)

    def setHeadersWithDict(self, headersDict):
        self.Headers.update(headersDict)

    def setHeaders(self, argument, value):
        self.Headers[argument] = value

    def setChannelHeadersWithDict(self, headersDict):
        self.channelHeaders.update(headersDict)

    def setChannelHeaders(self, argument, value):
        self.channelHeaders[argument] = value

    def additionalHeaders(self, source, newSource):
        headerList={}
        headerList.update(source)
        headerList.update(newSource)
        return headerList

    def optionsContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.options(url, headers=headers, data=data)

    def postContent(self, url, data=None, files=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.post(url, headers=headers, data=data, files=files)

    def getContent(self, url, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.get(url, headers=headers, stream=True)

    def deleteContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.post(url, headers=headers, data=data)

    def putContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.put(url, headers=headers, data=data)