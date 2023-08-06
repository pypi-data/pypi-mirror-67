# -*- coding: utf-8 -*-
from datetime import datetime
from waybackpy.exceptions import *
try:
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import Request, urlopen, HTTPError


default_UA = "waybackpy python package"

def clean_url(url):
    return str(url).strip().replace(" ","_")

def save(url,UA=default_UA):
    base_save_url = "https://web.archive.org/save/"
    request_url = (base_save_url + clean_url(url))
    hdr = { 'User-Agent' : '%s' % UA }
    req = Request(request_url, headers=hdr)
    if "." not in url:
        raise InvalidUrl("'%s' is not a vaild url." % url)
    try:
        response = urlopen(req) #nosec
    except HTTPError as e:
        if e.code == 502:
            raise BadGateWay(e)
        elif e.code == 429:
            raise TooManyArchivingRequests(e)
        elif e.code == 404:
            raise UrlNotFound(e)
        else:
          raise PageNotSaved(e)

    header = response.headers
    if "exclusion.robots.policy" in str(header):
        raise ArchivingNotAllowed("Can not archive %s. Disabled by site owner." % (url))
    archive_id = header['Content-Location']
    archived_url = "https://web.archive.org" + archive_id
    return archived_url

def near(
    url,
    year=datetime.utcnow().strftime('%Y'),
    month=datetime.utcnow().strftime('%m'),
    day=datetime.utcnow().strftime('%d'),
    hour=datetime.utcnow().strftime('%H'),
    minute=datetime.utcnow().strftime('%M'),
    UA=default_UA,
    ):
    timestamp = str(year)+str(month)+str(day)+str(hour)+str(minute)
    request_url = "https://archive.org/wayback/available?url=%s&timestamp=%s" % (clean_url(url), str(timestamp))
    hdr = { 'User-Agent' : '%s' % UA }
    req = Request(request_url, headers=hdr)
    response = urlopen(req) #nosec
    import json
    data = json.loads(response.read().decode('utf8'))
    if not data["archived_snapshots"]:
        raise ArchiveNotFound("'%s' is not yet archived." % url)
    
    archive_url = (data["archived_snapshots"]["closest"]["url"])
    return archive_url

def oldest(url,UA=default_UA,year=1994):
    return near(url,year=year,UA=UA)

def newest(url,UA=default_UA):
    return near(url,UA=UA)
