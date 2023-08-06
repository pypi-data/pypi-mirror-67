# coding:utf-8

import numpy as np
import scipy.optimize as opt
from lapras.ModelCode.utils import cost


def startTrain(trainx, trainy, lamb, type='logistic'):
    m = trainx.shape[0]
    n = trainx.shape[1] + 1
    # print m,n
    X = np.column_stack((np.ones((m, 1), dtype=float), trainx))
    # print X
    y = trainy
    min_J = np.inf
    min_theta = np.zeros(n)
    eps = 0.1
    if type == 'logistic':
        f = cost.f_logistic
        fgrad = cost.fgrad_logistic
    elif type == 'linear':
        f = cost.f_linear
        fgrad = cost.fgrad_linear
    for i in range(30):
        init_theta = np.random.rand(n) * 2.0 * eps - eps
        # print init_theta
        theta = opt.fmin_cg(f, init_theta, fprime=fgrad, args=(X, y, lamb), disp=False)
        # print theta
        J = f(theta, X, y, lamb)
        if J < min_J:
            min_J = J
            min_theta = theta
    return min_theta


if __name__ == '__main__':
    # x = np.ones((3, 1), dtype=int)
    # print np.asarray(x)


    # def f(x):
    #     a = x[0]
    #     b = x[1]
    #     return (a + b) ** 2 + 10


    # def fGrad(x):
    #     a = x[0]
    #     b = x[1]
    #     return np.mat('%s;%s' % (2 * (a + b), 2 * (a + b)))


    # init_x = np.mat('3;3').T
    # print init_x
    # print fGrad(init_x).T
    # res = opt.fmin_cg(f, init_x, fprime=fGrad)
    # print res

    trainx = np.array([[1], [2], [3], [4], [5], [6]])
    m = trainx.shape[0]
    trainy = np.array([1, 1, 1, 0, 0, 0])
    theta = startTrain(trainx, trainy, 0)
    print (cost.sigmoidFunction(np.column_stack((np.ones((m, 1), dtype=float), trainx)), theta))
    print (theta)
