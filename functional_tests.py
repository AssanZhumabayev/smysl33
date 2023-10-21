from selenium import webdriver
import unittest

class BasicInstalltest(unittest.TestCase):
    # zhil byl Arman
    # Assan rabotaet developerom v TechOrda
    # odnazhdy Assan hotel prokachat svoi navyki v java
    # Assan zashel v Google, i vvel zapros java dlya prodvinutyh
    # zashel po odnoi iz ssylok

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        # v brauzere Arman otkrylsa sait (po adressu ...)
        # v zagolovke saite Arman prochital (sait Assana Zhumabayeva)
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Сайт Асана Жумабаева',self.browser.title)

    def test_home_page_header(self):
        # v shapke saita napisano Assan Zhumabayev
        browser = self.browser.get('http://127.0.0.1:8000')
        header = browser.find_elements_by_tag_name('h1')[0]
        self.assertIn('Асан Жумабаев',header)


if __name__ == '__main__':
    unittest.main()

# self.fail("Finish the test")


# pod shapkoi raspolozhen bolg so statiami
# u kazhdoi stati est' zagolovok i odin abzac s tekstom
# Aeman kliknul po zagolovku i u nego otkrylsya stranica s polnym tektom statii
# prochitav statiu Assan kliknul po tekstu Assanzhumabayev v  shapke stranicy i popal v glavnuiu statiu

