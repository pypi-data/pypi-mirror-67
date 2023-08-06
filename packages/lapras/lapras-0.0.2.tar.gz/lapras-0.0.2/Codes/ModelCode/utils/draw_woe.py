# coding:utf-8

import matplotlib.pyplot as plot
from matplotlib.ticker import  MultipleLocator

def woe_draw(bond, sum_bad_percent, count_good):
    ks_bucket_x = [i + 1.5 for i in range(len(bond) - 1)]
    bond = list(bond)
    bond.insert(0, '0')
    ks_bucket_num = [i / 2 for i in range(2, int(ks_bucket_x[-1] * 2) + 2)]

    fig = plot.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(ks_bucket_x, sum_bad_percent, marker="*", linewidth=3, color="orange")

    for i, (_x, _y) in enumerate(zip(ks_bucket_x, sum_bad_percent)):
        plot.text(_x, _y, sum_bad_percent[i], color='black', fontsize=10, )

    ax1.set_ylim(bottom=-5, top=15)
    ax1.set_title('Trend Of Feature')

    ax1.set_xticks(ks_bucket_num)
    ax1.set_xticklabels(bond, fontsize=12)
    xmajorLocator = MultipleLocator(1)
    ax1.xaxis.set_major_locator(xmajorLocator)

    ax1.legend(["woe"], loc="upper right")
    ax1.grid(True)
    ax2 = ax1.twinx()
    plot.bar(ks_bucket_x, count_good, alpha=0.3, color='blue', label='count_good')
    ax2.set_ylim(bottom=0, top=1000000)  # [9.0, 1.0, 875440.0]
    ax2.legend(loc=2)
    plot.show()
