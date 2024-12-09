# ProjectPaper
Pick wallpaper from windows' spotlight

### Overview

> [!NOTE]
> 工程使用PyCharm开发，Python 3.12+，主要用于提取Windows的Spotlight壁纸。

### 运行条件

#### 依赖库

无

### 打包

使用**pyinstaller**打包成exe文件，打开**PyCharm**的`Terminal`输入：

```shell
pyinstaller --onefile --name PaperPicker --icon app.ico main.py
```

如果需要在exe文件名中添加版本号、版权、公司等版本信息，可以使用`--version-file`参数，例如：

```shell
pyinstaller --onefile --version-file version.txt --name PaperPicker --icon app.ico main.py
```

### 其他

#### 1.如何更新pip

```shell
python -m pip install --upgrade pip
```

![](https://raw.githubusercontent.com/zhongwcool/ProjectPaper/main/Assets/app-logo.png)