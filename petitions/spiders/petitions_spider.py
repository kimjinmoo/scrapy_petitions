import scrapy
from scrapy.selector import Selector

class PetitionsSpider(scrapy.Spider):
  name = "petitions"
  def start_requests(self):
    urls = [
      'https://www1.president.go.kr/petitions',
    ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    #filename = 'crawling.json'
    select = Selector(response)

    for s in select.css('div ul.petition_rank li'):
      self.log('xpath %s' % s)
      for sub in s.css('li'):
        self.log('test')

    # for s in response.xpath("/html[@class='js csstransitions']/body/div[@id='wrap']/div[@id='contents']/section[@id='cont_view']/div[@class='cs_area']/div[@class='cs_body']/div[@class='wrap']/div[@class='ct_petitions']/div[@class='ct_petitions_area ct_txt_left']/div[@class='ct_list']/div[@class='board text']/div[@class='b_list category b_list2']/div[@class='bl_body']/ul[@class='petition_rank']/li"):
    #   self.log('selected : %s' % s.xpath("/div[@class='bl_wrap']/div[@class='bl_subject']/a[@class='cb relpy_w']").get())
    # with open(filename, 'wb') as f:
    #   f.write(response.body)
