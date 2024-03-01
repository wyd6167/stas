StyleSheet = """
QToolTip { color: #ffffff; background-color: #1890ff; border: 0px; }
QDateEdit{
    border:1px solid #6d6d6d;
}
QDateEdit:focus{
    border:1px solid #fff;
}
QMenu{
    border-radius: 10px;
}
QComboBox{
    border:1px solid #6d6d6d;
    background:#23232d;
    border-radius: 10px;
    font: bold 14px;
    min-width: 10em;
    padding: 6px;
}
QComboBox::drop-down {
    border-top-right-radius: 10px;/*same radius as the QComboBox */
    border-bottom-right-radius:10px;
}
QRadioButton{
     border-top-right-radius: 10px;/*same radius as the QComboBox */
    border-bottom-right-radius:10px;
    border: 1px solid red;
}
QPushButton{
    border: 1px solid transparent;
     border-top-right-radius: 10px;/*same radius as the QComboBox */
    border-bottom-right-radius:10px;
}

QPlainTextEdit,QLineEdit {
    border:1px solid #6d6d6d;
    border-radius: 10px;
    font: 14px;
    min-width: 5em;
    padding: 5px;
    background:#23232d;
}
QPlainTextEdit:focus, QLineEdit:focus{
    border: 1px solid #fff;
}


QLabel{
    background: transparent;
    # border: 1px solid #fff;
}
"""
