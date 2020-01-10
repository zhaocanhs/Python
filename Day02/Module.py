# -*- coding:utf-8 -*-
# 作者：火小森

# sys 模块  -go

import sys

# print(sys.path)  #打印环境变量
# print(sys.argv)    #打印相对路径
# print(sys.argv[2])


# sys 模块  -end

# os 模块  -go
import os


cmd_res = os.system ( "dir" )  # 执行命令，不保存结果
print ( cmd_res )

cmd_res1 = os.popen ( "dir" ).read ( )
print ( cmd_res1 )
os.mkdir ( "new_dir" ) #同级下创建了一个名为new_dir的目录文件

# os 模块  -end
