import tkinter as tk
import platform
import os
import psutil
import GPUtil
import socket
import requests
import subprocess

def get_system_info():
    system_info = f"操作系统: {platform.system()} {platform.version()}\n"
    system_info += f"处理器: {platform.processor()}\n"
    system_info += f"Python版本: {platform.python_version()}\n"
    
    # 检查 Node.js 是否已安装
    try:
        node_version = subprocess.check_output(["node", "--version"], stderr=subprocess.STDOUT).decode().strip()
        system_info += f"Node.js版本: {node_version}\n"
    except FileNotFoundError:
        system_info += "Node.js未安装\n"
    
    # 检查 Java 是否已安装
    try:
        java_version = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT).decode().strip()
        system_info += f"Java版本: {java_version}\n"
    except FileNotFoundError:
        system_info += "Java未安装\n"
    
    # 检查 MySQL 是否已安装
    try:
        mysql_version = subprocess.check_output(["mysql", "--version"], stderr=subprocess.STDOUT).decode().strip()
        system_info += f"MySQL版本: {mysql_version}\n"
    except FileNotFoundError:
        system_info += "MySQL未安装\n"
    
    # 检查 PHP 是否已安装
    try:
        php_version = subprocess.check_output(["php", "--version"], stderr=subprocess.STDOUT).decode().strip()
        system_info += f"PHP版本: {php_version}\n"
    except FileNotFoundError:
        system_info += "PHP未安装\n"
    
    # 检查 Nginx 是否已安装
    try:
        nginx_version = subprocess.check_output(["nginx", "-v"], stderr=subprocess.STDOUT).decode().strip()
        system_info += f"Nginx版本: {nginx_version}\n"
    except FileNotFoundError:
        system_info += "Nginx未安装\n"
    
    # 检查 Apache 是否已安装
    try:
        apache_version = subprocess.check_output(["httpd", "-v"], stderr=subprocess.STDOUT).decode().strip()
        system_info += f"Apache版本: {apache_version}\n"
    except FileNotFoundError:
        system_info += "Apache未安装\n"
    
    return system_info

def get_cpu_info():
    cpu_info = f"物理CPU数量: {psutil.cpu_count(logical=False)}\n"
    cpu_info += f"逻辑CPU数量: {psutil.cpu_count(logical=True)}\n"
    cpu_info += f"CPU使用率: {psutil.cpu_percent()}%\n"
    return cpu_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    gpu_info = ""
    for i, gpu in enumerate(gpus):
        gpu_info += f"显卡{i}: {gpu.name}\n"
    return gpu_info

def get_network_info():
    network_info = f"主机名: {socket.gethostname()}\n"
    network_info += f"IP地址: {socket.gethostbyname(socket.gethostname())}\n"
    network_info += f"公网IP地址: {requests.get('https://api.ipify.org').text}\n"
    return network_info

def update_info():
    system_text.set(get_system_info())
    cpu_text.set(get_cpu_info())
    gpu_text.set(get_gpu_info())
    network_text.set(get_network_info())
    root.after(1000, update_info)

root = tk.Tk()
root.title("小恒工具：系统信息1.0")
root.geometry("1200x500")  # 设置窗口大小

system_text = tk.StringVar()
system_label = tk.Label(root, textvariable=system_text)
system_label.pack()

cpu_text = tk.StringVar()
cpu_label = tk.Label(root, textvariable=cpu_text)
cpu_label.pack()

gpu_text = tk.StringVar()
gpu_label = tk.Label(root, textvariable=gpu_text)
gpu_label.pack()

network_text = tk.StringVar()
network_label = tk.Label(root, textvariable=network_text)
network_label.pack()

author_label = tk.Label(root, text="\n大家好，我是作者恒，欢迎使用这个小工具1.0版本，该工具会在GitHub上开源，使用方法：放u盘或硬盘里，即插即用，快速了解本地情况。我说说实现原理：\n导入所需的库：如 tkinter(用于创建图形界面)、platform(用于获取系统信息)、psutil(用于获取CPU信息)、GPUtil(用于获取GPU信息)、socket(用于获取网络信息)和 requests(用于获取公网IP地址)。\n定义获取信息的函数：接下来定义函数,用于获取系统、CPU、GPU和网络信息。分别是 get_system_info()、get_cpu_info()、get_gpu_info() 和 get_network_info()。\n定义更新信息的函数update_info() ，它会调用获取信息的函数,并将返回的信息设置到相应的 StringVar 变量中,使用 root.after(1000, update_info) 来每隔1秒调用一次自身,以便实时更新信息。\n创建图形界面：我们使用 tkinter 库创建了一个简单的图形界面,包括一个窗口和四个标签。分别用于显示系统信息、CPU信息、GPU信息和网络信息。")
author_label.pack()

update_info()
root.mainloop()