import scrapy
from ..items import AmazonItem

class AmazonspiderSpider(scrapy.Spider):
    name = "amazonspider"
    allowed_domains = ["amazon.in"]
    page_number=2
    start_urls = ["https://www.amazon.in/s?k=books&ref=nb_sb_noss"]
    def parse(self, response):
        
        item=AmazonItem()
        item['product_name'] = response.css('.a-color-base.a-text-normal::text').extract()
        item['product_author'] = response.css('.a-color-secondary .s-link-style::text').extract()
        item['product_price'] = response.css('.a-price-whole::text').extract()
        item['product_imagelink'] = response.css('.s-image::attr(src)').extract()
        yield item
        
        next_page=f'https://www.amazon.in/s?k=books&page={AmazonspiderSpider.page_number}&qid=1698230683&ref=sr_pg_{AmazonspiderSpider.page_number}'
        if AmazonspiderSpider.page_number <=20:
            AmazonspiderSpider.page_number+=1
            yield response.follow(next_page,callback=self.parse)