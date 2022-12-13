from time import sleep
import page
from base.base import Base
from tool.get_log import GetLogger

log = GetLogger.get_logger()


class PageLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        log.info('输入用户名：{}'.format(username))
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_password(self, pwd):
        log.info('输入密码：{}'.format(pwd))
        self.base_input(page.login_pwd, pwd)

    # 点击刷新验证码
    def page_click_verification(self):
        log.info('点击刷新验证码')
        return self.base_click(page.verification_png)

    # 给验证码截图
    def page_screenshot_verification_png(self):
        log.info('给验证码截图')
        return self.base_get_element_screenshot(page.verification_png)

    # 输入验证码
    def page_input_ver(self, ver):
        log.info('输入验证码:{}'.format(ver))
        self.base_input(page.login_ver, ver)

    # 点击登录按钮
    def page_click_login_btn(self):
        log.info('点击登录按钮')
        self.base_click(page.login_btn)

    # 点击藏品管理
    def page_click_cpgl(self):
        log.info('点击藏品管理')
        self.base_click(page.cpgl)

    # 点击征集管理
    def page_click_zjgl(self):
        log.info('点击征集管理')
        self.base_click(page.zjgl)

    # 点击线索录入
    def page_click_xslr(self):
        log.info('点击线索录入')
        self.base_click(page.xslr)

    # 点击线索跟踪
    def page_click_xsgz(self):
        log.info('点击线索跟踪')
        self.base_click(page.xsgz)

    # 点击征集录入
    def page_click_zjlr(self):
        log.info('点击征集录入')
        self.base_click(page.zjlr)

    # 点击征集中
    def page_click_zjz(self):
        log.info('点击征集中')
        self.base_click(page.zjz)

    # 点击确认征集
    def page_click_qrzj(self):
        log.info('点击确认征集')
        self.base_click(page.qrzj)

    # 点击拨库管理
    def page_click_bkgl(self):
        log.info('点击拨库管理')
        self.base_click(page.bkgl)

    # 获取页面数据数文本
    def page_get_date_list(self):
        log.info('获取页面数据数')
        return self.base_get_text(page.date_list)

    # 点击已指派
    def page_click_yzp(self):
        log.info('点击已指派')
        self.base_click(page.yzp)

    # 点击已废弃
    def page_click_yfq(self):
        log.info('点击已废弃')
        self.base_click(page.yfq)

    # 点击已完成
    def page_click_ywc(self):
        log.info('点击已完成')
        self.base_click(page.ywc)

    # 点击已终止
    def page_click_yzz(self):
        log.info('点击已终止')
        self.base_click(page.yzz)

    # 点击已提交
    def page_click_ytj(self):
        log.info('点击已提交')
        self.base_click(page.ytj)

    # 点击已鉴定
    def page_click_yjd(self):
        log.info('点击已鉴定')
        self.base_click(page.yjd)

    # 点击已征集
    def page_click_yzj(self):
        log.info('点击已征集')
        self.base_click(page.yzj)

    # 点击已拨库
    def page_click_ybk(self):
        log.info('点击已拨库')
        self.base_click(page.ybk)

    # 列表界面-输入线索名称
    def page_input_thread_name(self, name):
        log.info('列表界面-输入线索名称:{}'.format(name))
        self.base_input(page.thread_name, name)

    # 列表界面-输入藏品名称
    def page_input_collection_name(self, collection_name):
        log.info('列表界面-输入藏品名称:{}'.format(collection_name))
        self.base_input(page.collection_name, collection_name)

    # 点击查询按钮
    def page_click_search_btn(self):
        log.info('点击查询按钮')
        self.base_click(page.search_btn)

    # 点击重置按钮
    def page_click_reset_btn(self):
        log.info('点击重置按钮')
        self.base_click(page.reset_btn)

    # 点击新增按钮
    def page_click_add_btn(self):
        log.info('点击新增按钮')
        self.base_click(page.add_btn)

    # 点击导出按钮
    def page_click_export_btn(self):
        log.info('点击导出按钮')
        self.base_click(page.export_btn)

    # 点击导入按钮
    def page_click_import_btn(self):
        log.info('点击导入按钮')
        self.base_click(page.import_btn)

    # 点击批量指派按钮
    def page_click_batch_assigned_btn(self):
        log.info('点击批量指派按钮')
        self.base_click(page.batch_assigned_btn)

    # 点击废弃按钮
    def page_click_abandon_btn(self):
        log.info('点击废弃按钮')
        self.base_click(page.abandon_btn)

    # 点击完成跟踪按钮
    def page_click_trace_over_btn(self):
        log.info('点击完成跟踪按钮')
        self.base_click(page.trace_over_btn)

    # 点击终止按钮
    def page_click_end_btn(self):
        log.info('点击终止按钮')
        self.base_click(page.end_btn)

    # 点击添加征集单按钮
    def page_click_add_zjd_btn(self):
        log.info('点击添加征集单按钮')
        self.base_click(page.add_zjd_btn)

    # 点击提交征集按钮
    def page_click_submit_collect_btn(self):
        log.info('点击提交征集按钮')
        self.base_click(page.submit_collect_btn)

    # 点击删除按钮
    def page_click_delete_btn(self):
        log.info('点击删除按钮')
        self.base_click(page.delete_btn)

    # 点击提交确认征集按钮
    def page_click_submit_confirm_collect_btn(self):
        log.info('点击提交确认征集按钮')
        self.base_click(page.submit_confirm_collect_btn)

    # 点击关联合同按钮
    def page_click_association_rules_btn(self):
        log.info('点击关联合同按钮')
        self.base_click(page.association_rules_btn)

    # 点击取消关联合同按钮
    def page_click_cancle_association_rules_btn(self):
        log.info('点击取消关联合同按钮')
        self.base_click(page.cancle_association_rules_btn)

    # 点击提交拨库按钮
    def page_click_submit_warehouse_btn(self):
        log.info('点击提交拨库按钮')
        self.base_click(page.submit_warehouse_btn)

    # 点击拨库按钮
    def page_click_warehouse_btn(self):
        log.info('点击拨库按钮')
        self.base_click(page.warehouse_btn)

    # # 点击编辑按钮
    # def page_click_edit_btn(self):
    #     self.base_click(page.edit_btn)
    #
    # # 点击查看按钮
    # def page_click_check_btn(self):
    #     self.base_click(page.check_btn)
    #
    # # 点击鉴定按钮
    # def page_click_authenticate_btn(self):
    #     self.base_click(page.authenticate_btn)
    #
    # # 点击日志填写按钮
    # def page_click_log_write_btn(self):
    #     self.base_click(page.log_write_btn)

    # 点击列表操作按钮(例如查看、编辑、鉴定、日志填写)
    def page_click_list_operate_btn(self):
        log.info('点击列表操作按钮(例如查看、编辑、鉴定、日志填写)')
        self.base_click(page.list_operate_btn)

    # 点击全选按钮
    def page_click_all_btn(self):
        log.info('点击全选按钮')
        self.base_click(page.all_btn)

    # 点击第一行的选择按钮
    def page_click_list1_select_btn(self):
        log.info('点击第一行的选择按钮')
        self.base_click(page.list1_select_btn)

    # 截图
    def page_get_img(self):
        log.info('截图')
        self.base_get_image()

    # 获取提示信息
    def page_get_hint_mes(self):
        log.info('获取提示信息')
        return self.base_get_text(page.hint_mes)

    # 获取第一行第一列的文本
    def page_get_row1_list1(self):
        log.info('获取第一行第一列的文本')
        return self.base_get_text(page.xs_row1_list1)

    # 获取第一行第三列的文本
    def page_get_row1_list3(self):
        log.info('获取第一行第三列的文本')
        return self.base_get_text(page.zj_row1_list3)

    # 获取线索名称
    def page_get_thread_name(self):
        log.info('获取线索名称')
        return self.base_get_value(page.add_thread_name)

    # 获取藏品名称
    def page_get_collection_name(self):
        log.info('获取藏品名称')
        return self.base_get_value(page.add_collection_name)

    # 新增界面-输入线索名称
    def page_input_add_thread_name(self, name):
        log.info('新增界面-输入线索名称:{}'.format(name))
        self.base_input(page.add_thread_name, name)

    # 新增界面-输入指派人并选择下拉框的第一个
    def page_input_designated_person(self, person):
        log.info('新增界面-输入指派人并选择下拉框的第一个:{}'.format(person))
        self.base_input(page.designated_person, person)
        self.base_keys(page.designated_person)

    # 新增界面-点击保存按钮
    def page_click_save_btn(self):
        log.info('新增界面-点击保存按钮')
        self.base_click(page.save_btn)

    # 新增界面-点击取消按钮
    def page_click_cancel_btn(self):
        log.info('新增界面-点击取消按钮')
        self.base_click(page.cancel_btn)

    # 新增界面-点击关闭按钮
    def page_click_close_btn(self):
        log.info('新增界面-点击关闭按钮')
        self.base_click(page.close_btn)

    # 废弃界面-输入原因
    def page_input_cause(self, cause):
        log.info('废弃界面-输入原因')
        self.base_input(page.cause, cause)

    # 废弃界面-点击确定按钮
    def page_click_confirm_btn(self):
        log.info('废弃界面-点击确定按钮')
        self.base_click(page.confirm_btn)

    # 废弃界面-点击时间此刻按钮
    def page_click_time_now_btn(self):
        log.info('废弃界面-点击时间此刻按钮')
        self.base_click(page.time_now_btn)

    # 导出界面-点击导出的列全选框
    def page_click_input_select_all(self):
        log.info('导出界面-点击导出的列全选框')
        self.base_click(page.input_select_all)

    # 导出界面-点击右箭头按钮
    def page_click_input_right_button(self):
        log.info('导出界面-点击右箭头按钮')
        self.base_click(page.input_right_button)

    # 导出界面-点击二次导出按钮
    def page_click_two_export_btn(self):
        log.info('导出界面-点击二次导出按钮')
        self.base_click(page.two_export_btn)

    # 导入界面-输入选取文件按钮的值
    def page_input_select_file_btn(self, file):
        log.info('导入界面-输入选取文件按钮的值:{}'.format(file))
        self.base_input_file(page.select_file_btn, file)

    # 导入界面-点击二次导入按钮
    def page_click_two_import_btn(self):
        log.info('导入界面-点击二次导入按钮')
        self.base_click(page.two_import_btn)

    # 批量指派界面-点击是按钮
    def page_click_yes_btn(self):
        log.info('批量指派界面-点击是按钮')
        self.base_click(page.yes_btn)

    # 终止界面-输入时间
    def page_input_c_time(self, c_time):
        log.info('终止界面-输入时间')
        self.base_input(page.c_time, c_time)

    # 终止界面-点击二次确认框
    def page_click_two_confirm_btn(self):
        log.info('终止界面-点击二次确认框')
        self.base_click(page.two_confirm_btn)

    # 线索日志界面-输入跟踪日志
    def page_input_xs_log(self, xs_log):
        log.info('线索日志界面-输入跟踪日志:{}'.format(xs_log))
        self.base_input(page.xs_log, xs_log)

    # 线索日志界面-点击添加按钮
    def page_click_log_add_btn(self):
        log.info('线索日志界面-点击添加按钮')
        self.base_click(page.log_add_btn)

    # 线索日志界面-判断暂无跟踪信息元素是否存在
    def page_if_exist_not_log(self):
        return self.base_if_exist(page.not_log_loc)

    # 征集单界面-输入单名称
    def page_input_form_name(self, form_name):
        log.info('征集单界面-输入单名称:{}'.format(form_name))
        self.base_input(page.form_name, form_name)

    # 征集单界面-点击并输入线索名称并选择下拉框第一个
    def page_input_form_xs_name(self, xs_name):
        log.info('征集单界面-点击并输入线索名称并选择下拉框第一个:{}'.format(xs_name))
        self.base_click(page.form_xs_name)
        self.base_input(page.form_xs_name, xs_name)
        self.base_keys(page.form_xs_name)
        sleep(1)

    # 藏品编辑界面-点击并输入所属征集单并选择下拉框第一个
    def page_input_for_form(self, for_form):
        log.info('藏品编辑界面-点击并输入所属征集单并选择下拉框第一个:{}'.format(for_form))
        self.base_click(page.for_form)
        self.base_input(page.for_form, for_form)
        self.base_keys(page.for_form)
        sleep(1)

    # 藏品编辑界面-输入藏品名称
    def page_input_add_collection_name(self, add_collection_name):
        log.info('藏品编辑界面-输入藏品名称:{}'.format(add_collection_name))
        self.base_input(page.add_collection_name, add_collection_name)

    # 藏品编辑界面-点击确认按钮
    def page_click_collection_confirm_btn(self):
        log.info('藏品编辑界面-点击确认按钮')
        self.base_click(page.collection_confirm_btn)

    # 藏品鉴定界面-点击鉴定/评审按钮
    def page_click_jd_ps_btn(self):
        log.info('藏品鉴定界面-点击鉴定/评审按钮')
        self.base_click(page.jd_ps_btn)

    # 藏品鉴定界面-点击专家鉴定标签
    def page_click_a_zjjd(self):
        log.info('藏品鉴定界面-点击专家鉴定标签')
        self.base_click(page.a_zjjd)

    # 藏品鉴定界面-输入专家姓名
    def page_input_zjjd_zjxm(self, zjjd_zjxm):
        log.info('藏品鉴定界面-输入专家姓名:{}'.format(zjjd_zjxm))
        self.base_input(page.zjjd_zjxm, zjjd_zjxm)

    # 藏品鉴定界面-输入专家职称
    def page_input_zjjd_zjzc(self, zjjd_zjzc):
        log.info('藏品鉴定界面-输入专家职称:{}'.format(zjjd_zjzc))
        self.base_input(page.zjjd_zjzc, zjjd_zjzc)

    # 藏品鉴定界面-输入所在单位
    def page_input_zjjd_szdw(self, zjjd_szdw):
        log.info('藏品鉴定界面-输入所在单位:{}'.format(zjjd_szdw))
        self.base_input(page.zjjd_szdw, zjjd_szdw)

    # 藏品鉴定界面-输入评定日期
    def page_input_zjjd_pdrq(self, zjjd_pdrq):
        log.info('藏品鉴定界面-输入评定日期:{}'.format(zjjd_pdrq))
        self.base_input(page.zjjd_pdrq, zjjd_pdrq)

    # 藏品鉴定界面-输入估价范围
    def page_input_zjjd_gjfw(self, zjjd_gjfw):
        log.info('藏品鉴定界面-输入估价范围:{}'.format(zjjd_gjfw))
        self.base_input(page.zjjd_gjfw, zjjd_gjfw)

    # 藏品鉴定界面-点击专家鉴定结果标签
    def page_click_a_zjjdjg(self):
        log.info('藏品鉴定界面-点击专家鉴定结果标签')
        self.base_click(page.a_zjjdjg)

    # 藏品鉴定界面-输入经办人
    def page_input_zjjdjg_jbr(self, zjjdjg_jbr):
        log.info('藏品鉴定界面-输入经办人：{}'.format(zjjdjg_jbr))
        self.base_input(page.zjjdjg_jbr, zjjdjg_jbr)

    # 藏品鉴定界面-输入经办人单位
    def page_input_zjjdjg_jbrdw(self, zjjdjg_jbrdw):
        log.info('藏品鉴定界面-输入经办人单位{}'.format(zjjdjg_jbrdw))
        self.base_input(page.zjjdjg_jbrdw, zjjdjg_jbrdw)

    # 藏品鉴定界面-输入评定日期
    def page_input_zjjdjg_pdrq(self, zjjdjg_pdrq):
        log.info('藏品鉴定界面-输入评定日期{}'.format(zjjdjg_pdrq))
        self.base_input(page.zjjdjg_pdrq, zjjdjg_pdrq)

    # 藏品鉴定界面-输入估价范围
    def page_input_zjjdjg_gjfw(self, zjjdjg_gjfw):
        log.info('藏品鉴定界面-输入估价范围{}'.format(zjjdjg_gjfw))
        self.base_input(page.zjjdjg_gjfw, zjjdjg_gjfw)

    # 藏品鉴定界面-点击是否征集_是勾选栏
    def page_click_zjjdjg_zj_yes(self):
        log.info('藏品鉴定界面-点击是否征集_是勾选栏')
        self.base_click(page.zjjdjg_zj_yes)

    # 藏品鉴定界面-点击馆内评审结果标签
    def page_click_a_gnpsjg(self):
        log.info('藏品鉴定界面-点击馆内评审结果标签')
        self.base_click(page.a_gnpsjg)

    # 藏品鉴定界面-输入经办人
    def page_input_gnpsjg_jbr(self, gnpsjg_jbr):
        log.info('藏品鉴定界面-输入经办人:{}'.format(gnpsjg_jbr))
        self.base_input(page.gnpsjg_jbr, gnpsjg_jbr)

    # 藏品鉴定界面-输入经办人单位
    def page_input_gnpsjg_jbrdw(self, gnpsjg_jbrdw):
        log.info('藏品鉴定界面-输入经办人单位:{}'.format(gnpsjg_jbrdw))
        self.base_input(page.gnpsjg_jbrdw, gnpsjg_jbrdw)

    # 藏品鉴定界面-输入评定日期
    def page_input_gnpsjg_pdrq(self, gnpsjg_pdrq):
        log.info('藏品鉴定界面-输入评定日期:{}'.format(gnpsjg_pdrq))
        self.base_input(page.gnpsjg_pdrq, gnpsjg_pdrq)

    # 藏品鉴定界面-输入估价范围
    def page_input_gnpsjg_gjfw(self, gnpsjg_gjfw):
        log.info('藏品鉴定界面-输入估价范围:{}'.format(gnpsjg_gjfw))
        self.base_input(page.gnpsjg_gjfw, gnpsjg_gjfw)

    # 藏品鉴定界面-点击是否征集_是勾选栏
    def page_click_gnpsjg_zj_yes(self):
        log.info('藏品鉴定界面-点击是否征集_是勾选栏')
        self.base_click(page.gnpsjg_zj_yes)

    # 藏品鉴定界面-点击卖家谈判标签
    def page_click_a_mjtp(self):
        log.info('藏品鉴定界面-点击卖家谈判标签')
        self.base_click(page.a_mjtp)

    # 藏品鉴定界面-输入经办人
    def page_input_mjtp_jbr(self, mjtp_jbr):
        log.info('藏品鉴定界面-输入经办人:{}'.format(mjtp_jbr))
        self.base_input(page.mjtp_jbr, mjtp_jbr)

    # 藏品鉴定界面-输入经办人单位
    def page_input_mjtp_jbrdw(self, mjtp_jbrdw):
        log.info('藏品鉴定界面-输入经办人单位:{}'.format(mjtp_jbrdw))
        self.base_input(page.mjtp_jbrdw, mjtp_jbrdw)

    # 藏品鉴定界面-输入谈判日期
    def page_input_mjtp_tprq(self, mjtp_tprq):
        log.info('藏品鉴定界面-输入谈判日期:{}'.format(mjtp_tprq))
        self.base_input(page.mjtp_tprq, mjtp_tprq)

    # 藏品鉴定界面-输入确定价格
    def page_input_mjtp_qdjg(self, mjtp_qdjg):
        log.info('藏品鉴定界面-输入确定价格:{}'.format(mjtp_qdjg))
        self.base_input(page.mjtp_qdjg, mjtp_qdjg)

    # 藏品鉴定界面-点击是否达成一致_是勾选栏
    def page_click_mjtp_yz_yes(self):
        log.info('藏品鉴定界面-点击是否达成一致_是勾选栏')
        self.base_click(page.mjtp_yz_yes)

    # 藏品鉴定界面-点击是否需要复制品_是勾选栏
    def page_click_mjtp_fz_yes(self):
        log.info('藏品鉴定界面-点击是否需要复制品_是勾选栏')
        self.base_click(page.mjtp_fz_yes)

    # 藏品鉴定界面-点击领导批复标签
    def page_click_a_ldpf(self):
        log.info('藏品鉴定界面-点击领导批复标签')
        self.base_click(page.a_ldpf)

    # 藏品鉴定界面-输入经办人
    def page_input_ldpf_jbr(self, ldpf_jbr):
        log.info('藏品鉴定界面-输入经办人:{}'.format(ldpf_jbr))
        self.base_input(page.ldpf_jbr, ldpf_jbr)

    # 藏品鉴定界面-输入经办人单位
    def page_input_ldpf_jbrdw(self, ldpf_jbrdw):
        log.info('藏品鉴定界面-输入经办人单位：{}'.format(ldpf_jbrdw))
        self.base_input(page.ldpf_jbrdw, ldpf_jbrdw)

    # 藏品鉴定界面-输入批复人
    def page_input_ldpf_pfr(self, ldpf_pfr):
        log.info('藏品鉴定界面-输入批复人:{}'.format(ldpf_pfr))
        self.base_input(page.ldpf_pfr, ldpf_pfr)

    # 藏品鉴定界面-输入批复日期
    def page_input_ldpf_pfrq(self, ldpf_pfrq):
        log.info('藏品鉴定界面-输入批复日期:{}'.format(ldpf_pfrq))
        self.base_input(page.ldpf_pfrq, ldpf_pfrq)

    # 藏品鉴定界面-输入批复价格
    def page_input_ldpf_pfjg(self, ldpf_pfjg):
        log.info('藏品鉴定界面-输入批复价格:{}'.format(ldpf_pfjg))
        self.base_input(page.ldpf_pfjg, ldpf_pfjg)

    # 藏品鉴定界面-点击是否征集_是勾选栏
    def page_click_ldpf_zj_yes(self):
        log.info('藏品鉴定界面-点击是否征集_是勾选栏')
        self.base_click(page.ldpf_zj_yes)

    # 藏品鉴定界面-点击最终谈判标签
    def page_click_a_zztp(self):
        log.info('藏品鉴定界面-点击最终谈判标签')
        self.base_click(page.a_zztp)

    # 藏品鉴定界面-输入经办人
    def page_input_zztp_jbr(self, zztp_jbr):
        log.info('藏品鉴定界面-输入经办人:{}'.format(zztp_jbr))
        self.base_input(page.zztp_jbr, zztp_jbr)

    # 藏品鉴定界面-输入经办人单位
    def page_input_zztp_jbrdw(self, zztp_jbrdw):
        log.info('藏品鉴定界面-输入经办人单位:{}'.format(zztp_jbrdw))
        self.base_input(page.zztp_jbrdw, zztp_jbrdw)

    # 藏品鉴定界面-输入谈判日期
    def page_input_zztp_tprq(self, zztp_tprq):
        log.info('藏品鉴定界面-输入谈判日期:{}'.format(zztp_tprq))
        self.base_input(page.zztp_tprq, zztp_tprq)

    # 藏品鉴定界面-输入成交价格
    def page_input_zztp_cjjg(self, zztp_cjjg):
        log.info('藏品鉴定界面-输入成交价格:{}'.format(zztp_cjjg))
        self.base_input(page.zztp_cjjg, zztp_cjjg)

    # 藏品鉴定界面-点击是否征集_是勾选栏
    def page_click_zztp_zj_yes(self):
        log.info('藏品鉴定界面-点击是否征集_是勾选栏')
        self.base_click(page.zztp_zj_yes)

    # 关联合同界面-点击请选择关联合同按钮
    def page_click_select_rules_btn(self):
        log.info('关联合同界面-点击请选择关联合同按钮')
        self.base_click(page.select_rules_btn)

    # # 拨库界面-输入目标库房并选择下拉框第一个
    # def page_input_aim_warehouse(self, aim_warehouse):
    #     self.base_click(page.aim_warehouse)
    #     self.base_input(page.aim_warehouse, aim_warehouse)
    #     self.base_keys(page.aim_warehouse)
    #
    # # 拨库界面-输入藏品分类并选择下拉框第一个
    # def page_input_collectible_classify(self, collectible_classify):
    #     self.base_click(page.collectible_classify)
    #     self.base_input(page.collectible_classify, collectible_classify)
    #     self.base_keys(page.collectible_classify)

    # 拨库界面-点击二次拨库按钮
    def page_click_two_warehouse_btn(self):
        log.info('拨库界面-点击二次拨库按钮')
        self.base_click(page.two_warehouse_btn)

    # 新增-组合业务方法
    def page_list_add(self, name, person):
        log.info('正在调用线索录入-新增方法，线索名：{}，指派人{}'.format(name, person))
        self.page_click_add_btn()
        self.page_input_add_thread_name(name)
        self.page_input_designated_person(person)
        self.page_click_save_btn()
        self.page_click_cancel_btn()
        sleep(1)

    # 线索查询-组合业务方法
    def page_list_search(self, name):
        log.info('正在调用线索查询-组合业务方法,线索名：{}'.format(name))
        self.page_input_thread_name(name)
        self.page_click_search_btn()
        sleep(2)

    # 编辑-组合业务方法
    def page_list_edit(self, name):
        log.info('正在调用编辑-组合业务方法,修改后的名字：{}'.format(name))
        self.page_click_list_operate_btn()
        sleep(1)
        self.page_input_add_thread_name(name)
        self.page_click_save_btn()
        self.page_click_close_btn()
        sleep(1)

    # 批量指派-组合业务方法
    def page_batch_assigned(self):
        log.info('正在调用批量指派-组合业务方法')
        self.page_click_list1_select_btn()
        self.page_click_batch_assigned_btn()
        sleep(1)
        self.page_click_yes_btn()
        sleep(1)

    # 废弃-组合业务方法
    def page_list_abandon(self, cause):
        log.info('正在调用废弃-组合业务方法,原因：{}'.format(cause))
        self.page_click_list1_select_btn()
        self.page_click_abandon_btn()
        self.page_input_cause(cause)
        self.page_click_confirm_btn()
        sleep(1)
        self.page_click_yes_btn()
        sleep(1)

    # 导出-组合业务方法
    def page_list_export(self):
        log.info('正在调用导出-组合业务方法')
        sleep(1)
        self.page_click_export_btn()
        self.page_click_input_select_all()
        self.page_click_input_right_button()
        self.page_click_two_export_btn()
        sleep(10)

    # 查看线索-组合业务方法
    def page_list_check(self):
        log.info('正在调用查看线索-组合业务方法')
        self.page_click_list_operate_btn()
        sleep(1)
        value = self.page_get_thread_name()
        self.page_click_close_btn()
        return value

    # 导入-组合业务方法
    def page_file_import(self, file):
        log.info('正在调用导入-组合业务方法,文件名：{}'.format(file))
        self.page_click_import_btn()
        self.page_input_select_file_btn(file)
        sleep(1)
        self.page_click_two_import_btn()
        sleep(1)
        self.page_click_close_btn()
        sleep(1)

    # 终止-组合业务方法
    def page_end(self, c_time, cause):
        log.info('正在调用终止-组合业务方法,终止时间：{}，原因：{}'.format(c_time, cause))
        self.page_click_list1_select_btn()
        self.page_click_end_btn()
        self.page_input_c_time(c_time)
        sleep(1)
        self.page_click_time_now_btn()
        self.page_input_cause(cause)
        self.page_click_confirm_btn()
        sleep(1)
        self.page_click_yes_btn()
        sleep(1)

    # 填写日志-组合业务方法
    def page_write_log(self, c_time, xs_log):
        log.info('正在调用填写日志-组合业务方法,时间：{}，日志：{}'.format(c_time, xs_log))
        self.page_click_list_operate_btn()
        self.page_input_c_time(c_time)
        sleep(1)
        self.page_click_time_now_btn()
        self.page_input_xs_log(xs_log)
        self.page_click_log_add_btn()
        msg = self.page_if_exist_not_log()
        self.page_click_close_btn()
        sleep(1)
        return msg

    # 完成跟踪-组合业务方法
    def page_trace_over(self):
        log.info('正在调用完成跟踪-组合业务方法')
        self.page_click_list1_select_btn()
        self.page_click_trace_over_btn()
        sleep(1)
        self.page_click_yes_btn()
        sleep(1)

    # 新增征集单-组合业务方法
    def page_form_add(self, form_name, xs_name):
        log.info('正在调用新增征集单-组合业务方法,征集单名：{}，线索名：{}'.format(form_name, xs_name))
        self.page_click_add_zjd_btn()
        self.page_input_form_name(form_name)
        self.page_input_form_xs_name(xs_name)
        self.page_click_save_btn()
        sleep(1)

    # 新增藏品-组合业务方法
    def page_collection_add(self, for_form, add_collection_name):
        log.info('正在调用新增藏品-组合业务方法,征集单：{}，藏品名：{}'.format(for_form, add_collection_name))
        self.page_click_add_btn()
        self.page_input_for_form(for_form)
        self.page_input_add_collection_name(add_collection_name)
        sleep(1)
        self.page_click_confirm_btn()
        self.page_click_close_btn()
        sleep(1)

    # 查询藏品-组合业务方法
    def page_collection_search(self, collection_name):
        log.info('正在调用查询藏品-组合业务方法,藏品名：{}'.format(collection_name))
        self.page_input_collection_name(collection_name)
        self.page_click_search_btn()
        sleep(2)

    # 编辑藏品-组合业务方法
    def page_collection_edit(self, collection_name):
        log.info('正在调用编辑藏品-组合业务方法,修改后的名称：{}'.format(collection_name))
        self.page_click_list_operate_btn()
        sleep(1)
        self.page_input_add_collection_name(collection_name)
        self.page_click_collection_confirm_btn()
        self.page_click_close_btn()
        sleep(1)

    # 查看藏品-组合业务方法
    def page_check_collection(self):
        log.info('正在调用查看藏品-组合业务方法')
        self.page_click_list_operate_btn()
        sleep(1)
        value = self.page_get_collection_name()
        self.page_click_close_btn()
        return value

    # 删除-组合业务方法
    def page_collection_delete(self):
        log.info('正在调用删除-组合业务方法')
        self.page_click_list1_select_btn()
        self.page_click_delete_btn()
        sleep(1)
        self.page_click_yes_btn()
        sleep(1)

    # 提交征集-组合业务方法
    def page_submit_collect(self):
        log.info('正在调用提交征集-组合业务方法')
        self.page_click_list1_select_btn()
        self.page_click_submit_collect_btn()
        sleep(1)
        self.page_click_yes_btn()
        sleep(1)

    # 终止-组合业务方法
    def page_collect_over(self, cause):
        log.info('正在调用终止-组合业务方法,原因：{}'.format(cause))
        self.page_click_list1_select_btn()
        self.page_click_end_btn()
        self.page_input_cause(cause)
        self.page_click_confirm_btn()
        sleep(1)
        self.page_click_yes_btn()
        self.page_click_two_confirm_btn()
        self.page_click_close_btn()
        sleep(1)

    # 藏品鉴定-组合业务方法
    def page_collect_authenticate(self,
                                  zjxm1, zjzc1, szdw1, pdrq1, gjfw1,
                                  jbr2, jbrdw2, pdrq2, gjfw2,
                                  jbr3, jbrdw3, pdrq3, gjfw3,
                                  jbr4, jbrdw4, tprq4, qdjg4,
                                  jbr5, jbrdw5, pfr5, pfrq5, pfjg5,
                                  jbr6, jbrdw6, tprq6, cjjg6):
        log.info('正在调用藏品鉴定-组合业务方法')
        self.page_click_list_operate_btn()
        self.page_click_jd_ps_btn()
        sleep(1)
        self.page_click_a_zjjd()
        self.page_input_zjjd_zjxm(zjxm1)
        self.page_input_zjjd_zjzc(zjzc1)
        self.page_input_zjjd_szdw(szdw1)
        self.page_input_zjjd_pdrq(pdrq1)
        self.page_click_a_zjjd()
        self.page_input_zjjd_gjfw(gjfw1)
        sleep(1)
        self.page_click_a_zjjdjg()
        self.page_input_zjjdjg_jbr(jbr2)
        self.page_input_zjjdjg_jbrdw(jbrdw2)
        self.page_input_zjjdjg_pdrq(pdrq2)
        self.page_input_zjjdjg_gjfw(gjfw2)
        self.page_click_a_zjjdjg()
        sleep(2)
        self.page_click_zjjdjg_zj_yes()
        sleep(2)
        self.page_click_a_gnpsjg()
        self.page_input_gnpsjg_jbr(jbr3)
        self.page_input_gnpsjg_jbrdw(jbrdw3)
        self.page_input_gnpsjg_pdrq(pdrq3)
        self.page_input_gnpsjg_gjfw(gjfw3)
        self.page_click_a_gnpsjg()
        sleep(2)
        self.page_click_gnpsjg_zj_yes()
        sleep(2)
        self.page_click_a_mjtp()
        self.page_input_mjtp_jbr(jbr4)
        self.page_input_mjtp_jbrdw(jbrdw4)
        self.page_input_mjtp_tprq(tprq4)
        self.page_input_mjtp_qdjg(qdjg4)
        self.page_click_a_mjtp()
        sleep(2)
        self.page_click_mjtp_yz_yes()
        sleep(2)
        self.page_click_mjtp_fz_yes()
        sleep(2)
        self.page_click_a_ldpf()
        self.page_input_ldpf_jbr(jbr5)
        self.page_input_ldpf_jbrdw(jbrdw5)
        self.page_input_ldpf_pfr(pfr5)
        self.page_input_ldpf_pfrq(pfrq5)
        self.page_input_ldpf_pfjg(pfjg5)
        self.page_click_a_ldpf()
        sleep(2)
        self.page_click_ldpf_zj_yes()
        sleep(2)
        self.page_click_a_zztp()
        self.page_input_zztp_jbr(jbr6)
        self.page_input_zztp_jbrdw(jbrdw6)
        self.page_input_zztp_tprq(tprq6)
        self.page_input_zztp_cjjg(cjjg6)
        self.page_click_a_zztp()
        sleep(2)
        self.page_click_zztp_zj_yes()
        sleep(2)
        self.page_click_save_btn()
        self.page_click_close_btn()
        sleep(1)

    # 提交确认征集-组合业务方法
    def page_submit_confirm_collect(self):
        log.info('正在调用提交确认征集-组合业务方法')
        self.page_click_list1_select_btn()
        self.page_click_submit_confirm_collect_btn()
        sleep(1)
        self.page_click_yes_btn()
        sleep(1)

    # 关联合同-组合业务方法
    def page_association_rules(self, file_name_path):
        log.info('正在调用关联合同-组合业务方法,文件名：{}'.format(file_name_path))
        self.page_click_list1_select_btn()
        self.page_click_association_rules_btn()
        sleep(1)
        self.page_input_select_file_btn(file_name_path)
        sleep(2)
        self.page_click_close_btn()
        sleep(1)

    # 取消关联合同-组合业务方法
    def page_cancle_association_rules(self):
        log.info('正在调用取消关联合同-组合业务方法')
        self.page_click_list1_select_btn()
        self.page_click_cancle_association_rules_btn()
        sleep(1)
        self.page_click_yes_btn()
        sleep(1)

    # 提交拨库-组合业务方法
    def page_submit_warehouse(self):
        log.info('正在调用提交拨库-组合业务方法')
        self.page_click_list1_select_btn()
        self.page_click_submit_warehouse_btn()
        sleep(1)
        self.page_click_yes_btn()
        sleep(1)

    # 拨库-组合业务方法
    def page_warehouse(self):
        log.info('正在调用拨库-组合业务方法')
        self.page_click_list1_select_btn()
        self.page_click_warehouse_btn()
        # self.page_input_aim_warehouse(aim_warehouse)
        # self.page_input_collectible_classify(collectible_classify)
        sleep(1)
        self.page_click_two_warehouse_btn()
        sleep(1)
        self.page_click_yes_btn()
        sleep(1)
