# -*- coding: utf-8 -*-
import json
from datetime import datetime
from waybackpy.exceptions import TooManyArchivingRequests, ArchivingNotAllowed, PageNotSaved, ArchiveNotFound, UrlNotFound, BadGateWay, InvalidUrl
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
    hdr = { 'User-Agent' : '%s' % UA } #nosec
    req = Request(request_url, headers=hdr) #nosec
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

def get(url,encoding=None,UA=default_UA):
    hdr = { 'User-Agent' : '%s' % UA }
    request_url = clean_url(url)
    req = Request(request_url, headers=hdr) #nosec
    resp=urlopen(req) #nosec
    if encoding is None:
        try:
            encoding= resp.headers['content-type'].split('charset=')[-1]
        except AttributeError:
            encoding = "UTF-8"
    return resp.read().decode(encoding)

def wayback_timestamp(year,month,day,hour,minute):
    year = str(year)
    month = str(month).zfill(2)
    day = str(day).zfill(2)
    hour = str(hour).zfill(2)
    minute = str(minute).zfill(2)
    return (year+month+day+hour+minute)

def near(
    url,
    year=datetime.utcnow().strftime('%Y'),
    month=datetime.utcnow().strftime('%m'),
    day=datetime.utcnow().strftime('%d'),
    hour=datetime.utcnow().strftime('%H'),
    minute=datetime.utcnow().strftime('%M'),
    UA=default_UA,
    ):
    timestamp = wayback_timestamp(year,month,day,hour,minute)
    request_url = "https://archive.org/wayback/available?url=%s&timestamp=%s" % (clean_url(url), str(timestamp))
    hdr = { 'User-Agent' : '%s' % UA }
    req = Request(request_url, headers=hdr) # nosec
    response = urlopen(req) #nosec
    data = json.loads(response.read().decode("UTF-8"))
    if not data["archived_snapshots"]:
        raise ArchiveNotFound("'%s' is not yet archived." % url)

    archive_url = (data["archived_snapshots"]["closest"]["url"])
    return archive_url

def oldest(url,UA=default_UA,year=1994):
    return near(url,year=year,UA=UA)

def newest(url,UA=default_UA):
    return near(url,UA=UA)
