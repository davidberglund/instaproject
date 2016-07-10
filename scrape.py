#!/usr/bin/env python

f = open('instagram.html', 'r+')

htmlfile = f.read()
#print htmlfile

def get_body(htmlfile):
    start_link = htmlfile.find('<body')
    if start_link == -1: 
        return None, 0
    start_quote = htmlfile.find('"', start_link)
    end_quote = htmlfile.find('</body>', start_quote + 1)
    url = htmlfile[start_quote + 1:end_quote]
    return url, end_quote

def get_only_body(htmlfile):
    links = []
    while True:
        url,endpos = get_body(htmlfile)
        if url:
            links.append(url)
            htmlfile = htmlfile[endpos:]
        else:
            break
    return links

page = get_only_body(htmlfile)

pageStr = ''.join(page)

def get_next_target(page):
    start_link = page.find("""display_src": """)
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('?', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

pageStr = get_all_links(pageStr)
pageStr = ''.join(pageStr)
pageStr = pageStr.replace(":", "")

pageStr = pageStr.replace(" ", """" > <img src= """)
pageStr = pageStr.replace("https", "https:")

pageStr = pageStr+"""">"""
pageStr = pageStr[3:]
print pageStr