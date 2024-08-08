import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from textwrap import wrap

# 读取CSV文件
df = pd.read_csv('product_metaphor_list.csv')

# 创建图形
fig, ax = plt.subplots(figsize=(15, len(df) * 1.2))  # 增加图形大小

# 隐藏坐标轴
ax.axis('off')

# 定义每个单元格的最大宽度（字符数）
max_width = 15

# 处理数据，使其换行
cell_text = []
for row in df.values:
    cell_text.append(['\n'.join(wrap(str(cell), max_width)) for cell in row])

# 创建表格
table = ax.table(cellText=cell_text,
                 colLabels=['\n'.join(wrap(col, max_width)) for col in df.columns],
                 cellLoc='center',
                 loc='center')

# 调整表格样式
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 2)  # 增加行高

# 为每行添加不同的背景色，并调整单元格高度
for i in range(len(df) + 1):  # +1 to include header
    for j in range(len(df.columns)):
        cell = table[i, j]
        cell.set_text_props(wrap=True, va='center')
        if i == 0:  # 标题行
            cell.set_text_props(weight='bold')
            cell.set_facecolor('#4CAF50')
            cell.set_text_props(color='white')
        elif i % 2 == 1:
            cell.set_facecolor('#f0f0f0')
        else:
            cell.set_facecolor('#ffffff')

        # 根据文本行数调整单元格高度
        lines = cell.get_text().get_text().count('\n') + 1
        cell.set_height(cell.get_height() * lines * 0.6)

# 调整布局并显示图形
plt.tight_layout()
plt.show()