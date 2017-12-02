#import libraries

import  urllib2

from bs4 import BeautifulSoup

import  pandas as pd

#specifying the url
ifp_blog="http://ifpartners.com/cut-the-wire"

req =urllib2.Request(ifp_blog, headers={'User-Agent' : " Magic Browser"})

page = urllib2.urlopen(req)

soup = BeautifulSoup(page, 'html.parser')

data=[]

#collecting images and articles in list
section=soup.find('section')

imgs= soup.find_all('img', attrs={'class': "attachment-post-thumbnail size-post-thumbnail wp-post-image"})

articles=soup.find_all('article')

#looping over the list to extract desired details: Title, Updated Time, Author, Content and Banner href
for i in range(0,6):
    blog = []
    article= articles[i]
    title = article.find('header').find('h2').find('a').text.encode('ascii','ignore')
    updateTime=article.find('time', attrs={'class' : 'updated'})['datetime']
    author = article.find('p').find('a').text
    content= article.find('div', attrs={'class' : 'entry-content'})
    bannerImg= imgs[i]['src']
    blog.extend((title, updateTime,author,content,bannerImg))
    data.append(blog)

#exporting the data to csv
df = pd.DataFrame(data, columns=["Title","Author","Updated Time","Content", "Image href"])
df.to_csv('ofile.csv', index=False)


