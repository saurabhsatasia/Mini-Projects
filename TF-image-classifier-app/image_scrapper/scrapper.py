import os
import time
import requests
from selenium.webdriver import ChromeOptions, Chrome

class Scrapper:
    def __init__(self):
        self.driver_path = 'D:\Strive\Mini-Projects\TF-image-classifier-app\image_scrapper\chromedriver.exe'
        self.driver = ChromeOptions()
        # self.browser = Chrome()

    def init_driver(self):
        path = self.driver_path
        self.driver.add_argument('--disable-extensions')
        self.driver.add_argument('--profile-directory=Default')
        self.driver.add_argument('--incognito')
        self.driver.add_argument('--disable-plugins-discovery')
        # self.driver.add_argument('--start-maximized')
        self.browser = Chrome(executable_path=path, options=self.driver)
        return self.browser

    def fetch_image_urls(self, query:str, max_links_to_fetch:int, wd, sleep_between_interactions:int = 1):
        self.max_links_to_fetch = max_links_to_fetch
        self.query = query
        def scroll_to_end(wd):
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(sleep_between_interactions)
        # build the google query
        self.search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
        # load the page
        wd.get(self.search_url.format(q=self.query))
        self.image_urls = set()
        self.image_count = 0
        self.results_start = 0
        while self.image_count < self.max_links_to_fetch:
            scroll_to_end(wd)
            # get all image thumbnail results
            self.thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
            self.number_results = len(self.thumbnail_results)
            print(f"Found: {self.number_results} search results. Extracting links from {self.results_start}:{self.number_results}")

            for img in self.thumbnail_results[self.results_start : self.number_results]:
                # try to click every thumbnail such that we can get the real image behind it
                try:
                    img.click()
                    time.sleep(sleep_between_interactions)
                except Exception:
                    continue
                # extract image urls
                self.actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
                for actual_image in self.actual_images:
                    if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                        self.image_urls.add(actual_image.get_attribute('src'))
                self.image_count = len(self.image_urls)
                if len(self.image_urls) >= self.max_links_to_fetch:
                    print(f"Found: {len(self.image_urls)} image links, done!")
                    break

            else:
                print("Found:", len(self.image_urls), "image links, looking for more ...")
                time.sleep(30)
                return
                self.load_more_button = wd.find_element_by_css_selector(".mye4qd")
                if self.load_more_button:
                    wd.execute_script("document.querySelector('.mye4qd').click();")
            # move the result startpoint further down
            results_start = len(self.thumbnail_results)
        return self.image_urls

    def persist_image(self,folder_path:str, url:str, counter):
        try:
            image_content = requests.get(url).content
        except Exception as e:
            print(f"ERROR - Could not download {url} - {e}")
        try:
            f = open(os.path.join(folder_path, 'jpg' + "_" + str(counter) + ".jpg"), 'wb')
            f.write(image_content)
            f.close()
            print(f"SUCCESS - saved {url} - as {folder_path}")
        except Exception as e:
            print(f"ERROR - Could not save {url} - {e}")

    def search_and_download(self, search_term: str, target_path='./images', number_images=10):
        target_folder = os.path.join(target_path, '_'.join(search_term.lower().split(' ')))

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        scrape = Scrapper()
        with scrape.init_driver() as wd:
            res = scrape.fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=1)

        counter = 0
        for elem in res:
            scrape.persist_image(target_folder, elem, counter)
            counter += 1
