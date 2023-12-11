import sys


from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
)
import subprocess
import webbrowser
import os

def open_vpn():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'resources', 'link_vpn.txt')
    with open(file_path,'r') as file: 
        exe_path = file.readline()
    print(exe_path)
    try:
        subprocess.run(exe_path, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

        
def open_jira():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'resources', 'link_jira.txt')
    with open(file_path,'r') as file: 
        http_link = file.readline()
    webbrowser.open(http_link)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Register Hours")

vpn_button = QPushButton("Open VPN")
vpn_button.clicked.connect(open_vpn)

vpn_button.setStyleSheet('''
    QPushButton {
        background-color: #4CAF50;
        color: white;
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 5px;
    }
    
    QPushButton:hover {
        background-color: #45a049;
    }
    
    QPushButton:pressed {
        background-color: #3c8031;
    }
''')

open_jira_button = QPushButton("Open Jira")
open_jira_button.clicked.connect(open_jira)

open_jira_button.setStyleSheet('''
    QPushButton {
        background-color: #FF5252;  /* Red */
        color: white;
        border: 2px solid #FF5252;  /* Red */
        border-radius: 5px;
        padding: 5px;
    }
    
    QPushButton:hover {
        background-color: #FF1744;  /* Darker Red */
    }
    
    QPushButton:pressed {
        background-color: #D50000;  /* Darkest Red */
    }
''')

layout = QGridLayout()
layout.addWidget(vpn_button, 0, 0)
layout.addWidget(open_jira_button, 0, 1)

window.setLayout(layout)
window.show()
sys.exit(app.exec())