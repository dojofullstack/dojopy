# import os
import logging
from time import sleep
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait


# logging.basicConfig(level=logging.DEBUG)
#
# logging.debug("es una prueba debug")
# logging.info("es una prueba info")
# logging.warning("es una prub warning")
# logging.error("es una prueba error")
#
# try:
#     logging.info("iniciando funcion")
#     data = input('ingresa un numero')
#     print(data / 2)
# except Exception as e:
#     logging.error(f"es un error {e}")


USER_AGENT = """user-agent= Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gec
ko) Chrome/68.0.3440.84 Safari/537.36"""
window_resolution = '1280x1024'
WINDOW_SIZE = 'window-size={}'.format(window_resolution)
ALLOW_INSECURE = '--allow-running-insecure-content'
REDUCE_SECURITY = '--reduce-security-for-testing'
DISABLE_GPU = '--disable-gpu'
PREFERENCES = { "profile.default_content_setting_values.notifications" : 2 }
EXECUTABLE_PATH = '/usr/local/bin/chromedriver'
TIMEOUT = 180
TIMEOUT_ELEMENT = 20
WD_POSITION = '--window-position=0,0'
INFO_BARS = '--disable-infobars'
HEADLESS = '--headless'
KIOSK = '--kiosk' #modo f11
WD_MAX = '--start-maximized'


class BotFacebook(object):
    def __init__(self, user, pwd, active_login):
        self.active_login = active_login
        self.login_url = 'https://www.facebook.com/login'
        self.user = user
        self.password = pwd

    def start_chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument(USER_AGENT)
        options.add_argument(WINDOW_SIZE)
        options.add_argument(ALLOW_INSECURE)
        options.add_argument(REDUCE_SECURITY)
        options.add_argument(DISABLE_GPU)
        options.add_argument(WD_POSITION)
        options.add_argument(INFO_BARS)
        options.add_argument("--user-data-dir=/home/henry/app-data-browser/")   # setear ruta local path

        self.driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH, chrome_options=options)
        self.driver.set_page_load_timeout(TIMEOUT)
        self.driver.get(self.login_url)

    def start_session(self):
        if self.active_login is False:
            input_email =  self.driver.find_element_by_id('email')
            input_pass =  self.driver.find_element_by_id('pass')
            input_email.clear()
            input_email.send_keys(self.user)
            input_pass.clear()
            input_pass.send_keys(self.password)
            self.driver.find_element_by_id('loginbutton').click()
        else:
            print('sesion ya iniciada!')


    def config_grupo(self):
        with open('lista_grupos.txt') as target:
            lista = target.read().split('\n')
        self.publicar_en_grupos(lista)

    def publicar_en_grupos(self, lista):
        for url in lista:
            if 'facebook.com' in url:
                self.driver.get(url)
                sleep(3)
                # self.crear_post()
                self.upload_image()

        input("esperando algo")

    def crear_post(self):
        campo_post = self.driver.find_element_by_css_selector('.m9osqain.a5q79mjw.jm1wdb64.k4urcfbm')
        campo_post.click()

        sleep(3)

        campo_post2 = self.driver.find_elements_by_css_selector('.notranslate._5rpu')[1]
        campo_post2.send_keys("hola")
        sleep(1)
        buton_publicar = self.driver.find_element_by_css_selector('.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.g5gj957u.d2edcug0.hpfvmrgz.mg4g778l.buofh1pr.ph5uu5jm.b3onmgus.e5nlhep0.ecm0bbzt')
        buton_publicar.click()

    def upload_image(self):
        path_file = '/home/henry/Downloads/anuncio_tienda.mp4'
        campo_post = self.driver.find_element_by_css_selector('.m9osqain.a5q79mjw.jm1wdb64.k4urcfbm')
        campo_post.click()
        sleep(2)
        # campo_post2 = self.driver.find_elements_by_css_selector('.notranslate._5rpu')[1]
        # campo_post2.send_keys("hola")
        # sleep(1)
        btn_file = self.driver.find_elements_by_class_name('mkhogb32')
        btn_file[6].send_keys(path_file)
        # for i, value in enumerate(btn_file):
        #     try:
        #         print(f'value {i}', value)
        #         value.send_keys(path_file)
        #         sleep(1)
        #     except Exception as e:
        #         print(e)

        # btn_file = self.driver.find_elements_by_class_name('mkhogb32')[6]
        # btn_file.send_keys(path_file)
        # sleep(3)
        # buton_publicar = self.driver.find_elements_by_css_selector('.oajrlxb2.s1i5eluu.gcieejh5.bn081pho.humdl8nn.izx4hr6d.rq0escxv.nhd2j8a9.j83agx80.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.d1544ag0.qt6c0cv9.tw6a2znq.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.l9j0dhe7.abiwlrkh.p8dawk7l.beltcj47.p86d2i9g.aot14ch1.kzx2olss.cbu4d94t.taijpn5t.ni8dbmo4.stjgntxs.k4urcfbm.tv7at329')
        # buton_publicar[2].click()


obj = BotFacebook('hola@dojopy.com', '-', active_login=True)
obj.start_chrome()
obj.config_grupo()
# obj.start_session()
# obj.config_grupo()
