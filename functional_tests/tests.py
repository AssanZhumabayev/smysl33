from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from blog.models import Article
from datetime import datetime
import pytz
import os


class BasicInstalltest(LiveServerTestCase):
    # zhil byl Arman
    # Assan rabotaet developerom v TechOrda
    # odnazhdy Assan hotel prokachat svoi navyki v java
    # Assan zashel v Google, i vvel zapros java dlya prodvinutyh
    # zashel po odnoi iz ssylok

    def setUp(self):
        self.browser = webdriver.Chrome()
        staging_server = os.environ.get('STAGING_SERVER')  
        if staging_server:
            self.live_server_url = 'http://' + staging_server
        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full_text 1',
            pubdate=datetime.utcnow().replace(tzinfo=pytz.utc),
            slug="ooo"
        )

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        # v brauzere Arman otkrylsa sait (po adressu ...)
        # v zagolovke saite Arman prochital (sait Assana Zhumabayeva)
        self.browser.get(self.live_server_url)
        self.assertIn('Сайт Асана Жумабаева', self.browser.title)

    def test_home_page_header(self):
        # Открываем страницу
        self.browser.get(self.live_server_url)
        # Находим элемент с тегом 'h1' (заголовок) на странице
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        # Проверяем, содержит ли заголовок ожидаемый текст
        self.assertIn('Асан Жумабаев', header.text)

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        footer = self.browser.find_element(By.CLASS_NAME, "footer")
        self.assertTrue(footer.location['y'] > 600
        )

    def test_home_page_blog(self):
        # pod shapkoi raspolozhen bolg so statiami
        self.browser.get(self.live_server_url)
        article_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(article_list)

    def test_home_page_blog_has_articles_look_correct(self):
        # u kazhdoi stati est' zagolovok i odin abzac s tekstom
        self.browser.get(self.live_server_url)
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_summary = self.browser.find_element(By.CLASS_NAME, 'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

    def test_home_page_article_title_link_leads_to_article_page(self):
        # Arman kliknul po zagolovku i u nego otkrylsya stranica s polnym tektom statii
        # open home page
        self.browser.get(self.live_server_url)
        # search article
        #  head
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_title_text = article_title.text
        # search link into head
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        # go into link
        self.browser.get(article_link.get_attribute('href'))
        # We expect that there is an article on the page that opens
        article_page_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        self.assertEquals(article_title_text, article_page_title.text)

# self.fail("Finish the test")

# assan popytalsya otkryr nesushestvuiu statiu, emu otkrilas stranica 404
# prochitav statiu Assan kliknul po tekstu Assanzhumabayev v  shapke stranicy i popal v glavnuiu statiu


#
# nekotorye articles v adminke, no ne opublikovany
