from image_scrapper.scrapper import Scrapper
from CNN.callback import Call_back
from CNN import model
# from CNN import predict
from CNN import generate_data

# Web Scrapper
scrape = Scrapper()
fruit_list=['apple_fruit', 'banana', 'grapes', 'tomato']
for fr in fruit_list:
    scrape.search_and_download(search_term=fr, target_path='D:/Strive/Mini-Projects/TF-image-classifier-app/images', number_images=30 )

# Data Generator
calls = Call_back()
gen_data = generate_data.GenerateData()
train_data, test_data = gen_data.datagen(dir_path='D:/Strive/Mini-Projects/TF-image-classifier-app/images')
model = model.model_training(training_set=train_data, testing_set=test_data, calls=calls)

# pending prediction part
# reduce batch size to prevent memory warnings
