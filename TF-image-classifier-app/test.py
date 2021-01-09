from image_scrapper.scrapper import Scrapper

scrape = Scrapper()
fruit_list=['apple+fruit', 'banana', 'grapes', 'tomato', 'water melon']
for fr in fruit_list:
    scrape.search_and_download(search_term=fr, target_path='./images', number_images=10 )