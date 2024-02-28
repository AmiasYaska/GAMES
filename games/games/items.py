# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# from scrapy.loader.processors import TakeFirst, MapCompose
from itemloaders.processors import TakeFirst, MapCompose

def get_platforms(one_class):
    platforms = []

    platform = one_class.split(" ")[-1]

    if platform == "win":
        platforms.append("Windows")
    if platform == "mac":
        platforms.append("MacOS")
    if platform == "linux":
        platforms.append("Linux")
    if platform == "vr_supported":
        platforms.append("VR Supported")
    return platforms


def discount(rate):
    if rate:
        return rate.lstrip("-")
    else:
        return "0"


def price(final):
    if final:
        return final
    else:
        return "FREE"


def original(last):
    if last:
        return last
    else:
        return "-"


class SteamItem(scrapy.Item):
    game_name = scrapy.Field(
        output_processor=TakeFirst()
    )
    game_url = scrapy.Field(
        output_processor=TakeFirst()
    )
    image_url = scrapy.Field(
        output_processor=TakeFirst()
    )
    platforms = scrapy.Field(
        input_processor=MapCompose(get_platforms)
    )
    discount_rate = scrapy.Field(
        input_processor=MapCompose(discount),
        output_processor=TakeFirst()

    )
    original_price = scrapy.Field(
        input_processor=MapCompose(original),
        output_processor=TakeFirst()
    )
    final_price = scrapy.Field(
        input_processor=MapCompose(price),
        output_processor=TakeFirst()
    )
