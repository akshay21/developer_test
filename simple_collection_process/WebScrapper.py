#import libraries

import  urllib2

from bs4 import BeautifulSoup

#specify the url
ifp_blog="http://ifpartners.com/cut-the-wire"

req =urllib2.Request(ifp_blog, headers={'User-Agent' : " Magic Browser"})

page = urllib2.urlopen(req)

soup = BeautifulSoup(page, 'html.parser')

#print soup.prettify()

#attachment-post-thumbnail size-post-thumbnail wp-post-image

articles=soup.find_all('article')
for i in range(6):
    article= articles[i]
    updateTime=article.find('time', attrs={'class' : 'updated'})
    title = article.find('header').find('h2').find('a').text
    author = article.find('p').find('a').text
    content= article.find('div', attrs={'class' : 'entry-content'})


    print "Title ", title
    print "Author ", author
    print "updated time ", updateTime
    print "Content ", content
    print "*************************************************************************************************"
