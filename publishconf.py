# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

AUTHOR = 'Filipa Calado'
SITENAME = 'Queer Tools: notes toward a dissertation'
SITEURL = 'https://gofilipa.github.io/qt'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Contact me:', 'mailto:filipa@princeton.edu'),
         ('Personal Website', 'https:www.filipacalado.com'))

# Social widget
SOCIAL = (('Github', 'https://github.com/gofilipa/'),
          ('Twitter', 'https://twitter.com/Caladoscope'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

## FC EDITs: 


## Customizing the navbar

DISPLAY_ARTICLES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
