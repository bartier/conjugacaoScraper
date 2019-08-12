# -*- coding: utf-8 -*-
import scrapy


class VerbsSpider(scrapy.Spider):
    name = 'verbs'

    allowed_domains = [
        'conjugacao.com.br'
    ]

    def start_requests(self):
        urls = ['https://www.conjugacao.com.br/verbos-populares/1/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        self.log(f'Current page: {page}')

        next_page = response.xpath('//div[@class="paginacao"]/a[@class="nav"][last()]/@href').get()
        self.log(f'Next page: {next_page}')

        verbs = response.xpath('//div[@class="wrapper"]/ul//li/a//text()').extract()

        for verb in verbs:
            yield {
                'verb': verb
            }

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
