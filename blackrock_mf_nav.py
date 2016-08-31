#! /usr/local/bin/python

import urllib2
from bs4 import BeautifulSoup
import pprint

# the blackrock fund url
bgf_url = 'https://www.blackrock.com/sg/en/products/256058/bgf-global-multi-asset-income-fund-a6-sgd-hedged'

def main():
    html_doc = urllib2.urlopen('http://www.bloomberg.com/quote/BGMAA6S:LX')
    soup = BeautifulSoup(html_doc, "html.parser")

    fields = {}
    fields['fund_name'] = soup.find("div", class_='ticker').text
    fields['fund_value'] = soup.find("div", class_='price').text
    
    pprint.pprint("{0} {1}".format(fields['fund_name'].strip(), fields['fund_value']), width=4)

if __name__ == '__main__':
    main()
