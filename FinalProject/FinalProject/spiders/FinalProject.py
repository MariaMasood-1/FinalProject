import scrapy
from ..items import FinalprojectItem

class Final_Project(scrapy.Spider):  #inheriting from already written class in spider
    name = 'projects'
    start_urls = [
        'https://coronalenergy.com/solar-portfolio/?tag=Utility%20Scale'
    ]
    def parse(self, response):

        items = FinalprojectItem()

        content_information = response.css('div.col.col-1')
        for data in content_information:

            title = data.css('h4.textdiv_title::text').extract()
        new_content_information = response.css('div.col.col-1')

        for data2 in new_content_information:

            capacity = data2.css('li.biz-icon-location').extract()
            for x in data2:
                capacity = x.css('div.textdiv_data2::text').extract()


            items['title'] = title
            items['capacity'] = capacity

            yield items      #the source code from the url will be held in response. response contains the source code of our website

