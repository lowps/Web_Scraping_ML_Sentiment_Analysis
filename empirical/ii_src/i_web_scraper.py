import sys 
import os
import traceback
from selenium import webdriver
from bs4 import BeautifulSoup

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.helper import get_directory_name
from utils.logger import Logger

abs_path = get_directory_name('/Users/ericklopez/Desktop/Web_scraping_ml_sentiment_analysis/empirical/src')
inspector_gadget = Logger(abs_path)

def scrape():
    driver = webdriver.Chrome()
    driver.get('https://www.amazon.com/Super-Smash-Bros-Ultimate-Nintendo-Switch/product-reviews/B01N5OKGLH/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2')







def main():
    scrape()


if __name__ =='__main__':
    main()
