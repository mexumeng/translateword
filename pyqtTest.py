import sys
import requests
import re
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QLabel


class App(QWidget):
    trans_pattern = r'base-list([\w\W]*?)</ul>'
    word_pattern = r'<span>([\w\W]*?)</span>'
    words_pattern = r'in-base-top([\w\W]*?)</div>'

    def trans_word(self,wd):
        url = 'http://www.iciba.com/' + wd
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                                     '(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
        html = str(r.content, encoding='utf-8')
        result = re.findall(self.trans_pattern, html)
        if result:
            result = result[0]
            result = re.findall(self.word_pattern, result)
            trans_result = wd + '\n'
            for r in result:
                trans_result += r + '\n'
        else:
            result = re.findall(self.words_pattern, html)
            if result:
                result = result[0]
                result = re.findall(r'<div[\w\W]*?>([\w\W]*)', result)[0]
                trans_result = result
            else:
                trans_result = '翻译不了'
        return trans_result

    def main(self, wd):
        res = self.trans_word(wd)
        return res

    def __init__(self):
        super().__init__()
        self.title = '翻译为'
        self.left = 500
        self.top = 500
        self.width = 500
        self.height = 500
        self.label = QLabel(self)
        self.label.layout()
        self.input = QInputDialog(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        wd = self.getText()
        res = self.main(wd)
        self.label.update()
        self.label.setText(res)
        self.show()

    def getText(self):
        text, okPressed = self.input.getText(self, "翻译吧！", "输入您想翻译的内容:")
        if okPressed and text != '':
            return text
        else:
            exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
