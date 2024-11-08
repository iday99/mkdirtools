from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                           QTextEdit, QPushButton, QFileDialog,
                           QMessageBox,QMenuBar,QMenu)
from PyQt6.QtCore import Qt
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("目录生成工具")
        self.setMinimumSize(600, 400)
        self.create_menu_bar()
        # 创建中心部件和布局
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        
        # 创建文本编辑框
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("请粘贴目录结构，格式如：\nproject/\n├── src/\n│   ├── gui/")
        layout.addWidget(self.text_edit)
        
        # 创建按钮
        self.generate_btn = QPushButton("选择目标目录并生成")
        self.generate_btn.clicked.connect(self.generate_structure)
        layout.addWidget(self.generate_btn)
        
        self.setCentralWidget(central_widget)
    def create_menu_bar(self):
        menubar = self.menuBar()
        
        # 创建帮助菜单
        help_menu = menubar.addMenu("帮助")
        
        # 创建关于动作
        about_action = help_menu.addAction("关于")
        about_action.triggered.connect(self.show_about_dialog)
    
    def show_about_dialog(self):
        QMessageBox.about(
            self,
            "关于目录生成工具",
            """<h3>目录生成工具 v1.0.0</h3>
            <p>一个用于生成目录结构的图形界面工具。</p>
            <p>功能特点：</p>
            <ul>
                <li>快速根据目录层级生成目录和文件。</li>
                <li>UTF-8编码支持</li>
            </ul>
            <p>作者：爱文明</p>
            <p>项目地址：<a href="https://github.com/yourusername/mkdirtools">GitHub</a></p>
            <p>个人博客：<a href="http://www.aiwenming.com">主页</a></p>
            <p>Copyright © 2024</p>"""
        )
    def generate_structure(self):
        # 选择目标目录
        target_dir = QFileDialog.getExistingDirectory(self, "选择目标目录")
        if not target_dir:
            return
            
        # 解析文本内容
        content = self.text_edit.toPlainText()
        structure = self.parse_structure(content)
        
        # 生成目录和文件
        self.create_structure(target_dir, structure)
    
    def parse_structure(self, content):
        structure = {}
        current_path = []
        
        for line in content.split('\n'):
            line = line.rstrip()
            if not line:
                continue
                
            # 计算缩进级别
            indent = 0
            for char in line:
                if char in ['│', '├', '└']:
                    indent += 1
                else:
                    break
            
            # 提取名称
            name = line.strip('│├└── \t')
            if not name:
                continue
                
            # 更新当前路径
            current_path = current_path[:indent]
            current_path.append(name)
            
            # 更新结构字典
            current_dict = structure
            for path_part in current_path[:-1]:
                current_dict = current_dict.setdefault(path_part, {})
            current_dict[name] = {}
            
        return structure
    
    def create_structure(self, base_path, structure, is_root=True):  # 添加 is_root 参数
        try:
            for name, contents in structure.items():
                path = os.path.join(base_path, name)
                
                if name.endswith('/'):
                    # 创建目录
                    os.makedirs(path, exist_ok=True)
                    # 递归创建子目录/文件，传入 is_root=False
                    self.create_structure(path, contents, is_root=False)
                else:
                    # 创建文件
                    with open(path, 'w', encoding='utf-8') as f:
                        pass
            
            # 只在根调用时显示提示
            if is_root:
                QMessageBox.information(
                    self,
                    "成功",
                    f"目录结构已成功生成到：\n{base_path}",
                    QMessageBox.StandardButton.Ok
                )
        except Exception as e:
            # 错误提示只在根调用时显示
            if is_root:
                QMessageBox.critical(
                    self,
                    "错误",
                    f"生成目录结构时发生错误：\n{str(e)}",
                    QMessageBox.StandardButton.Ok
                )