import scrapy

def checkVerified(data):
	verified_str = data.xpath('.//span[@data-hook="avp-badge"]/text()').extract()
	return "Verified Purchase" in verified_str

def extractComment(data):
	comment_str = data.xpath('.//span[@data-hook="review-body"]/span/text()').extract()
	return comment_str[0].strip('\n ')

def extractStarRating(data):
	rating_str = data.xpath('.//i[@data-hook="review-star-rating"]/span/text()').extract()
	rating_int = int(rating_str[0][0])
	return rating_int

def extraxtProductName(data):
    name_str = data.xpath('.//a[@data-hook="product-link"]/text()').extract()
    return name_str

class AmazonReviewDistSpider(scrapy.Spider):
    name = 'amazon_review_dist'
    allowed_domains = ['amazon.com']
    
    baseURL = 'https://www.amazon.com/Gosund-Compatible-Required-appliances-Certified/product-reviews/B079MFTYMV/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2'
    start_urls = [baseURL]


    def parse(self, response):
        data = response.css('#histogramTable')  
        stars = data.xpath('.//div[@class="a-meter"]/@aria-label').extract()
        product_name = extraxtProductName(response)

        yield{'5stars': stars[0].strip('%'),
        '4stars': stars[1].strip('%'),
        '3stars': stars[2].strip('%'),
        '2stars': stars[3].strip('%'),
        '1stars': stars[4].strip('%'),
        'product_name': product_name}

