# JGM Automator

> 这是基于 OpenCV 模板匹配的《家国梦》游戏自动化脚本。


## 安装与运行
以下命令中，python是指python3，使用Linux而且默认python2的同学自行修改命令。Windows请无视本行。
```bash
# 安装依赖
python -m pip install uiautomator2 opencv

# adb 连接
# 使用 MuMu 模拟器，确保屏幕大小为 1920（长） * 1080（宽）
adb connect 127.0.0.1:7555

# 获取 device 名称,并填写至 main.py
adb devices

# 在已完成 adb 连接后，在手机安装 ATX 应用
python -m uiautomator2 init

# 打开 ATX ，点击“启动 UIAutomator”选项，确保 UIAutomator 是运行的。

# 进入游戏页面，启动自动脚本。
python main.py
```

## 说明

+ 建筑编号

<img src="./assets/Screenshot.png" style="zoom:40%" />

+ Weditor

我们可以使用 Weditor 工具，获取屏幕坐标，以及在线编写自动化脚本。

```bash
# 安装依赖
python -m pip install --pre weditor

# 启动 Weditor
python -m weditor
```


-------------
偷懒 - 不想使用模拟器，不想修改屏幕坐标，又没有1920x1080分辨率的手机，可以使用adb修改设备的分辨率。
```bash
adb shell wm size 1080x1920
adb shell wm density 240 （可选）
```

如果通过adb修改了分辨率，可以通过以下命令将手机分辨率改回去。
```bash
adb shell wm size reset
adb shell wm density reset
```
