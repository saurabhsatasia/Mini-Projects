import os
import time
import requests
from selenium import webdriver


def fetch_image_urls(name:str, max_links_to_fetch:int, wd:webdriver, sleep_bt_interactions:int = 1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_bt_interactions)

    search_url = 'https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img'
    wd.get(search_url.format(q=name))
    img_urls = set()
    img_count=0
    res_start = 0
    while img_count < max_links_to_fetch:
        scroll_to_end(wd)


        # get all the image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector('img.Q4LuWd') # img tag class name:Q4LuWd
        number_results = len(thumbnail_results)

        print(f'Found: {number_results} search results. Extracting links from {res_start}:{number_results}')

        for img in thumbnail_results[res_start:number_results]:
            try:
                img.click()
                time.sleep(sleep_bt_interactions)
            except Exception:
                continue

            # extract image urls
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    img_urls.add(actual_image.get_attribute('src'))

            img_count=(len(img_urls))
            if len(img_urls) >= max_links_to_fetch:
                print(f"Found: {len(img_urls)} image links, DONE!")
                break

        else:
            print("Found", len(img_urls), 'image links, looking for more .. . . ')
            time.sleep(30)
            return
            load_more_button = wd.find_elements_by_css_selector('.mye4qd')
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4d').click();")

        res_start = len(thumbnail_results)

    return img_urls

def persist_img(folder_path:str, url:str, counter):
    try:
        image_content = requests.get(url).content
    except Exception as e:
        print(f"ERROR - COuld not download {url} - {e}")

    try:
        f = open(os.path.join(folder_path, 'jpg' + '_' + str(counter) + ".jpg"), 'wb')
        f.write(image_content)
        f.close()
        print(f"SUCCESS - saved {url} - as {folder_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")


def search_and_download(search_term: str, driver_path: str, num_of_images=10, target_path='./images'):
    target_folder = os.path.join(target_path,'_'.join(search_term.lower().split(' ')))
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=driver_path) as wd: # opens just chrome browser with blank page
        output = fetch_image_urls(search_term, num_of_images, wd=wd, sleep_bt_interactions=0.5) #time interval 0.5miliseconds wait between each images

    counter=0
    for elem in output:
        persist_img(target_folder, elem, counter)
        counter+=1


DRIVER_PATH = './chromedriver'
search_term = 'dog'
# num of images you can pass it from here  by default it's 10 if you are not passing
number_images = 40
search_and_download(search_term=search_term, driver_path=DRIVER_PATH, num_of_images=number_images)
