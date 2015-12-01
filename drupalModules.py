""" Creates a list of all possible Drupal modules by parsing each of the
    Drupal modules pages.
    usage: python drupalModules.py > modules.txt
    
    Author: Trevor Yu
    Date: Nov. 26, 2015
    Email: trevor.tyu@gmail.com
"""
import urllib2,sys
from HTMLParser import HTMLParser

class MyHTMLParser( HTMLParser ):
    modules = []
    isH2 = False
    isA = True
    def handle_starttag( self, tag, attrs ):
        if tag == "h2":
            self.isH2 = True
        elif tag == "a":
            self.isA = True
            if self.isH2 and self.isA:
                for name, value in attrs:
                    if name == "href":
                        print value
                        break
            
    def handle_endtag( self, tag ):
        if tag == "h2":
            self.isH2 = False
        elif tag == "a":
            self.isA = False
            
    def handle_data( self, data ):
        if self.isH2 and self.isA:
            self.modules.append( data )

parser = MyHTMLParser()

# Get all the Drupal modules
pageNum = 0
host = "https://www.drupal.org/project/project_module"
print pageNum
try:
    content = urllib2.urlopen(url=host).read()
except urllib2.HTTPError as e:
    None
parser.feed( content )

page = "?page="
maxPage = 1302

for pageNum in range( 1, maxPage ):
    host = "https://www.drupal.org/project/project_module" + page + str(pageNum)
    print pageNum
    try:
        content = urllib2.urlopen(url=host).read()
    except urllib2.HTTPError:
        continue

    content = unicode( content, errors='ignore' )
    parser.feed( content )
