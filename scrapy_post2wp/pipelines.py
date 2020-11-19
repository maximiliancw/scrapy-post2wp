import base64
from urllib.parse import urljoin
import requests


class Post2WordPress(object):
    """
    Creates WordPress posts from scraped items using the built-in REST API

    Settings:
        - WP_BASE_URL:  base url of your WordPress instance, i.e. https://mysite.com
        - WP_USERNAME:  username (recommended: create a dedicated user with 'author' privileges)
        - WP_APP_PWD:   application password (use this plugin: https://de.wordpress.org/plugins/application-passwords)

    An item must contain the fields "title" and "content", check items.py for all available fields

    """

    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url
        self.username = username
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings.get('WP_BASE_URL'),
            crawler.settings.get('WP_USERNAME'),
            crawler.settings.get('WP_APP_PWD')
        )

    def process_item(self, item, spider):
        # Enable for every spider per default
        enabled = spider.send_to_wp if hasattr(spider, 'send_to_wp') else True
        if enabled:
            if 'title' in item and 'content' in item:
                url = urljoin(self.base_url, '/wp-json/wp/v2/posts')
                # Encode authentication data
                token = base64.b64encode((self.username + ':' + self.password).encode('ascii'))
                headers = {'Authorization': 'Basic ' + token.decode('ascii')}
                response = requests.post(url, headers=headers, json=dict(item))
                if response.status_code != 201:
                    raise Exception(response.text)

        return item

