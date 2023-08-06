# coding:utf-8

from lapras.ReportCode.SingleParamAnalyze import show_mutil, show_single
from lapras.ModelCode.main import run_model
from lapras.DealConfig import singleModelName, ParamsShow
from lapras.ReportConfig import score_bond
from lapras.ReportCode.ShowModelResult import show_model_pic
from lapras.model_performance import performance


'''
运行代码主文件

使用时请注释掉不需要运行的行
'''

if __name__ == '__main__':

    '''
    建模 
    '''
    '''     决策树分箱 '''
    run_model("model_data.csv",run_type_cus=0)
    '''     手动分箱 确认分箱 '''
    # run_model(run_type_cus=1)
    '''     确认分箱 循环跑 寻找较优解 '''
    # run_model(run_type_cus=2)


    ''' 
    报告分析 
    '''
    # show_single(singleModelName, ParamsShow)  #单变量批量查看

    # show_mutil(singleModelName)   #单变量全部查看


    ''' 
    整体建模报告查看 
    '''
    # show_model_pic(score_bond)

    ''' 
    模型效果查看 
    '''
    # performance()

