from import_file import *
from plan import *
from gui import *


class APP():
    def __init__(self):
        self.plan = Plan()
        self.wordlist = WordlistWithPosition(self.plan.oldwords, self.plan.newwords)
        self.gui = Ui_MainWindow(self.wordlist)
        self.run()

    def run(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow(self.wordlist)
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


def import_wordlist(path):
    w = Wordlist()
    w.create_wordlist(path + '.txt')
    w.save(path + '.json')


if __name__ == "__main__":
    # with open('settings.txt', 'r', encoding='UTF-8') as f:
    #   settings = f.readlines()
    # import_wordlist('./words/CET6')
    # print(settings)
    app = APP()

'''
TODO:
1.delete old files
2.import setting from a txt file
3.GUI: import file, settings
'''
