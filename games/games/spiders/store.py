import scrapy
from ..items import SteamItem
from scrapy.loader import ItemLoader


class StoreSpider(scrapy.Spider):
    name = "store"
    allowed_domains = ["store.steampowered.com"]
    start_urls = ["https://store.steampowered.com/"]

    def parse(self, response):
        games = response.css(".tab_content a.tab_item")

        for game in games:
            loader = ItemLoader(item=SteamItem(), selector=game, response=response)

            loader.add_css("game_name", '.tab_item_name::text')
            loader.add_xpath('game_url', './/@href')
            loader.add_xpath('image_url', ".//div[@class='tab_item_cap']/img/@src")
            loader.add_xpath('platforms', ".//span[contains(@class, 'platform_img') or @class='vr_supported']/@class")
            loader.add_xpath('discount_rate', './/div[@class="discount_block tab_item_discount"]//div[@class="discount_pct"]/text()')
            loader.add_xpath('original_price', './/div[@class="discount_original_price"]/text()')
            loader.add_xpath('final_price', './/div[@class="discount_final_price"]/text()')

            yield loader.load_item()
