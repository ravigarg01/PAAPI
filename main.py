from amazon_paapi import AmazonApi

KEY = 'AKIAIH2INWASV3ZQPCWQ'
SECRET = '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'
TAG = 'rahulaggarw0c-21'
COUNTRY = 'IN'

# amazon = bottlenose.Amazon(AMAZON_ACCESS_KEY_ID, AMAZON_SECRET_ACCESS_KEY, AMAZON_ASSOC_TAG, Region='IN')
# response = amazon.ItemLookup(ItemId="9355612087")

amazon = AmazonApi(KEY, SECRET, TAG, COUNTRY)
item = amazon.get_items('9355612087')[0]
search = amazon.search_items(keywords='Examcart UPSC IAS Prelims (Civil Services) Topic-wise Solved Papers By AS Pandit Sir For 2024 Exam in English', search_index='KindleStore')
print(search)
print(item.item_info.title.display_value) # Item title
