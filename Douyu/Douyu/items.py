# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # �����ǳ�
    nickname = scrapy.Field()
    # ͼƬ����
    image_link = scrapy.Field()
    # ͼƬ���ر���
    image_paths = scrapy.Field()


class ImagespiderItem(scrapy.Item):
    imgurl = scrapy.Field()

