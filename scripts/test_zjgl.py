from time import sleep
import pytest
from base.get_driver import GetDriver
from page.page import PageLogin
from tool.export import get_filename
from tool.get_log import GetLogger
from tool.get_verification import YdmVerify
from tool.read_yaml import read_yaml

log = GetLogger.get_logger()


# 新建测试类并继承
class TestLogin():
    login = None

    # setUp
    def setup_class(cls):
        # 实例化 获取页面对象 PageLogin
        cls.login = PageLogin(GetDriver().get_driver())
        # 先登录
        account = read_yaml('account.yaml')
        username = account[0][0]
        password = account[0][1]
        token = account[0][2]
        # 输入用户名
        cls.login.page_input_username(username)
        # 输入密码
        cls.login.page_input_password(password)
        # 先刷新下验证码
        cls.login.page_click_verification()
        # 验证码截图
        png_file = cls.login.page_screenshot_verification_png()
        sleep(1)
        # # 调用本地验证码识别,不一定能成功
        # verification_code = YdmVerify().dddd_ocr(png_file)
        # 调用付费接口识别验证码 备用，成功率高
        verification_code = YdmVerify().common_verify(png_file, token)
        # 输入验证码
        cls.login.page_input_ver(verification_code)
        # 点击登录按钮
        cls.login.page_click_login_btn()
        # 点击藏品管理
        sleep(1)
        cls.login.page_click_cpgl()
        # 点击征集管理
        sleep(1)
        cls.login.page_click_zjgl()
        # 点击线索录入
        sleep(1)
        cls.login.page_click_xslr()
        # 判断弹出的框是否有新句柄
        # all_handles = GetDriver().get_driver().window_handles
        # print(all_handles)

    # teardown
    def teardown_class(cls):
        sleep(3)
        # 关闭 driver驱动对象
        GetDriver().quit_driver()

    # 线索录入
    # 用例001-003
    # 新增-测试方法
    @pytest.mark.parametrize('name, person, expect_result',
                             [('藏品线索1', '水荣荣', '添加成功！'), ('藏品线索2', '水荣荣', '添加成功！'),
                              ('藏品线索3', '水荣荣', '添加成功！')])
    def test001_003(self, name, person, expect_result):
        sleep(1)
        # 调用方法
        self.login.page_list_add(name, person)
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except Exception as e:
            log.error('断言出错，错误原因：{}'.format(e))
            # 截图
            self.login.page_get_img()
            raise

    # 用例004
    # 导入-测试方法
    @pytest.mark.parametrize('file_name_path, expect_result',
                             [("C:\\Users\\caojingwei\\Desktop\\线索录入导入.xlsx", "导入成功")])
    def test004(self, file_name_path, expect_result):
        sleep(1)
        self.login.page_file_import(file_name_path)
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例005
    # 导出-测试方法
    def test005(self):
        sleep(1)
        self.login.page_list_export()

    # 用例006
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品线索1'])
    def test006(self, name):
        sleep(1)
        self.login.page_list_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list1()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例007
    # 编辑-测试方法
    @pytest.mark.parametrize('name, expect_result', [('藏品线索1修改', '更新成功！')])
    def test007(self, name, expect_result):
        sleep(1)
        self.login.page_list_edit(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例008
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品线索1修改'])
    def test008(self, name):
        sleep(1)
        self.login.page_list_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list1()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例009
    # 废弃-测试方法
    @pytest.mark.parametrize('cause, expect_result', [('废弃', '作废成功！')])
    def test009(self, cause, expect_result):
        sleep(1)
        self.login.page_list_abandon(cause)
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例010
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品线索2'])
    def test010(self, name):
        sleep(1)
        self.login.page_list_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list1()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例011
    # 批量指派-测试方法
    @pytest.mark.parametrize('expect_result', ['指派成功！'])
    def test011(self, expect_result):
        sleep(1)
        self.login.page_batch_assigned()
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例012
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品线索3'])
    def test012(self, name):
        sleep(1)
        self.login.page_list_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list1()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例013
    # 批量指派-测试方法
    @pytest.mark.parametrize('expect_result', ['指派成功！'])
    def test013(self, expect_result):
        sleep(1)
        self.login.page_batch_assigned()
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例014
    # 导出-测试方法
    def test014(self):
        sleep(1)
        self.login.page_click_yzp()
        self.login.page_list_export()

    # 用例015
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品线索2'])
    def test015(self, name):
        sleep(1)
        self.login.page_list_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list1()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例016
    # 查看-测试方法
    @pytest.mark.parametrize('name', ['藏品线索2'])
    def test016(self, name):
        sleep(1)
        try:
            # 获取线索名称
            msg = self.login.page_list_check()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例017
    # 导出-测试方法
    def test017(self):
        sleep(1)
        self.login.page_click_yfq()
        self.login.page_list_export()

    # 用例018
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品线索1修改'])
    def test018(self, name):
        sleep(1)
        self.login.page_list_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list1()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例019
    # 查看-测试方法
    @pytest.mark.parametrize('name', ['藏品线索1修改'])
    def test019(self, name):
        sleep(1)
        try:
            # 获取线索名称
            msg = self.login.page_list_check()
            print(msg)
            # 断言
            assert (msg == name)
        except:
            # 截图
            self.login.page_get_img()

    # 线索跟踪
    # 用例020
    # 导出-测试方法
    def test020(self):
        sleep(1)
        self.login.page_click_xsgz()
        self.login.page_list_export()

    # 用例021
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品线索2'])
    def test021(self, name):
        sleep(1)
        self.login.page_list_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list1()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例022
    # 终止-测试方法
    @pytest.mark.parametrize('c_time, cause, expect_result', [('2022-03-30 00:00:00', '终止', '终止成功！')])
    def test022(self, c_time, cause, expect_result):
        sleep(1)
        self.login.page_end(c_time, cause)
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例023
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品线索3'])
    def test023(self, name):
        sleep(1)
        self.login.page_list_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list1()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例024
    # 填写日志-测试方法
    @pytest.mark.parametrize('c_time, xs_log, expect_result', [('2022-03-30 00:00:00', '跟踪日志1', '添加成功！')])
    def test024(self, c_time, xs_log, expect_result):
        sleep(1)
        self.login.page_write_log(c_time, xs_log)
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例025
    # 完成跟踪-测试方法
    @pytest.mark.parametrize('expect_result', ['提交成功！'])
    def test025(self, expect_result):
        sleep(3)
        self.login.page_trace_over()
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例026
    # 导出-测试方法
    def test026(self):
        sleep(1)
        self.login.page_click_ywc()
        self.login.page_list_export()

    # 用例027
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品线索3'])
    def test027(self, name):
        sleep(1)
        self.login.page_list_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list1()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例028
    # 查看-测试方法
    @pytest.mark.parametrize('name', ['藏品线索3'])
    def test028(self, name):
        sleep(1)
        try:
            # 获取线索名称
            msg = self.login.page_list_check()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 已终止
    # 用例029
    # 导出-测试方法
    def test029(self):
        sleep(1)
        self.login.page_click_yzz()
        self.login.page_list_export()

    # 用例030
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品线索2'])
    def test030(self, name):
        sleep(1)
        self.login.page_list_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list1()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例031
    # 查看-测试方法
    @pytest.mark.parametrize('name', ['藏品线索2'])
    def test031(self, name):
        sleep(1)
        try:
            # 获取线索名称
            msg = self.login.page_list_check()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 征集录入
    # 用例032
    # 新增征集单-测试方法
    @pytest.mark.parametrize('form_name, xs_name, expect_result', [("征集单1", '藏品线索3', '添加成功！')])
    def test032(self, form_name, xs_name, expect_result):
        # print(nub, name, des, expect_result, success)
        sleep(1)
        self.login.page_click_zjlr()
        # 调用方法
        self.login.page_form_add(form_name, xs_name)
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例033-035
    # 新增-测试方法
    @pytest.mark.parametrize('for_form, add_collection_name, expect_result',
                             [('征集单1', '藏品01', '添加成功！'), ('征集单1', '藏品02', '添加成功！'),
                              ('征集单1', '藏品03', '添加成功！')])
    def test033_035(self, for_form, add_collection_name, expect_result):
        sleep(1)
        # 调用方法
        self.login.page_collection_add(for_form, add_collection_name)
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例036
    # 导入-测试方法
    @pytest.mark.parametrize('file_name_path, expect_result',
                             [("C:\\Users\\caojingwei\\Desktop\\征集录入导入.xlsx", "导入成功")])
    def test036(self, file_name_path, expect_result):
        sleep(1)
        self.login.page_file_import(file_name_path)
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例037
    # 导出-测试方法
    def test037(self):
        sleep(1)
        self.login.page_list_export()

    # 用例038
    # 查询-测试方法
    @pytest.mark.parametrize('collection_name', ['藏品01'])
    def test038(self, collection_name):
        sleep(1)
        self.login.page_collection_search(collection_name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list3()
            print(msg)
            # 断言
            assert msg == collection_name
        except:
            # 截图
            self.login.page_get_img()

    # 用例039
    # 编辑-测试方法
    @pytest.mark.parametrize('collection_name, expect_result', [('藏品01修改', '更新成功！')])
    def test039(self, collection_name, expect_result):
        sleep(1)
        self.login.page_collection_edit(collection_name)
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例040
    # 查询-测试方法
    @pytest.mark.parametrize('collection_name', ['藏品01修改'])
    def test040(self, collection_name):
        sleep(1)
        self.login.page_collection_search(collection_name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list3()
            print(msg)
            # 断言
            assert (msg == collection_name)
        except:
            # 截图
            self.login.page_get_img()

    # 用例041
    # 删除-测试方法
    @pytest.mark.parametrize('expect_result', ['删除成功！'])
    def test041(self, expect_result):
        sleep(1)
        self.login.page_collection_delete()
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例042
    # 查询-测试方法
    @pytest.mark.parametrize('collection_name', ['藏品02'])
    def test042(self, collection_name):
        sleep(1)
        self.login.page_collection_search(collection_name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list3()
            print(msg)
            # 断言
            assert msg == collection_name
        except:
            # 截图
            self.login.page_get_img()

    # 用例043
    # 提交征集-测试方法
    @pytest.mark.parametrize('expect_result', ['提交成功！'])
    def test043(self, expect_result):
        sleep(1)
        self.login.page_submit_collect()
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例044
    # 查询-测试方法
    @pytest.mark.parametrize('collection_name', ['藏品03'])
    def test044(self, collection_name):
        sleep(1)
        self.login.page_collection_search(collection_name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list3()
            print(msg)
            # 断言
            assert msg == collection_name
        except:
            # 截图
            self.login.page_get_img()

    # 用例045
    # 提交征集-测试方法
    @pytest.mark.parametrize('expect_result', ['提交成功！'])
    def test045(self, expect_result):
        sleep(1)
        self.login.page_submit_collect()
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 已提交
    # 用例046
    # 导出-测试方法
    def test046(self):
        sleep(1)
        self.login.page_click_ytj()
        self.login.page_list_export()

    # 用例047
    # 查询-测试方法
    @pytest.mark.parametrize('collection_name', ['藏品02'])
    def test047(self, collection_name):
        sleep(1)
        self.login.page_collection_search(collection_name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list3()
            print(msg)
            # 断言
            assert msg == collection_name
        except:
            # 截图
            self.login.page_get_img()

    # 用例048
    # 查看-测试方法
    @pytest.mark.parametrize('name', ['藏品02'])
    def test048(self, name):
        sleep(1)
        try:
            # 获取藏品名称
            msg = self.login.page_check_collection()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 征集中
    # 用例049
    # 导出-测试方法
    def test049(self):
        sleep(1)
        self.login.page_click_zjz()
        self.login.page_list_export()

    # 用例050
    # 查询-测试方法
    @pytest.mark.parametrize('collection_name', ['藏品02'])
    def test050(self, collection_name):
        sleep(1)
        self.login.page_collection_search(collection_name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list3()
            print(msg)
            # 断言
            assert msg == collection_name
        except:
            # 截图
            self.login.page_get_img()

    # 用例051
    # 终止-测试方法
    @pytest.mark.parametrize('cause, expect_result', [('终止', '终止成功！')])
    def test051(self, cause, expect_result):
        sleep(1)
        self.login.page_collect_over(cause)
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例052
    # 查询-测试方法
    @pytest.mark.parametrize('collection_name', ['藏品03'])
    def test052(self, collection_name):
        sleep(1)
        self.login.page_collection_search(collection_name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list3()
            print(msg)
            # 断言
            assert msg == collection_name
        except:
            # 截图
            self.login.page_get_img()

    # 用例053
    # 鉴定-测试方法
    @pytest.mark.parametrize(
        'zjxm1, zjzc1, szdw1, pdrq1, gjfw1,jbr2, jbrdw2, pdrq2, gjfw2,jbr3, jbrdw3, pdrq3, gjfw3,jbr4, jbrdw4, tprq4, qdjg4,jbr5, jbrdw5, pfr5, pfrq5, pfjg5,jbr6, jbrdw6, tprq6, cjjg6, expect_result',
        [('专家1', '职称1', '单位1', '2022-04-25', '10w',
          '经办人2', '单位2', '2022-04-26', '11w',
          '经办人3', '单位3', '2022-04-27', '12w',
          '经办人4', '单位4', '2022-04-28', '13w',
          '经办人5', '单位5', '领导1', '2022-04-29', '14w',
          '经办人6', '单位6', '2022-04-30', '15w', '保存成功！')])
    def test053(self,
                zjxm1, zjzc1, szdw1, pdrq1, gjfw1,
                jbr2, jbrdw2, pdrq2, gjfw2,
                jbr3, jbrdw3, pdrq3, gjfw3,
                jbr4, jbrdw4, tprq4, qdjg4,
                jbr5, jbrdw5, pfr5, pfrq5, pfjg5,
                jbr6, jbrdw6, tprq6, cjjg6, expect_result):
        sleep(1)
        self.login.page_collect_authenticate(zjxm1, zjzc1, szdw1, pdrq1, gjfw1,
                                             jbr2, jbrdw2, pdrq2, gjfw2,
                                             jbr3, jbrdw3, pdrq3, gjfw3,
                                             jbr4, jbrdw4, tprq4, qdjg4,
                                             jbr5, jbrdw5, pfr5, pfrq5, pfjg5,
                                             jbr6, jbrdw6, tprq6, cjjg6)
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例054
    # 提交确认征集-测试方法
    @pytest.mark.parametrize('expect_result', ['提交成功！'])
    def test054(self, expect_result):
        sleep(1)
        self.login.page_submit_confirm_collect()
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例055
    # 导出-测试方法
    def test055(self):
        sleep(1)
        self.login.page_click_yjd()
        self.login.page_list_export()

    # 用例056
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品03'])
    def test056(self, name):
        sleep(1)
        self.login.page_collection_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list3()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例057
    # 查看-测试方法
    @pytest.mark.parametrize('name', ['藏品03'])
    def test057(self, name):
        sleep(1)
        try:
            # 获取藏品名称
            msg = self.login.page_check_collection()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例058
    # 导出-测试方法
    def test058(self):
        sleep(1)
        self.login.page_click_yzz()
        self.login.page_list_export()

    # 用例059
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品02'])
    def test059(self, name):
        sleep(1)
        self.login.page_collection_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list3()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例060
    # 查看-测试方法
    @pytest.mark.parametrize('name', ['藏品02'])
    def test060(self, name):
        sleep(1)
        try:
            # 获取藏品名称
            msg = self.login.page_check_collection()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 确认征集
    # 用例061
    # 导出-测试方法
    def test061(self):
        sleep(1)
        self.login.page_click_qrzj()
        self.login.page_list_export()

    # 用例062
    # 关联合同-测试方法
    @pytest.mark.parametrize('file_name_path', ["C:\\Users\\caojingwei\\Desktop\\合同.png"])
    def test062(self, file_name_path):
        sleep(1)
        self.login.page_association_rules(file_name_path)

    # 用例063
    # 取消关联合同-测试方法
    @pytest.mark.parametrize('expect_result', ['取消关联成功！'])
    def test063(self, expect_result):
        sleep(1)
        self.login.page_cancle_association_rules()
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例064
    # 关联合同-测试方法
    @pytest.mark.parametrize('file_name_path',["C:\\Users\\caojingwei\\Desktop\\合同.png"])
    def test064(self, file_name_path):
        sleep(1)
        self.login.page_association_rules(file_name_path)

    # 用例065
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品03'])
    def test065(self, name):
        sleep(1)
        self.login.page_collection_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list3()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例066
    # 查看-测试方法
    @pytest.mark.parametrize('name', ['藏品03'])
    def test066(self, name):
        sleep(1)
        try:
            # 获取藏品名称
            msg = self.login.page_check_collection()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例067
    # 提交拨库-测试方法
    @pytest.mark.parametrize('expect_result', ['提交成功！'])
    def test067(self, expect_result):
        sleep(1)
        self.login.page_submit_warehouse()
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例068
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品03'])
    def test068(self, name):
        sleep(1)
        self.login.page_click_yzj()
        sleep(3)
        self.login.page_collection_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list3()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例069
    # 查看-测试方法
    @pytest.mark.parametrize('name', ['藏品03'])
    def test069(self, name):
        sleep(1)
        try:
            # 获取藏品名称
            msg = self.login.page_check_collection()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 拨库管理
    # 用例070
    # 导出-测试方法
    def test070(self):
        sleep(1)
        self.login.page_click_bkgl()
        self.login.page_list_export()

    # 用例071
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品03'])
    def test071(self, name):
        sleep(1)
        self.login.page_collection_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list3()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例072
    # 查看-测试方法
    @pytest.mark.parametrize('name', ['藏品03'])
    def test072(self, name):
        sleep(1)
        try:
            # 获取藏品名称
            msg = self.login.page_check_collection()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例073
    # 提交拨库-测试方法
    @pytest.mark.parametrize('expect_result', ['拨库成功！'])
    def test073(self, expect_result):
        sleep(1)
        self.login.page_warehouse()
        try:
            # 获取提示信息
            msg = self.login.page_get_hint_mes()
            print(msg)
            # 断言
            assert msg == expect_result
        except:
            # 截图
            self.login.page_get_img()

    # 用例074
    # 导出-测试方法
    def test074(self):
        sleep(1)
        self.login.page_click_ybk()
        self.login.page_list_export()

    # 用例075
    # 查询-测试方法
    @pytest.mark.parametrize('name', ['藏品03'])
    def test075(self, name):
        sleep(1)
        self.login.page_collection_search(name)
        try:
            # 获取提示信息
            msg = self.login.page_get_row1_list3()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例076
    # 查看-测试方法
    @pytest.mark.parametrize('name', ['藏品03'])
    def test076(self, name):
        sleep(1)
        try:
            # 获取藏品名称
            msg = self.login.page_check_collection()
            print(msg)
            # 断言
            assert msg == name
        except:
            # 截图
            self.login.page_get_img()

    # 用例077
    # 导出-测试方法
    @pytest.mark.parametrize('file_name', ['线索信息_未指派', '线索信息_已指派', '线索信息_作废',
                                           '线索跟踪信息_跟踪中', '线索跟踪信息_已完成', '线索跟踪信息_已终止',
                                           '征集录入_未提交', '征集录入_已提交',
                                           '征集中_待鉴定', '征集中_已鉴定', '征集中_已终止',
                                           '确认征集_未征集',
                                           '拨库管理_待拨库', '拨库管理_已拨库'])
    def test077(self, file_name):
        msg = get_filename(file_name)
        print(msg)
