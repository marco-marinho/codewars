import re

def domain_name(url: str):
    http = re.compile(r"((https|http)://)?(?:www\.)?")
    url = re.sub(http, '', url)
    return url[:url.find(".")]