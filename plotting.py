import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# plt.rcdefaults()

plt.ylabel('Pesos')
plt.xlabel('Month')
x = months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug',
          'Sept', 'Oct', 'Nov', 'Dec']
y = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3932.0, 6835.0, 4623.0, 3394.0, 0.0, 0.0]
sns.set_style('darkgrid')
sns.barplot(x, y)
sns.set()
plt.title('Monthly food expenses')
plt.show()



# fig = plt.figure()
# ax = fig.add_subplot(111)
#
# ## the data
# N = 5
# menMeans = [18, 35, 30, 35, 27]
# menStd =   [2, 3, 4, 1, 2]
# womenMeans = [25, 32, 34, 20, 25]
# womenStd =   [3, 5, 2, 3, 3]
#
# ## necessary variables
# ind = np.arange(N)                # the x locations for the groups
# width = 0.35                      # the width of the bars
#
# ## the bars
# rects1 = ax.bar(ind, menMeans, width,
#                 color='black',
#                 yerr=menStd )
#
# # rects2 = ax.bar(ind+width, womenMeans, width,
# #                     color='red',
# #                     yerr=womenStd,
# #                     error_kw=dict(elinewidth=2,ecolor='black'))
#
# # axes and labels
# ax.set_xlim(-width,len(ind)+width)
# ax.set_ylim(0,45)
# ax.set_ylabel('Costs')
# ax.set_title('Food costs')
# xTickMarks = ['Group'+str(i) for i in range(1,6)]
# ax.set_xticks(ind+width)
# xtickNames = ax.set_xticklabels(xTickMarks)
# plt.setp(xtickNames, rotation=45, fontsize=10)
#
# # plt.bar(range(len(months)), totals)
# plt.xlabel('Months')
# plt.ylabel('Price $$$')
# plt.show()
#
# ## add a legend
# # ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
#
# plt.show()
# # Save the figure as png
# # bbox_inches='tight' removes all extra whitespace on the edges
# plt.savefig('./plotting.png', bbox_inches='tight')
