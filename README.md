# know-your-computer-faster
一个应用程序，快速显示电脑系统信息，cpu，显卡，网络，各种环境变量信息
## Hollo，l am Heng
![image](https://github.com/lmliheng/know-your-computer-faster/blob/main/readme.png)
## 说一下这个小玩意
大家好，我是作者恒，欢迎使用这个小工具1.0版本，该工具会在GitHub上开源，使用方法:放u盘或硬盘里，即插即用，快速了解本地情况。我说说实现原理:
导入所需的库:如tkinter(用于创建图形界面)、platform(用于获取系统信息)、psutil(用于获取CPU信息)、GPUtil(用于获取GPU信息)、socket(用于获取网络信息)和requests(用于获取公网IP地址)。
定义获取信息的函数:接下来定义函数,用于获取系统、CPU、GPU和网络信息。分别是get_system_info0、get_cpu_info0、get_gpu_info0和 get_network_info().
定义更新信息的函数update_info0，它会调用获取信息的函数,并将返回的信息设置到相应的StringVar 变量中,使用root.after(1000,update_info)来每隔1秒调用一次自身,以便实时更新信息。
创建图形界面:我们使用tkinter库创建了一个简单的图形界面,包括一个窗口和四个标签。分别用于显示系统信息、CPU信息、GPU信息和网络信息。
