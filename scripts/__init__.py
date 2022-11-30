# 原因：运行pytest会提示没有导包，然后这段话是加在test_zjgl中的，写在这里就不用每个文件都写了
# 导包
import os
import sys

sys.path.append(os.getcwd())