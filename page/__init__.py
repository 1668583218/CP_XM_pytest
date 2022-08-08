from selenium.webdriver.common.by import By

"""项目配置地址"""
url = "http://prodplus.okaygis.com:8880/#/login"

"""以下为登录界面元素配置信息"""
# 用户名
login_username = By.XPATH, "//label[contains(text(), '登录名')]/following-sibling::div/div/input"
# 密码
login_pwd = By.XPATH, "//label[contains(text(), '密码')]/following-sibling::div/div/input"
# 验证码
# login_ver = By.XPATH, "//input[contains(@placeholder, '请输入验证码')]"
# 登录按钮
login_btn = By.XPATH, "//span[contains(text(), '登录')]"

"""以下为首页界面元素配置信息"""
# 藏品管理
cpgl = By.XPATH, "//span[contains(text(), '藏品管理')]"

"""以下为藏品管理界面元素配置信息"""
# 征集管理
zjgl = By.XPATH, "//span[contains(text(), '征集管理')]"
# 线索录入
xslr = By.XPATH, "//span[contains(text(), '线索录入')]"
# 线索跟踪
xsgz = By.XPATH, "//span[contains(text(), '线索跟踪')]"
# 征集录入
zjlr = By.XPATH, "//span[contains(text(), '征集录入')]"
# 征集中
zjz = By.XPATH, "//span[contains(text(), '征集中')]"
# 确认征集
qrzj = By.XPATH, "//span[contains(text(), '确认征集')]"
# 拨库管理
bkgl = By.XPATH, "//span[contains(text(), '拨库管理')]"

"""以下为二级界面元素配置信息"""
# 已指派
yzp = By.XPATH, "//span[contains(text(), '已指派')]"
# 已废弃
yfq = By.XPATH, "//span[contains(text(), '已废弃')]"
# 已完成
ywc = By.XPATH, "//span[contains(text(), '已完成')]"
# 已终止
yzz = By.XPATH, "//span[contains(text(), '已终止')]"
# 已提交
ytj = By.XPATH, "//span[contains(text(), '已提交')]"
# 已鉴定
yjd = By.XPATH, "//span[contains(text(), '已鉴定')]"
# 已征集
yzj = By.XPATH, "//span[contains(text(), '已征集')]"
# 已拨库
ybk = By.XPATH, "//span[contains(text(), '已拨库')]"

"""以下为列表界面元素配置信息"""
# 线索名称输入框
thread_name = By.XPATH, "//input[@placeholder='线索名称']"
# 藏品名称输入框
collection_name = By.XPATH, "//input[@placeholder='藏品名称']"
# 查询按钮
search_btn = By.XPATH, "//span[contains(text(), '查询')]"
# 重置按钮
reset_btn = By.XPATH, "//span[contains(text(), '重置')]"
# 新增按钮
add_btn = By.XPATH, "//span[contains(text(), '新增')]"
# 导出按钮
export_btn = By.XPATH, "//span[contains(text(), '导出')]"
# 导入按钮
import_btn = By.XPATH, "//button/span[contains(text(), '导入')]"
# 批量指派按钮
batch_assigned_btn = By.XPATH, "//span[contains(text(), '批量指派')]"
# 废弃按钮
abandon_btn = By.XPATH, "//button/span[contains(text(), '废弃')]"
# 完成跟踪按钮
trace_over_btn = By.XPATH, "//span[contains(text(), '完成跟踪')]"
# 终止按钮
end_btn = By.XPATH, "//button/span[contains(text(), '终止')]"
# 添加征集单按钮
add_zjd_btn = By.XPATH, "//div[contains(text(), '添加征集单')]"
# 提交征集按钮
submit_collect_btn = By.XPATH, "//button/span[contains(text(), '提交征集')]"
# 删除按钮
delete_btn = By.XPATH, "//button/span[contains(text(), '删除')]"
# 提交确认征集按钮
submit_confirm_collect_btn = By.XPATH, "//button/span[contains(text(), '提交确认征集')]"
# 关联合同按钮
association_rules_btn = By.XPATH, "(//button/span[contains(text(), '关联合同')])[1]"
# 取消关联合同按钮
cancle_association_rules_btn = By.XPATH, "//button/span[contains(text(), '取消关联合同')]"
# 提交拨库按钮
submit_warehouse_btn = By.XPATH, "//button/span[contains(text(), '提交拨库')]"
# 拨库按钮
warehouse_btn = By.XPATH, "//button/span[contains(text(), '拨库')]"
# # 编辑按钮
# edit_btn = By.XPATH, "(//span[contains(text(), '编辑')])[2]"
# # 查看按钮
# check_btn = By.XPATH, "(//span[contains(text(), '查看')])[2]"
# # 鉴定按钮
# authenticate_btn = By.XPATH, "(//span[contains(text(), '鉴定')])[4]"
# # 日志填写按钮
# log_write_btn = By.XPATH, "(//span[contains(text(), '日志填写')])[2]"
# 列表操作按钮
list_operate_btn = By.XPATH, "(//tbody)[2]/tr[1]/td[contains(@class, 'is-center')]/div/button/span"
# 全选按钮
all_btn = By.XPATH, "(//span[contains(@class, 'el-checkbox__input')])[1]"
# 第一行的选择按钮
list1_select_btn = By.XPATH, "(//span[contains(@class, 'el-checkbox__input')])[2]"
# 提示信息
hint_mes = By.XPATH, "//p[contains(@class, 'el-message__content')]"
# 线索列表第一行第一列
xs_row1_list1 = By.XPATH, "(//tr/td)[2]/div"
# 征集列表第一行第三列
zj_row1_list3 = By.XPATH, "//div[3]/table/tbody/tr[1]/td[4]/div"

"""以下为查看、新增、编辑界面元素配置信息"""
# 线索名称
add_thread_name = By.XPATH, "(//label[contains(text(), '线索名称')]/following-sibling::div/div/input)[2]"
# 指派人
designated_person = By.XPATH, "(//label[contains(text(), '指派人')]/following-sibling::div/div/div/input)[1]"
# 保存按钮
save_btn = By.XPATH, "(//span[contains(text(), '保存')])[1]"
# 关闭按钮
close_btn = By.XPATH, "//button[@class='el-dialog__headerbtn']"
# 取消按钮
cancel_btn = By.XPATH, "//span[contains(text(), '取消')]"

"""以下为废弃界面元素配置信息"""
# 原因输入框
cause = By.XPATH, "//textarea[contains(@class, 'el-textarea__inner')]"
# 确定按钮
confirm_btn = By.XPATH, "//span[contains(text(), '确定')]"
# 时间界面此刻按钮
time_now_btn = By.XPATH, "//span[contains(text(), '此刻')]"

"""以下为导出界面元素配置信息"""
# 二次导出按钮
two_export_btn = By.XPATH, "(//span[contains(text(), '导出')])[5]"
# 选择导出的列全选框
input_select_all = By.XPATH, "((//span[contains(text(), '选择导出的列')])[1]/parent::label/span)[1]"
# 右箭头按钮
input_right_button = By.XPATH, "(//button[contains(@class, 'el-transfer__button')])[2]"

"""以下为导入界面元素配置信息"""
# 选取文件按钮
select_file_btn = By.XPATH, "//input[contains(@type, 'file')]"
# 二次导入按钮
two_import_btn = By.XPATH, "(//span[contains(text(), '导入')])[4]"

"""以下为批量指派界面元素配置信息"""
# 是按钮
yes_btn = By.XPATH, "//span[contains(text(), '是')]"
# 否按钮
no_btn = By.XPATH, "//span[contains(text(), '否')]"

"""以下为终止界面元素配置信息"""
# 时间输入框
c_time = By.XPATH, "//input[contains(@placeholder, '选择日期时间')]"
two_confirm_btn = By.XPATH, "(//span[contains(text(), '确定')])[2]"

"""以下为线索日志界面元素配置信息"""
# 跟踪日志输入框
xs_log = By.XPATH, "(//textarea[contains(@class, 'el-textarea__inner')])[2]"
# 添加按钮
log_add_btn = By.XPATH, "//span[contains(text(), '添加')]"

"""以下为征集单新增、编辑界面元素配置信息"""
# 单名称输入框
form_name = By.XPATH, "//label[contains(text(), '单名称')]/following-sibling::div/div/input"
# 线索名称输入框
form_xs_name = By.XPATH, "//label[contains(text(), '线索名称')]/following-sibling::div/div/div/input"

"""以下为藏品新增、编辑界面元素配置信息"""
# 所属征集单输入框
for_form = By.XPATH, "//label[contains(text(), '所属征集单')]/following-sibling::div/div/div/input"
# 藏品名称输入框
add_collection_name = By.XPATH, "(//label[contains(text(), '藏品名称')]/following-sibling::div/div/input)[2]"
# 确定按钮
collection_confirm_btn = By.XPATH, "(//span[contains(text(), '确定')])[2]"

"""以下为藏品鉴定界面元素配置信息"""
# 鉴定/评审按钮
jd_ps_btn = By.XPATH, "//div[contains(text(), '鉴定/评审')]"

# 专家鉴定标签
a_zjjd = By.XPATH, "(//a[contains(text(), '专家鉴定')])[1]"
# 专家姓名输入框
zjjd_zjxm = By.XPATH, "//label[contains(text(), '专家姓名')]/following-sibling::div/div/input"
# 专家职称输入框
zjjd_zjzc = By.XPATH, "//label[contains(text(), '专家职称')]/following-sibling::div/div/input"
# 所在单位输入框
zjjd_szdw = By.XPATH, "//label[contains(text(), '所在单位')]/following-sibling::div/div/input"
# 评定日期输入框
zjjd_pdrq = By.XPATH, "(//label[contains(text(), '评定日期')]/following-sibling::div/div/input)[1]"
# 估价范围输入框
zjjd_gjfw = By.XPATH, "(//label[contains(text(), '估价范围')]/following-sibling::div/div/input)[1]"

# 专家鉴定结果标签
a_zjjdjg = By.XPATH, "//a[contains(text(), '专家鉴定结果')]"
# 经办人输入框
zjjdjg_jbr = By.XPATH, "(//label[contains(text(), '经办人')]/following-sibling::div/div/input)[1]"
# 经办人单位输入框
zjjdjg_jbrdw = By.XPATH, "(//label[contains(text(), '经办人单位')]/following-sibling::div/div/input)[1]"
# 评定日期输入框
zjjdjg_pdrq = By.XPATH, "(//label[contains(text(), '评定日期')]/following-sibling::div/div/input)[2]"
# 估价范围输入框
zjjdjg_gjfw = By.XPATH, "(//label[contains(text(), '估价范围')]/following-sibling::div/div/input)[2]"
# 是否征集_是勾选栏
zjjdjg_zj_yes = By.XPATH, "(//span[contains(@class, 'el-radio__inner')])[1]"

# 馆内评审结果标签
a_gnpsjg = By.XPATH, "//a[contains(text(), '馆内评审结果')]"
# 经办人输入框
gnpsjg_jbr = By.XPATH, "(//label[contains(text(), '经办人')]/following-sibling::div/div/input)[3]"
# 经办人单位输入框
gnpsjg_jbrdw = By.XPATH, "(//label[contains(text(), '经办人单位')]/following-sibling::div/div/input)[2]"
# 评定日期输入框
gnpsjg_pdrq = By.XPATH, "(//label[contains(text(), '评定日期')]/following-sibling::div/div/input)[3]"
# 估价范围输入框
gnpsjg_gjfw = By.XPATH, "(//label[contains(text(), '估价范围')]/following-sibling::div/div/input)[3]"
# 是否征集_是勾选栏
gnpsjg_zj_yes = By.XPATH, "(//span[contains(@class, 'el-radio__inner')])[3]"

# 卖家谈判标签
a_mjtp = By.XPATH, "//a[contains(text(), '卖家谈判')]"
# 经办人输入框
mjtp_jbr = By.XPATH, "(//label[contains(text(), '经办人')]/following-sibling::div/div/input)[5]"
# 经办人单位输入框
mjtp_jbrdw = By.XPATH, "(//label[contains(text(), '经办人单位')]/following-sibling::div/div/input)[3]"
# 谈判日期输入框
mjtp_tprq = By.XPATH, "(//label[contains(text(), '谈判日期')]/following-sibling::div/div/input)[1]"
# 确定价格输入框
mjtp_qdjg = By.XPATH, "//label[contains(text(), '确定价格')]/following-sibling::div/div/input"
# 是否达成一致_是勾选栏
mjtp_yz_yes = By.XPATH, "(//span[contains(@class, 'el-radio__inner')])[5]"
# 是否需要复制品_是勾选栏
mjtp_fz_yes = By.XPATH, "(//span[contains(@class, 'el-radio__inner')])[7]"

# 领导批复标签
a_ldpf = By.XPATH, "//a[contains(text(), '领导批复')]"
# 经办人输入框
ldpf_jbr = By.XPATH, "(//label[contains(text(), '经办人')]/following-sibling::div/div/input)[7]"
# 经办人单位输入框
ldpf_jbrdw = By.XPATH, "(//label[contains(text(), '经办人单位')]/following-sibling::div/div/input)[4]"
# 批复人输入框
ldpf_pfr = By.XPATH, "//label[contains(text(), '批复人')]/following-sibling::div/div/input"
# 批复日期输入框
ldpf_pfrq = By.XPATH, "//label[contains(text(), '批复日期')]/following-sibling::div/div/input"
# 批复价格输入框
ldpf_pfjg = By.XPATH, "//label[contains(text(), '批复价格')]/following-sibling::div/div/input"
# 是否征集_是勾选栏
ldpf_zj_yes = By.XPATH, "(//span[contains(@class, 'el-radio__inner')])[9]"

# 最终谈判标签
a_zztp = By.XPATH, "//a[contains(text(), '最终谈判')]"
# 经办人输入框
zztp_jbr = By.XPATH, "(//label[contains(text(), '经办人')]/following-sibling::div/div/input)[9]"
# 经办人单位输入框
zztp_jbrdw = By.XPATH, "(//label[contains(text(), '经办人单位')]/following-sibling::div/div/input)[5]"
# 谈判日期输入框
zztp_tprq = By.XPATH, "(//label[contains(text(), '谈判日期')]/following-sibling::div/div/input)[2]"
# 成交价格输入框
zztp_cjjg = By.XPATH, "//label[contains(text(), '成交价格')]/following-sibling::div/div/input"
# 是否征集_是勾选栏
zztp_zj_yes = By.XPATH, "(//span[contains(@class, 'el-radio__inner')])[11]"

"""以下为关联合同界面元素配置信息"""
# 请选择关联合同按钮
select_rules_btn = By.XPATH, "//p[contains(text(), '请选择关联合同')]"

"""以下为拨库界面元素配置信息"""
# 目标库房输入框
aim_warehouse = By.XPATH, "//label[contains(text(), '目标库房')]/following-sibling::div/div/div/input"
# 藏品分类输入框
collectible_classify = By.XPATH, "//label[contains(text(), '藏品分类')]/following-sibling::div/div/div/input"
# 二次拨库按钮
two_warehouse_btn = By.XPATH, "(//button/span[contains(text(), '拨库')])[2]"
