

#python3 -m venv venv
import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"


    start_urls=[
    "https://blog.scrapinghub.com/"
    ]
    def parse(self,response):
        for post in response.css('div.post-item'):

            yield{
                'title':post.css('.post-header h2 a::text')[0].get(),
                'data':post.css('.post-header a::text')[1].get(),
                'author':post.css('.post-header a::text')[2].get()
            }


        next_page = response.css('a.next-posts-link::attr(href)').get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)




#response.css('h3::text').getall()
#response.css('h3::text')[2].get()
#response.css('title::text').get()
#response.css('.post-header a::text')[1].get()
#response.css('p::text').re(r'scraping')
#response.css('p::text').re(r's\w+')
#response.xpath('//h3')
#response.xpath('//*[@id="hs_cos_wrapper_module_1523032069834331"]/div/div/div/div/div[1]/div[2]/div[2]/div/span[2]/a').extract()
#response.xpath('//*[@id="hs_cos_wrapper_module_1523032069834331"]/div/div/div/div/div[1]/div[2]/div[2]/div/span[2]/a/text()').extract()
#post = response.css('div.post-item')[0]
#title = post.css('.post-header h2 a::text')[0].get()


'''for post in response.css('div.post-item'):
...     title = post.css('.post-header h2 a::text')[0].get()

...     data  = post.css('.post-header a::text')[1].get()
...     author = post.css('.post-header a::text')[2].get()
...     print(dict(title=title,data=data,author=author))'''
