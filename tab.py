import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = 'STFangsong'

fig = plt.figure()
fig.suptitle(r'实验3.18 硅太阳能电池的光照特性', fontsize=18)

sub = fig.add_subplot(221)
df = pd.read_excel('./dat.xlsx', sheet_name='Sheet1')
line1, = sub.plot(df['V'], df['I'], marker='o', markersize=4,  linewidth=2, linestyle='-',
                  color='red')
df2 = pd.read_excel('./dat.xlsx', sheet_name='Sheet2')
line2, = sub.plot(df2['V'], df2['I'], marker='o', markersize=4, linewidth=2,
                  linestyle=':',  color='black')
sub.legend(handles=[line1, line2], labels=[
           '单晶硅', '非晶硅'], loc='best')
sub.grid(which='major')
sub.set_xlabel(r'$V$(V)', fontsize=12, rotation=0, loc='right')
sub.set_ylabel(r'$I$(mA)', fontsize=12, rotation=0,
               loc='top')
sub.set_title(r'硅太阳能电池的$I$-$V$曲线', fontsize=16)
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.1f}'))
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.1f}'))


sub2 = fig.add_subplot(222)
df = pd.read_excel('./dat.xlsx', sheet_name='Sheet3')
line1, = sub2.plot(np.log(df['Iin']), df['V'],  marker='o', markersize=4, linewidth=2,
                   linestyle='-',  color='red')
df2 = pd.read_excel('./dat.xlsx', sheet_name='Sheet4')
line2, = sub2.plot(np.log(df2['Iin']), df2['V'], marker='o', markersize=4, linewidth=2,
                   linestyle=':',  color='black')
sub2.legend(handles=[line1, line2], labels=[
    '单晶硅', '非晶硅'], loc='best')
sub2.grid(which='major')
sub2.set_ylabel(r'$V_{OC}$(V)', fontsize=12, rotation=0, loc='top')
sub2.set_xlabel(r'ln($I_{in}$(mA))', fontsize=12, rotation=0, loc='right')
sub2.set_title(r'硅太阳能电池的$V_{OC}$-ln($I_{in}$)图线', fontsize=16,)
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.1f}'))
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.1f}'))
# sub2.set_ylim(bottom=2.3)


sub3 = fig.add_subplot(223)
df = pd.read_excel('./dat.xlsx', sheet_name='Sheet3')
line1, = sub3.plot(df['Iin'], df['Isc'],  marker='o', markersize=4, linewidth=2,
                   linestyle='-',  color='red')
df2 = pd.read_excel('./dat.xlsx', sheet_name='Sheet4')
line2, = sub3.plot(df2['Iin'], df2['Isc'], marker='o', markersize=4, linewidth=2,
                   linestyle=':',  color='black')
sub3.legend(handles=[line1, line2], labels=[
    '单晶硅', '非晶硅'], loc='best')
sub3.grid(which='major')
sub3.set_ylabel(r'$I_{SC}$(mA)', fontsize=12, rotation=0, loc='top')
sub3.set_xlabel(r'$I_{in}$(mA)', fontsize=12, rotation=0, loc='right')
sub3.set_title(r'硅太阳能电池的$I_{SC}$-$I_{in}$图线', fontsize=16,)
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.1f}'))
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.1f}'))


sub4 = fig.add_subplot(224)
df = pd.read_excel('./dat.xlsx', sheet_name='Sheet5')
line1, = sub4.plot(df['R'], df['I']**2*df['R']/1000, marker='o', markersize=4, linewidth=2,
                   linestyle='-', color='red')

sub4_2 = sub4.twinx()
df2 = pd.read_excel('./dat.xlsx', sheet_name='Sheet6')
line2, = sub4_2.plot(df2['R'], df2['I']**2*df2['R']/1000, marker='o', markersize=4, linewidth=2,
                     linestyle=':', color='black')

sub4.legend(handles=[line1, line2], labels=['单晶硅', '非晶硅'], loc='best')
sub4.grid(which='major')
# sub4.set_ylabel('$I^2R$(mW)\n单晶硅', fontsize=12, labelpad=-10,
#                 rotation=0, loc='top', color='black')
# sub4_2.set_ylabel('$I^2R$(mW)\n非晶硅', fontsize=12, labelpad=40,
#                   rotation=0, loc='top', color='black')
sub4.text(-0.05, 1.0, '$I^2R$(mW)\n单晶硅', fontsize=12, ha='center',
          va='center', transform=sub4.transAxes, color='black')
sub4_2.text(1.05, 1.0, '$I^2R$(mW)\n非晶硅', fontsize=12, ha='center',
            va='center', transform=sub4_2.transAxes, color='black')

sub4.set_xlabel(r'$R$(Ω)', fontsize=12, rotation=0, loc='right')
sub4.set_title(r'硅太阳能电池的功率曲线', fontsize=16)

sub4.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.1f}'))
sub4.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.1f}'))
sub4_2.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y:.1f}'))
sub4.set_ylim(bottom=0)
sub4_2.set_ylim(bottom=0)

plt.show()
plt.close('all')
