# coding:utf-8


from lapras.ReportConfig import score_bond
from lapras.ReportCode.ShowModelResult import show_model_pic
from lapras.ModelCode.main import run_model
import toad

'''
运行代码主文件

使用时请注释掉不需要运行的行
'''
def IV(datafilepath):
    if datafilepath is None:
        print("please enter data file path.")
    else:
        run_model(datafilepath,run_type_cus=0)


if __name__ == '__main__':
    IV("model_data.csv")
    toad.IV()