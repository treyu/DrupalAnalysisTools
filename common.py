import urllib2
import BeautifulSoup
from sets import Set

def get_html_string(url):
    """
    Gets the html string from a url
    :param url: (str) the url to get html from
    :returns: (str) the string representation of the html at a url
    """
    catcher = 0
    while(catcher <3):
        try:
            URLObj = urllib2.urlopen(url)
            html_string = URLObj.read().decode('utf-8')
            catcher=3
            return html_string
        except:
            print "Link retrieval error on:"
            print url
            html_string = ""
            catcher+=1
            if(catcher==3):
                return html_string
            else:
                print "Trying again"

def users_from_node(base_url):
    """
    Gets usernames from nodes page
    :param url: (str) the web url of a Drupal web site.  Please include 'http'(s)
    :returns: (list of str) of unique usernames from all traversable nodes
    """
    usernames = Set()
    
    # If last character in base_url is '/' then remove the '/'
    if base_url[-1] == "/":
        base_url = base_url[:-1]
   
    # add '/node' onto end of base_url and treat that combination as the new url 
    url=base_url+"/node"
    
    # Go through all node pages and collect usernames
    while True:
        # Usernames are in a span with class username
        node_soup = BeautifulSoup.BeautifulSoup(get_html_string(url))
        for tag in node_soup.findAll('span', {'class':'username'}):
            usernames.add(tag.string)
        
        # Find next page buttons
        next_node = None
        for tag in node_soup.findAll('a', href=True):
            if (tag.string == "next"):
                next_node = tag.get('href',None)
                break
        
        if not next_node:
            break
        else:
            url = base_url+next_node
    
    return list(usernames)


"""
Example use below.
Call for your own base url
"""
#users_from_node("https://bobsite.ca/")
