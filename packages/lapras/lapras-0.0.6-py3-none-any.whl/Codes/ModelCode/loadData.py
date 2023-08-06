import os
import random as rand
import sys
import numpy as np
import pandas as pd
from DealConfig import makeModelDataFillnaFileName, OnlyModelDataFillnaFileName
from Codes.ModelCode.DealParamConfig import params
from Settings import col_head


def get_only_model_data():
    param_list = col_head + params
    df_data = pd.read_csv(makeModelDataFillnaFileName)
    df_data = df_data.dropna(how='all')
    df_data[param_list].to_csv(OnlyModelDataFillnaFileName, index=None, encoding='utf-8')


def load_data(path):
    companylist = list()
    f=open(path)

    data=[]
    columns = list()
    for index_l, line in enumerate(f):
        if index_l==0:
            columns = line
            continue

        cols=line.strip().split(',')
        companylist.append(cols[0])

        line_data=[float(x) for x in cols[2:]]

        line_data.append(float(cols[1]))

        data.append(line_data)
    f.close
    return np.array(data), columns.split(','), companylist





def rankData(data, dim, bond, woe):
    data_dim = data[:, dim]
    m = data_dim.shape[0]
    b = bond.shape[0]
    eps = 1e-8
    for i in range(m):
        xi = float(data_dim[i])
        bond_index = -1
        for j in range(b - 1):
            if (j < b - 2 and xi > bond[j] - eps and xi < bond[j + 1]) or (
                                j == b - 2 and xi > bond[j] - eps and xi < bond[j + 1] + eps):
                bond_index = j
        data_dim[i] = woe[bond_index]
    return data


def getTrainTest(data, sep=-1):
    if sep == -1:
        np.random.shuffle(data)
        sep = int(data.shape[0] * 0.7)
    trainx = data[:sep, :-1]
    trainy = data[:sep, -1]
    testx = data[sep:, :-1]
    testy = data[sep:, -1]
    return 1. * trainx, 1. * trainy, 1. * testx, 1. * testy


if __name__ == '__main__':
    # a = ['1', '2', '3']
    # print str(a[:-1])[1:-1].replace('\'', '')
    # print str([0 for i in range(3)])[1:-1]
    # a = np.array([[1, 2], [2, 3]])
    # print a.tolist()
    # x = 27
    # y = 100.000001
    # print x < y
    print (-np.inf - 3)
