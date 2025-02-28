# Python Script, API Version = V21
# USAGE
# 使用前需要将点 移到新组建 or Move to New Component
# 输出点的三维坐标,其中保留4位有效数字，SI单位
# Export 3D coordination in 4 declinal places
# Memorise_Xuxu
# memorisexuxu@outlook.com
#
  
# Get the root part
part = GetRootPart()
print part.GetName()

# Get the bodies directly under the root part
bodies = part.GetBodies()
allComponent = part.GetAllComponents()
for comp in allComponent:
    print comp.GetName()
    points_in_group = comp.GetAllDatumPoints()
    print points_in_group.Count
    for point_group in points_in_group:
        # x = point_group.Position[0] [0]=x [1]=y [2]=z
        print('{:.4f}, {:.4f}, {:.4f}'.format(point_group.Position[0], point_group.Position[1], point_group.Position[2]))
    print("\n")
        
print "Finished"