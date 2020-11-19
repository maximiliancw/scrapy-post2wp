import scrapy


class WPPost(scrapy.Item):
    title = scrapy.Field()                      # required
    content = scrapy.Field()                    # required
    date = scrapy.Field(default=None)           # Publication date (if set, WP will adopt this date)
    excerpt = scrapy.Field(default='')
    categories = scrapy.Field(default=None)     # List of category IDs
    tags = scrapy.Field(default=None)           # List of tag IDs
