# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecruitmentItem(scrapy.Item):
    # define the fields for your item here like:
    position = scrapy.Field()   # 职位名称
    href = scrapy.Field()   # 职位url
    category = scrapy.Field()   # 职位类别
    num = scrapy.Field()    # 人数
    location = scrapy.Field()   # 地址
    time = scrapy.Field()   # 发布时间
    responsibility = scrapy.Field()
    require = scrapy.Field()