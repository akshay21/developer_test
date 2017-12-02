#import libraries
import urllib
import  urllib2

from bs4 import BeautifulSoup

import  pandas as pd
import  csv
#specify the url
ifp_blog="http://ifpartners.com/cut-the-wire"

req =urllib2.Request(ifp_blog, headers={'User-Agent' : 'Mozilla/5.0'})

page = urllib2.urlopen(req)

soup = BeautifulSoup(page, 'html.parser')

data=[]

section=soup.find('section')
imgs= soup.find_all('img', attrs={'class': "attachment-post-thumbnail size-post-thumbnail wp-post-image"})
img_links =[each.get('src') for each in imgs]
for each in img_links:
    print each
    reqs= urllib2.Request(each, headers={'User-Agent' : 'Mozilla/5.0',
                                                               'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"})
    try:
        images=urllib2.urlopen(each)
        filename = each.split('/')[-1]
        print filename
    except urllib2.HTTPError, e:
        print e
        #urllib.urlretrieve(each, filename)

# articles=soup.find_all('article')
# for i in range(0,6):
#     blog = []
#     article= articles[i]
#     title = article.find('header').find('h2').find('a').text.encode('ascii','ignore')
#     updateTime=article.find('time', attrs={'class' : 'updated'})['datetime']
#     author = article.find('p').find('a').text
#     content= article.find('div', attrs={'class' : 'entry-content'})
#     bannerImg= imgs[i]['src']
#
#     blog.extend((title, updateTime,author,content,bannerImg))
#     data.append(blog)
    # print "Title ", title
    # print "Author ", author
    # print "updated time ", updateTime
    # print "Image href ", bannerImg
    # #print "Content ", content
    # print "*************************************************************************************************"

# df = pd.DataFrame(data, columns=["Title","Author","Updated Time","Content", "Image href"])
# df.to_csv('ofile.csv', index=False)
# with open("ofile.csv", 'wb') as outcsv:
#     writer = csv.writer(outcsv, lineterminator='\n', quoting=csv.QUOTE_ALL)
#     for d in data:
#         writer.writerow(d)








# articles=soup.find_all('article')
#
# article= articles[0]
# updateTime=article.find('time', attrs={'class' : 'updated'})
# title = article.find('header').find('h2').find('a').text
# author = article.find('p').find('a').text
# content= article.find('div', attrs={'class' : 'entry-content'})
#
#
# print "Title ", title
# print "Author ", author
# print "updated time ", updateTime
# print "Content ", content
# print "*************************************************************************************************"

