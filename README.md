# 目录生成工具 (MkdirTools)

一个使用 PyQt6 开发的图形界面工具，用于快速生成目录结构。

## 功能特点

- 📁 支持多级目录和文件的批量创建
- 🌐 完整的 UTF-8 编码支持
- 🖥️ 直观的图形界面操作
- 📋 支持直接粘贴目录结构
- 🎯 可视化目标目录选择

## 安装方法

1. 确保已安装 Python 3.6 或更高版本
2. 克隆仓库：
```bash
git clone https://github.com/iday99/mkdirtools.git
cd mkdirtools
```

3. 安装依赖：
```bash
pip install -e .
```
## 使用方法

1. 启动程序：
```bash
mkdirtools
```

2. 在文本框中粘贴目录结构，格式如下：
project/
├── src/
│ ├── gui/
│ │ ├── main_window.py
│ │ └── dialogs.py
│ └── utils/
│ ├── config.py
│ └── logger.py
└── main.py


3. 点击"选择目标目录并生成"按钮
4. 选择要生成目录结构的目标位置
5. 程序会自动创建所有目录和文件

## 目录结构格式说明

- 目录必须以 `/` 结尾
- 使用 `├──`、`│` 和 `└──` 表示层级关系
- 不以 `/` 结尾的项目将被创建为文件

## 开发环境

- Python 3.6+
- PyQt6
- 支持 Windows/Linux/MacOS

## 构建项目
```bash
python setup.py sdist bdist_wheel



## 许可证

MIT License

## 作者

- 作者：爱文明
- 博客：[作者博客](http://www.aiwenming.com)
- GitHub：[项目地址](https://github.com/iday99/mkdirtools)

## 贡献

欢迎提交 Issue 和 Pull Request！

## 更新日志

### v1.0.0 (2024-03-xx)
- 🎉 首次发布
- ✨ 实现基本的目录生成功能
- 🎨 添加图形界面
- 📝 支持 UTF-8 编码