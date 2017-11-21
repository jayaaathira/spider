# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AlleventsPipeline(object):
    def process_item(self, item, spider):
        return item
	"""ITEM_PIPELINES = {
  'scrapy.pipelines.images.ImagesPipeline': 1
}
IMAGES_STORE = 'tmp/images/DownloadFirstImg.csv'"""
