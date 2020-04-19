
#(base) maeg-ui-MacBook-Air:spiders mac$ scrapy startproject kitapyurdu

#(base) maeg-ui-MacBook-Air:kitapyurdu mac$ scrapy shell "https://www.kitapyurdu.com/cok-satan-kitaplar/haftalik/1.html"
# request atip respond alacaz

#>>> response.css("div.name.ellipsis a span::text").extract()


#>>> response.css("div.publisher span a span::text").extract()

import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    pageCount = 0
    def start_requests(self):

        urls =  ["https://www.kitapyurdu.com/cok-satan-kitaplar/haftalik/1.html"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        book_names = response.css("div.name.ellipsis a span::text").extract()
        book_authors = response.css("div.author span a span::text").extract()
        book_publishers = response.css("div.publisher span a span::text").extract()

        i = 0

        while (i < len(book_names)):
            yield {
                "name" : book_names[i],
                "author" : book_names[i],
                "author" : book_authors[i],
                "publisher"  : book_publishers[i]
            }
            i+=1



            
