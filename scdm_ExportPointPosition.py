# Python Script, API Version = V21
# USAGE:
# 使用前需要将点 移到新组建 or Move to New Component
# 输出点的三维坐标,其中保留4位有效数字，SI单位
# Export 3D coordination in 4 declinal places
# Memorise_Xuxu
# memorisexuxu@outlook.com
# Code in UTF-8


import time, os
from datetime import datetime

# filename文件名修改,格式为 2025_03_20_131010
# 获取当前时间
current_time = datetime.now()

# 格式化为指定的时间戳字符串
timestamp_str = current_time.strftime("%Y_%m_%d_%H%M")

# 组合成完整文件名
file_name = "{}.txt".format(timestamp_str)

# 获取完整路径
full_path = os.path.join(os.getcwd(), file_name)

# SpaceClaim 部分
#
# 获取整个结果树的instance
part = GetRootPart() 

# 获取所有实体,由于测点不是实体,这里没用到
bodies = part.GetBodies() 

# 由于点已经放进去组件里面,这里需要获取所有组件
allComponents = part.GetAllComponents() 

# 循环所有获取到的组件
for comp in allComponents:
    # 获取其中一个组件的名字
    compName = comp.GetName()
    # 输出组件的名字
    print ("当前组件:" + compName)
    # 获取当前组件中所有的点
    points_in_group = comp.GetAllDatumPoints()
    # 获取点的个数
    point_Num = points_in_group.Count
    # 输出找点的个数
    print ("共有" + str(point_Num) + "个点")
    
    # Fluent监控点脚本
    #
    # Fluent consol命令创建点的命令
    cmdPrefix = 'surface/point-surface'
    # 监控点名字的前缀,如 b-1 b-2,不能遗漏连接符号
    ptNamePrefix = 'ex-'
    # 若没有手动定义旋转轴,就可以将引号内容设置为空 '' 即可
    refAxis = 'global' # 若没有手动定义旋转轴,就可以将引号内容设置为空 '' 即可
    # refAxis = ''
    
    # 遍历单一组件内所有的点
    for point_group in points_in_group:
        # x = point_group.Position[0] [0]=x [1]=y [2]=z
        # 单位为米 Metre
        # 输出所有点的三维坐标,保留小数点后4位
        print('{:.4f} {:.4f} {:.4f}'.format(point_group.Position[0], point_group.Position[1], point_group.Position[2]))
        #print('Index {}: {:.4f} {:.4f} {:.4f}'.format(i, point_group.Position[0], point_group.Position[1], point_group.Position[2]))
    
    print("\n")
    
    # 遍历生成Fluent中创建点的命令
    for i, point_group in enumerate(points_in_group, start=1):
        # x = point_group.Position[0] [0]=x [1]=y [2]=z
        
        # 没有自定义旋转轴,可以默认为global,或为空(代码采用了为空的方式)
        #context = cmdPrefix + " " + ptNamePrefix + str(i)+' '+'{:.4f} {:.4f} {:.4f}'.format(point_group.Position[0], point_group.Position[1], point_group.Position[2])
        #print(cmdPrefix + " " + ptNamePrefix + str(i)+' '+'{:.4f} {:.4f} {:.4f}'.format(point_group.Position[0], point_group.Position[1], point_group.Position[2]))
        
        # 手动定义监控点名字前缀,引用 ptNamePrefix
        #context = cmdPrefix + " " + ptNamePrefix + str(i)+" "+ refAxis +' '+'{:.4f} {:.4f} {:.4f}'.format(point_group.Position[0], point_group.Position[1], point_group.Position[2])
        #print(cmdPrefix + " " + ptNamePrefix + str(i)+" "+ refAxis +' '+'{:.4f} {:.4f} {:.4f}'.format(point_group.Position[0], point_group.Position[1], point_group.Position[2]))
        
        # 使用组件名称,比较推荐,要注意组件名称，这里自动添加了连接符号-
        context = cmdPrefix + " " + compName + '-'+ str(i)+" "+ refAxis +' '+'{:.4f} {:.4f} {:.4f}'.format(point_group.Position[0], point_group.Position[1], point_group.Position[2])
        print(cmdPrefix + " " + compName + '-'+ str(i)+" "+ refAxis +' '+'{:.4f} {:.4f} {:.4f}'.format(point_group.Position[0], point_group.Position[1], point_group.Position[2]))
        
        # 输出Fluent命令,默认情况到用户根目录下C:\User\[用户名]
        with open(file_name, 'a') as file:
            # Write the content to the file
            context_write = context
            file.write(context_write + "\n")
    print("\n")
    
print("文件保存的完整路径:",(full_path) )
print("Finished")
