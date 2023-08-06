# coding:utf-8

from ModelConfig import bin_params_dict
from ModelConfig import  minLeaf, treeDepth, bucketnum

params = list(bin_params_dict.keys())
bin_params =  [bin_params_dict.get(para) for para in params]