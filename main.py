import sys
from PySide6.QtWidgets import QApplication
from ui import FilterApp

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    dark_stylesheet = """
    QMainWindow {
        background-color: #1e1e1e;
    }
    QWidget {
        background-color: #1e1e1e;
        color: #f0f0f0;
        font-family: 'Segoe UI', 'Roboto', sans-serif;
        font-size: 14px;
    }
    QGroupBox {
        border: 2px solid #3e3e42;
        border-radius: 6px;
        margin-top: 24px;
        font-weight: bold;
        color: #cccccc;
        font-size: 15px;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 5px;
    }
    QPushButton {
        background-color: #3e3e42;
        border: 1px solid #555;
        color: white;
        padding: 8px 16px;
        border-radius: 4px;
        font-weight: 600;
    }
    QPushButton:hover {
        background-color: #505050;
        border-color: #007acc;
    }
    QPushButton:pressed {
        background-color: #252526;
    }
    /* Specific Button Colors */
    QPushButton#btn_save {
        background-color: #2da44e; /* Green */
        border: 1px solid #2da44e;
    }
    QPushButton#btn_save:hover {
        background-color: #2c974b;
    }
    QPushButton#btn_retry {
        background-color: #cf6679; /* Reddish */
        border: 1px solid #cf6679;
        color: black;
    }
    QPushButton#btn_retry:hover {
        background-color: #b00020;
        color: white;
    }
    
    QListWidget {
        background-color: #252526;
        border: 1px solid #3e3e42;
        border-radius: 6px;
        outline: none;
        padding: 5px;
    }
    QListWidget::item {
        padding: 10px;
        color: #d4d4d4;
        border-bottom: 1px solid #2d2d30;
    }
    QListWidget::item:selected {
        background-color: #37373d;
        color: #ffffff;
        border-left: 3px solid #007acc;
    }
    QListWidget::item:hover {
        background-color: #2a2d2e;
    }
    
    QLabel {
        color: #e0e0e0;
    }
    QSplitter::handle {
        background-color: #2d2d30;
        width: 2px;
    }
    QScrollBar:vertical {
        border: none;
        background: #1e1e1e;
        width: 10px;
        margin: 0px;
    }
    QScrollBar::handle:vertical {
        background: #424242;
        min-height: 20px;
        border-radius: 5px;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        height: 0px;
    }
    """
    app.setStyleSheet(dark_stylesheet)
    
    window = FilterApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
