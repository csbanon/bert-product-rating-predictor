import scrapy

def checkVerified(data):
    verified_str = data.xpath('.//span[@data-hook="avp-badge"]/text()').extract()
    if "Verified Purchase" in verified_str:
        return 1
    else:
        return 0

def extractComment(data):
	new_data = data.css('.review-text-content')
	main_comment_str = new_data.xpath('.//span/text()').extract()
	sub_comment_str = new_data.xpath('.//span/text()[preceding-sibling::br]').extract()
	if not sub_comment_str:
		return main_comment_str[0].strip()
	else:
		return main_comment_str[0].strip() + sub_comment_str[0].strip()

def extractStarRating(data):
    new_data = data.css('.review-rating')
    rating_str = new_data.xpath('.//span/text()').extract()
    rating_int = int(rating_str[0][0])
    return rating_int

def extractDate(data):
    date_str = data.xpath('.//span[@data-hook="review-date"]/text()').extract()
    date_str = date_str[0]
    if "January" in date_str:
        month = 1
        string_tuple = date_str.partition("January")
    elif "February" in date_str:
        month = 2
        string_tuple = date_str.partition("February")
    elif "March" in date_str:
        month = 3
        string_tuple = date_str.partition("March")
    elif "April" in date_str:
        month = 4
        string_tuple = date_str.partition("April")
    elif "May" in date_str:
        month = 5
        string_tuple = date_str.partition("May")
    elif "June" in date_str:
        month = 6
        string_tuple = date_str.partition("June")
    elif "July" in date_str:
        month = 7
        string_tuple = date_str.partition("July")
    elif "August" in date_str:
        month = 8
        string_tuple = date_str.partition("August")
    elif "September" in date_str:
        month = 9
        string_tuple = date_str.partition("September")
    elif "October" in date_str:
        month = 10
        string_tuple = date_str.partition("October")
    elif "November" in date_str:
        month = 11
        string_tuple = date_str.partition("November")
    elif "December" in date_str:
        month = 12
        string_tuple = date_str.partition("December")

    day_year_tuple = string_tuple[2].partition(',')
    day = int(day_year_tuple[0].strip())
    year = int(day_year_tuple[2].strip())
    date = "{}-{}-{}"
    return date.format(year,month,day)

def extractHelpful(data):
    helpful_str = data.xpath('.//span[@data-hook="helpful-vote-statement"]/text()').extract()
    if not helpful_str:
    	return 0
    elif "One" in helpful_str[0]:
    	return 1
    else:
    	return helpful_str[0][0]

def extractCountry(data):
    country_str = data.xpath('.//span[@data-hook="review-date"]/text()').extract()
    if "United States" in country_str[0]:
        return 1
    else:
        return 0

def extractHasMedia(data):
	new_data = data.css('.review-image-container')
	media_str = new_data.xpath('.//div/text()').extract()
	if not media_str:
		return 0
	else:
		return 1

class AmazonReviewSpider(scrapy.Spider):
    name = 'amazon_review'
    allowed_domains = ['amazon.com']
    
    baseURL = 'https://www.amazon.com/Gosund-Compatible-Required-appliances-Certified/product-reviews/B079MFTYMV/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='
    start_urls = []

    for i in range(1,501):
    	start_urls.append(baseURL+str(i))

    def parse(self, response):
        data = response.css('.review')   

        for review in data:
            #print("-----------------------------------------------" + review.extract())
            yield{'comment': extractComment(review),
            'stars': extractStarRating(review),
            'verified': checkVerified(review),
            'date': extractDate(review),
            'country': extractCountry(review),
            'helpful': extractHelpful(review),
            'has-media': extractHasMedia(review)}

