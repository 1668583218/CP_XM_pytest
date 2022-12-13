from selenium import webdriver
import page
from tool.get_log import GetLogger

log = GetLogger.get_logger()


class GetDriver:
    # 设置类属性
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 设置谷歌对象
            chrome_options = webdriver.ChromeOptions()
            log.info('设置谷歌对象-无头浏览器')
            chrome_options.add_argument("--headless")
            # 尝试解决无头浏览器下无法下载文件
            prefs = {
                # 下载目录
                'download.default_directory': 'C:\\Users\\caojingwei\\Downloads',
                # 设置为0，禁止弹出窗口
                'profile.default_content_settings.popups': 0,
                'download.prompt_for_download': False,
                'download.directory_upgrade': True,
                'safebrowsing.enabled': False,
                'safebrowsing.disable_download_protection': True,
                'safebrowsing_for_trusted_sources_enabled': False
            }
            chrome_options.add_experimental_option('prefs', prefs)
            # 更改加载策略，缩短加载时间
            chrome_options.page_load_strategy = 'eager'
            # 设置浏览器分辨率，opt会导致maximize最大化失败
            log.info('设置浏览器分辨率')
            chrome_options.add_argument('--window-size=2560,1600')
            # 实例化浏览器
            log.info('实例化浏览器')
            cls.driver = webdriver.Chrome(chrome_options=chrome_options)
            # log.info('实例化driver对象')
            # cls.driver = webdriver.Chrome()
            # # 最大化
            # log.info('最大化浏览器')
            # cls.driver.maximize_window()
            # 打开浏览器
            log.info('打开网页')
            cls.driver.get(page.url)
        return cls.driver

    # 退出driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            # print("关闭之前：", cls.driver)
            log.info('关闭对象')
            cls.driver.quit()
            # print("关闭之后：", cls.driver)

            # 注意：此处有一个很大坑
            log.info('置空对象')
            cls.driver = None
            # print("置空之后：", cls.driver)


if __name__ == '__main__':
    # 第一次获取浏览器
    print(GetDriver().get_driver())
    # 第二次获取浏览器
    print(GetDriver().get_driver())
    # 调用关闭，测试 关闭后driver是否为None
    GetDriver().quit_driver()
    # print(GetDriver().get_driver())
