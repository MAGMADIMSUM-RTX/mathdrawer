# 数学绘图工具 <font size=3>——以硅光电池实验为例</font>

### Interview

为了快速绘制科学图像，笔者以硅光电池的实验数据为例，写了这个工具。数据仅供参考，严禁直接将源码的数据作为作业提交。
若出现任何学术不端行为，笔者概不负责。

![image](https://github.com/user-attachments/assets/7f7815c7-9da8-42b9-8de4-21e3376f28fd)

### Get Start

1. 克隆仓库到本地：

   ```bash 
   git clone https://github.com/MAGMADIMSUM-RTX/mathdrawer.git   
   ```

   ![image](https://github.com/user-attachments/assets/6f63d440-f828-470b-8614-24f939cb4708)

2. 安装 python 绘图包:

   ```bash 
   pip install numpy     
   pip install pandas 
   pip install matplotlib   
   ```

3. 在 mathdrawer 目录下运行

   ```bash
   cd mathdrawer
   python tab.py
   ```

   ![image](https://github.com/user-attachments/assets/7f0de53e-17b4-4a55-9802-02948b4b92d9)

### 修改数据：

- 打开 dat.xslx

  ![image](https://github.com/user-attachments/assets/e9506ab7-7b6b-41db-8711-c87ba5e4e6b6)

- Sheet1-Sheet6 的内容分别为

  - 单晶硅电池的暗伏安特性
  - 非晶硅电池的暗伏安特性
  - 单晶硅电池的开路电压与短路电流随光强变化关系
  - 非晶硅电池的开路电压与短路电流随光强变化关系
  - 单晶硅电池的输出特性
  - 非晶硅电池的输出特性

## OK，那么现在开始，你就可以尽情修改 Code，绘制属于自己的科学图像啦

### 都看到这了，给项目点个 Star 吧 😘
