""" For websites built on Drupal, there is a directory that holds all the
    added modules. This directory is often accessible via the site's URL.
    For example: https://www.drupal.org/sites/all/modules/
    This script takes a URL and a name of a file. The file contains a list
    of Drupal modules that the script will check if the specified website
    uses.
    usage: python moduleCheck.py url file

    Author: Trevor Yu
    Date: Nov. 26, 2015
    Email: trevor.tyu@gmail.com
"""
import urllib2,sys

modules = []
validModules = []

args = sys.argv

helpText = "usage: python moduleCheck.py url file"

host = None # The host URL to check whether or not the Drupal modules exist
moduleFile = None # A file that lists out all the Drupal modules

try:
    host = args[1]
    moduleFile = args[2]
except:
    print helpText
    sys.exit()

# Check if host URL is set
if host is None:
    print helpText
    print "Please enter a host URL"
    sys.exit()

# Check if the module file is set
if moduleFile is None:
    print helpText
    print "Please enter a file to use"
    sys.exit()

# Test host URL
try:
    content = urllib2.urlopen(url=host).read()
except ValueError:
    print "Improperly formatted host URL."
    print "URL should be like the following: https://www.drupal.org/sites/all/modules/"
    sys.exit()
except:
    pass
       
# Need to add slash to end if host URL doesn't have one
if host.endswith( "/" ) is False:
    host = host + "/"

print "Starting check..."

i = 0
with open( moduleFile ) as f:
    for module in f:
        module = module.replace( "\r\n", "" )
       
        testHost = host + module + "/"
        while True:
            try:
                content = urllib2.urlopen(url=testHost).read()
            except urllib2.HTTPError as e:
                if( "403" in str(e) ):
                    print module
                else:
                    print i
                i = i + 1
                break
            except urllib2.URLError as e:
                if( "Connection timed out" in str(e) ):
                    continue
