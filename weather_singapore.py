#! /usr/local/bin/python
# -*- coding: utf-8 -*-
'''
Python script to print the weather info for singapore
'''
import os
from bs4 import BeautifulSoup
import urllib2

WEATHER_URL = 'https://sg.weather.yahoo.com/'
UNITS = u'\xb0C'

def main():
    html_doc = urllib2.urlopen(WEATHER_URL)
    soup = BeautifulSoup(html_doc, "html.parser")

    # current temp and description
    current_temp = soup.find("span", class_="Va(t)").text
    current_desc = soup.find("span", class_="description")

    # lets download the current weather icon to a temp location
    # u'https://s.yimg.com/os/weather/1.0.1/shadow_icon/60x60/thundershowers_day_night@2x.png'
    current_img_src = soup.find("img", class_="Trsdu(.42s)").get('src')
    tmp_image = os.path.join('/var', 'tmp', '.current_weather.png')
    with open(tmp_image, 'w') as fh:
        fh.write(urllib2.urlopen(current_img_src).read())

    # Details, for instance feels like, humidity, etc
    details = soup.find("div", class_="D(tbc) W(60%)")
    details_list = [x.text.encode('utf-8') for x in details.findChildren("div")]
    details_dict = dict(zip(details_list[0::2], details_list[1::2]))  

    # geeklet display
    print "{0}".format(current_desc.text.title()), 
    print "\t{0}".format(current_temp) + UNITS.encode('utf-8')
    print
    for key, value in details_dict.iteritems():
        print "\t{0}\t".format(key), value#.decode('utf-8')

if __name__ == '__main__':
    main()





