import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from tool.get_log import GetLogger
import time
from selenium.webdriver.common.keys import Keys

log = GetLogger.get_logger()


class Base:
    # 初始化
    def __init__(self, driver):
        log.info('初始化driver{}'.format(driver))
        self.driver = driver
        self.action = ActionChains(self.driver)

    # 查找元素方法 (提供：点击、输入、获取文本)使用
    def base_find_element(self, loc, timeout=30, poll=0.5):
        log.info('正在查找元素:{}'.format(loc))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    #
    # # 查找一组元素方法 (提供：点击、输入、获取文本)使用
    # def base_find_elements(self, loc, timeout=30, poll=0.5):
    #     log.info('正在查找元素组:{}'.format(loc))
    #     return WebDriverWait(self.driver,
    #                          timeout=timeout,
    #                          poll_frequency=poll).until(lambda x: x.find_elements(*loc))
    #
    # # 点击下拉框内的元素
    # def base_click_select(self, loc, value):
    #     log.info('正在查找并点击下拉框内的元素')
    #     list_loc = self.base_find_elements(loc)
    #     for i in list_loc:
    #         log.info(i.text)
    #         if value in i.text:
    #             i.click()
    #             log.info('找到了，点击完成')
    #             break
    #     log.error('没找到')

    # # 二次定位(用于下拉框)
    # def base_twice_find_element(self, loc, loc_son):
    #     return self.base_find_element(loc).base_find_element(loc_son)

    # 点击方法
    def base_click(self, loc):
        log.info('正在点击元素:{}'.format(loc))
        self.base_find_element(loc).click()

    # 键盘向下加回车方法
    def base_keys(self, loc):
        log.info('正在向下')
        self.base_find_element(loc).send_keys(Keys.DOWN)
        log.info('正在回车')
        self.base_find_element(loc).send_keys(Keys.ENTER)

    # # 下拉框点击
    # def base_twice_click(self, loc, loc_son):
    #     log.info('正在点击元素:{}的{}'.format(loc, loc_son))
    #     self.base_twice_find_element(loc, loc_son).click()

    # 输入方法
    def base_input(self, loc, value):
        log.info('准备给元素{}输入内容:{}'.format(loc, value))
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        log.info('正在给元素{}清空'.format(loc))
        # 输入
        el.send_keys(value)
        log.info('正在给元素{}输入内容:{}'.format(loc, value))

    # 导入文件输入方法
    def base_input_file(self, loc, value):
        log.info('准备给元素{}输入内容:{}'.format(loc, value))
        el = self.base_find_element(loc)
        # 输入
        el.send_keys(value)
        log.info('正在给元素{}输入内容:{}'.format(loc, value))

    # # 弹出框输入方法
    # def base_twice_input(self, loc, loc_son, value):
    #     log.info('准备给元素{}输入内容:{}'.format(loc_son, value))
    #     el = self.base_twice_find_element(loc, loc_son)
    #     # 清空
    #     el.clear()
    #     log.info('正在给元素{}清空'.format(loc_son))
    #     # 输入
    #     el.send_keys(value)
    #     log.info('正在给元素{}输入内容:{}'.format(loc_son, value))

    # 获取文本方法
    def base_get_text(self, loc):
        # 注意：一定要返回元素的文本信息
        log.info('正在获取元素{}的文本'.format(loc))
        return self.base_find_element(loc, timeout=3).text

    # 获取输入框内文本方法
    def base_get_value(self, loc):
        # 注意：一定要返回元素的文本信息
        log.info('正在获取元素{}的value值'.format(loc))
        return self.base_find_element(loc, timeout=3).get_attribute('value')

    # 单个元素截图
    def base_get_element_screenshot(self, loc):
        log.info('先获取元素{}的src名称'.format(loc))
        scr_name = self.base_find_element(loc).get_attribute('src')
        png_name = ''.join([x for x in scr_name if x.isdigit()])
        log.info('名称为{}'.format(png_name))
        png_file = './image/verification_{}.png'.format(png_name)
        log.info('正在给元素{}截图'.format(loc))
        self.base_find_element(loc).screenshot(png_file)
        log.info('截图成功！')
        return png_file

    # 将图片写入aller报告
    def base_write_img(self, png_file):
        # 1.获取图片流
        log.error('图片正在写入aller报告')
        with open(png_file, 'rb') as f:
            file = f.read()
        # 2.调用aller的方法
        allure.attach(file, "错误截图", allure.attachment_type.PNG)
        log.error('写入完成')

    # 截图方法
    def base_get_image(self):
        log.error('断言出错！正在截图')
        png_file = "./image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S"))
        self.driver.get_screenshot_as_file(png_file)
        log.error('截图完成，名称为{}'.format(png_file))
        self.base_write_img(png_file)

    # 封装判断元素是否存在
    def base_if_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            log.info('判断元素{}存在'.format(loc))
            # 找到元素  aseertTrue
            return True
        except:
            # 没找到元素
            return False

    # 鼠标操作-元素右击
    def base_context_click(self, loc):
        log.info('正在右击元素:{}'.format(loc))
        self.action.context_click(self.base_find_element(loc)).perform()

    # 鼠标操作-元素双击
    def base_double_click(self, loc):
        log.info('正在右击元素:{}'.format(loc))
        self.action.double_click(self.base_find_element(loc)).perform()

    # 鼠标操作-元素拖动
    def base_drag_and_drop(self, loc_source, loc_target):
        log.info('正在从元素:{}拖动到元素:{}上'.format(loc_source, loc_target))
        self.action.drag_and_drop(self.base_find_element(loc_source), self.base_find_element(loc_target)).perform()

    # 鼠标操作-元素悬挺
    def base_move(self, loc):
        log.info('正在把鼠标悬停在元素:{}之上'.format(loc))
        self.action.move_to_element(self.base_find_element(loc)).perform()

    # 进入框架方法
    def base_goto_frame(self, frame_name):
        log.info('正在进入框架:{}'.format(frame_name))
        self.driver.switch_to.frame(frame_name)

    # 返回默认框架方法
    def base_quit_frame(self):
        log.info('正在返回默认框架')
        self.driver.switch_to.default_content()

    # 进入下拉框方法
    def base_choice_select(self, loc):
        log.info('正在定位下拉框{}'.format(loc))
        select = Select(self.base_find_element(loc))
        return select

    # 下拉框通过value定位
    def base_select_value(self, loc, value):
        self.base_choice_select(loc).select_by_value(value)

    # 下拉框通过index定位
    def base_select_index(self, loc, index):
        self.base_choice_select(loc).select_by_index(index)
