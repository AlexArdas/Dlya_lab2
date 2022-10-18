from PyQt5 import QtWidgets
import sys
import gamma

Result = "Result.txt"
Sourse = "Sourse.txt"
NewResult = "NewResult.txt"


class MainApp(QtWidgets.QMainWindow, gamma.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Bott_shifr.clicked.connect(self.Crypt)
        self.Bott_deshifr.clicked.connect(self.DeCrypt)

    def Crypt(self):
        A = 5
        B = 1
        M = 16
        Y0 = 7
        gamma_list = []
        for i in range(8):
            y = (A * Y0 + B) % M
            gamma_list.append(y)
        gamma = gamma_list
        line = self.For_txt.text()
        with open("Sourse.txt", "w") as file:
            file.write(line)

        res = open("Result.txt", "w", encoding="utf-8")
        with open('Sourse.txt', 'r', encoding="utf-8") as f:
            r_int = ""
            r = ""
            while True:
                temp = f.read(8)
                if temp:
                    for i, item in enumerate(temp):
                        r_int = r_int + " " + str(ord(item) ^ gamma[i])
                        r = r + chr(ord(item) ^ gamma[i])
                        res.write(chr(ord(item) ^ gamma[i]))
                else:
                    break


        self.For_deshifr.setText(r)

    def DeCrypt(self):
        A = 5
        B = 1
        M = 16
        Y0 = 7
        gamma_list = []
        for i in range(8):
            y = (A * Y0 + B) % M
            gamma_list.append(y)

        gamma = gamma_list
        line = self.For_deshifr.text()
        with open("Result.txt", "w") as file:
            file.write(line)

        res = open("NewResult.txt", "w", encoding="utf-8")
        with open('Result.txt', 'r', encoding="utf-8") as f:
            r_int = ""
            r = ""
            while True:
                temp = f.read(8)
                if temp:
                    for i, item in enumerate(temp):
                        r_int = r_int + " " + str(ord(item) ^ gamma[i])
                        r = r + chr(ord(item) ^ gamma[i])
                        res.write(chr(ord(item) ^ gamma[i]))
                else:
                    break
        self.Obsh.setText(r)



        with open(NewResult, "r") as f:
            for res in f:
                print(res)


if __name__ == "__main__":
    def main():
        app = QtWidgets.QApplication(sys.argv)
        window = MainApp()
        window.show()
        app.exec_()


    if __name__ == '__main__':
        main()
