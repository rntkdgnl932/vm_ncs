# * QTabWidget 탭에 다양한 위젯 추가
import numpy as np
from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QIcon, QFont       #아이콘
from PyQt5.QtCore import Qt, QThread

import sys

sys.path.append('C:/my_games/nightcrows/data_nc/mymodule')
import os
import time
from datetime import datetime
import random
import os.path
from datetime import date, timedelta
import re
import git

import cv2
# print(cv2.__version__)
# import matplotlib.pyplot as plt
from PIL import Image

import numpy
# 패키지 다운 필요
import pytesseract
# from pytesseract import image_to_string #
import pyautogui
import clipboard
# import keyboard
# 패키지 다운 불필요
import tkinter
import webbrowser
import colorthief

# 나의 모듈
# from function import imgs_set, imgs_set_, click_pos_2, random_int, text_check_get_3, int_put_, text_check_get, \
#     click_with_image, drag_pos, image_processing, get_region, click_pos_reg
from function import imgs_set, imgs_set_, click_pos_2, random_int, text_check_get_3, int_put_, text_check_get, click_with_image, drag_pos, image_processing, get_region, click_pos_reg


from massenger import line_monitor
from schedule import myQuest_play_check, myQuest_play_add
from test_ import go_test
from grow_1 import tuto_grow
from grow_2 import main_quest_grow
from grow_3 import sub_quest_grow
from grow_4 import select_daily_quest_grow
from dungeon import dungeon_play
from jadong_crow import jadong_play
from gyucjunji import gyucjunji_play
from get_item import get_items, get_item_checking, guild_jilyung
from potion import maul_potion
from action import maul_check, bag_open, quest_look, character_change, my_gold_check, bag_full_check

from one_event import daily_one

import variable as v_

sys.setrecursionlimit(10 ** 7)
# pyqt5 관련###################################################
rowcount = 0
colcount = 0
thisRow = 0
thisCol = 0
table_datas = ""
#  onCollection= False
onCharacter = 0
onRefresh_time = 0
onDunjeon = "none"
onDunjeon_level = 0
onHunt = "none"
onHunt2 = "none"
onHunt3 = "none"
onMaul = "none"

isgloballoop = False

version = v_.version_

# 기존 오토모드 관련##############################################


pyautogui.FAILSAFE = False
####################################################################################################################
# pytesseract.pytesseract.tesseract_cmd = R'E:\workspace\pythonProject\Tesseract-OCR\tesseract'
pytesseract.pytesseract.tesseract_cmd = R'C:\Program Files\Tesseract-OCR\tesseract'


####################################################################################################################
####################################################################################################################
####################################################################################################################
#######pyqt5 관련####################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################


class MyApp(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)

        self.initUI()

    def initUI(self):
        tabs = QTabWidget()
        tabs.addTab(FirstTab(), '스케쥴')
        tabs.addTab(SecondTab(), '내 정보')
        tabs.addTab(ThirdTab(), '모니터링')

        # buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # buttonbox.accepted.connect(self.accept)
        # buttonbox.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        # vbox.addWidget(buttonbox)

        self.setLayout(vbox)


        self.my_title()

        # 풀버젼
        # pyinstaller --hidden-import PyQt5 --hidden-import requests --hidden-import chardet --add-data="C:\\my_games\\nightcrows\\data_nc;./data_nc" -i="nightcrows.ico" --add-data="nightcrows.ico;./" --icon="nightcrows.ico" --paths "C:\Users\1_S_3\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2" main.py
        # 업데이트버젼
        # pyinstaller --hidden-import PyQt5 --hidden-import requests --hidden-import chardet -i="nightcrow.ico" --add-data="nightcrow.ico;./" --icon="nightcrow.ico" --paths "C:\Users\1_S_3\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2" main.py

        self.setGeometry(1000, 300, 900, 600)
        self.show()
    def my_title(self):
        self.setWindowTitle("나이트크로우(ver " + version + ")")

class ThirdTab(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        # self.set_rand_int()

    def initUI(self):

        dir_path = "C:\\my_games"
        file_path = dir_path + "\\line\\line.txt"

        if os.path.isdir(dir_path) == False:
            os.makedirs(dir_path)
        isFile = False
        while isFile is False:
            if os.path.isfile(file_path) == True:
                isFile = True
                # 파일 읽기
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    line = file.read()
                    line_ = line.split(":")
                    print('line', line)
            else:
                print('line 파일 없당')
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write("ccocco:메롱")

        self.monitor = QGroupBox('My Cla Monitor')

        self.own = QLabel("       현재 소유자 : " + line_[0] + "\n\n")
        self.computer = QLabel("       현재 컴퓨터 : " + line_[1] + " 컴퓨터\n\n")

        self.own_in = QLineEdit(self)
        self.own_in.setText(line_[0])
        self.computer_in = QLineEdit(self)
        self.computer_in.setText(line_[1])
        self.line_save = QPushButton("저장하기")
        self.line_save.clicked.connect(self.button_line_save)

        self.monitoring_1 = QPushButton("one 모니터링")
        self.monitoring_1.clicked.connect(self.button_monitoring_one)
        self.monitoring_2 = QPushButton("two 모니터링")
        self.monitoring_2.clicked.connect(self.button_monitoring_two)

        mo1_1 = QHBoxLayout()
        mo1_1.addWidget(self.own)

        mo1_2 = QHBoxLayout()
        mo1_2.addWidget(self.computer)

        mo1_3 = QHBoxLayout()
        mo1_3.addStretch(1)
        mo1_3.addWidget(self.own_in)
        mo1_3.addWidget(self.computer_in)
        mo1_3.addStretch(1)
        mo1_3.addWidget(self.line_save)
        mo1_3.addStretch(18)

        mo1_4 = QHBoxLayout()
        mo1_4.addWidget(self.monitoring_1)
        mo1_4.addWidget(self.monitoring_2)

        Mobox1 = QVBoxLayout()
        Mobox1.addStretch(1)
        Mobox1.addLayout(mo1_1)
        Mobox1.addLayout(mo1_2)
        Mobox1.addLayout(mo1_3)
        Mobox1.addStretch(3)
        Mobox1.addLayout(mo1_4)
        Mobox1.addStretch(3)

        self.monitor.setLayout(Mobox1)

        hbox_ = QHBoxLayout()
        hbox_.addWidget(self.monitor)

        Vbox_ = QVBoxLayout()
        Vbox_.addLayout(hbox_)

        self.setLayout(Vbox_)

        # hbox__ = QHBoxLayout()
        # hbox__.addWidget(self.monitor)
        #
        # ###
        # vbox = QVBoxLayout()
        # vbox.addLayout(hbox__)

    def button_line_save(self):
        own_ = self.own_in.text()  # line_edit text 값 가져오기
        computer_ = self.computer_in.text()
        print(own_)
        print(computer_)

        self.own.setText("       현재 소유자 : " + own_ + "\n\n")
        self.computer.setText("       현재 컴퓨터 : " + computer_ + " 컴퓨터\n\n")
        write_ = own_ + ":" + computer_
        dir_path = "C:\\my_games"
        file_path = dir_path + "\\line\\line.txt"

        with open(file_path, "w", encoding='utf-8-sig') as file:
            file.write(write_)

    def button_monitoring_one(self):
        m_ = Monitoring_one(self)
        m_.start()

    def button_monitoring_two(self):
        m_ = Monitoring_two(self)
        m_.start()


class SecondTab(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        # self.set_rand_int()

    def initUI(self):

        dir_path = "C:\\my_games\\nightcrows"
        file_path_one = dir_path + "\\mysettings\\idpw\\onecla.txt"
        file_path_two = dir_path + "\\mysettings\\idpw\\twocla.txt"
        if os.path.isfile(file_path_one) == True:
            # 파일 읽기
            with open(file_path_one, "r", encoding='utf-8-sig') as file:
                lines_one = file.read().splitlines()
                print('lines_one', lines_one)
                thismyid_one = lines_one[0]
                thismypw_one = lines_one[1]
                thismyps_one = lines_one[2]
        else:
            print('one 파일 없당')
            thismyid_one = 'none'
            thismyps_one = 'none'

        if os.path.isfile(file_path_two) == True:
            # 파일 읽기
            with open(file_path_two, "r", encoding='utf-8-sig') as file:
                lines_two = file.read().splitlines()
                print('lines_two', lines_two)
                thismyid_two = lines_two[0]
                thismypw_two = lines_two[1]
                thismyps_two = lines_two[2]
        else:
            print('two 파일 없당')
            thismyid_two = 'none'
            thismyps_two = 'none'

        # 111

        self.com_group1 = QGroupBox('One Cla')
        self.one_cla_id = QLabel("       ID          ")
        self.one_cla_pw = QLabel("       PW        ")
        self.one_cla_ps = QLabel("       참고사항 ")

        self.one_cla_id_now = QLabel("       현재 내 아이디 : " + thismyid_one + "\n\n")
        self.one_cla_ps_now = QLabel("       무슨 참고 사항을 적었나요? " + thismyps_one)

        self.pushButton_login1 = QPushButton("로그인하기")
        self.pushButton_login1.clicked.connect(self.let_is_login_1)

        self.pushButton_left = QPushButton("좌로 정렬")
        self.pushButton_left.clicked.connect(self.win_left)

        # self.one_cla_id_in = QLineEdit()
        self.one_cla_id_in = QLineEdit(self)
        self.one_cla_id_in.setText(thismyid_one)
        self.one_cla_pw_in = QLineEdit(self)
        self.one_cla_pw_in.setText(thismypw_one)
        self.one_cla_ps_in = QLineEdit(self)
        self.one_cla_ps_in.setText(thismyps_one)
        self.pushButton_one = QPushButton("저장하기")
        self.pushButton_one.clicked.connect(self.button_event1)

        vbox1_1 = QHBoxLayout()
        vbox1_1.addWidget(self.one_cla_id_now)

        vbox1_2 = QHBoxLayout()
        vbox1_2.addWidget(self.one_cla_ps_now)

        vbox1_log = QHBoxLayout()
        vbox1_log.addStretch(5)
        vbox1_log.addWidget(self.pushButton_login1)
        vbox1_log.addStretch(5)

        vbox1_left = QHBoxLayout()
        vbox1_left.addStretch(15)
        vbox1_left.addWidget(self.pushButton_left)
        vbox1_left.addStretch(1)

        vbox1_3 = QHBoxLayout()
        vbox1_3.addWidget(self.one_cla_id)
        vbox1_3.addWidget(self.one_cla_id_in)

        vbox1_4 = QHBoxLayout()
        vbox1_4.addWidget(self.one_cla_pw)
        vbox1_4.addWidget(self.one_cla_pw_in)

        vbox1_5 = QHBoxLayout()
        vbox1_5.addWidget(self.one_cla_ps)
        vbox1_5.addWidget(self.one_cla_ps_in)

        vbox1_6 = QHBoxLayout()
        vbox1_6.addStretch(5)
        vbox1_6.addWidget(self.pushButton_one)

        Vbox1 = QVBoxLayout()
        Vbox1.addStretch(1)
        Vbox1.addLayout(vbox1_1)
        Vbox1.addLayout(vbox1_2)
        Vbox1.addStretch(1)
        Vbox1.addLayout(vbox1_log)
        Vbox1.addStretch(5)
        Vbox1.addLayout(vbox1_left)
        Vbox1.addStretch(3)
        Vbox1.addLayout(vbox1_3)
        Vbox1.addLayout(vbox1_4)
        Vbox1.addLayout(vbox1_5)
        Vbox1.addLayout(vbox1_6)
        Vbox1.addStretch(2)
        # maul_add = QPushButton('마을 의뢰 추가')
        # maul_add.clicked.connect(self.onActivated_maul_add)
        # vbox6.addWidget(maul_add)
        self.com_group1.setLayout(Vbox1)

        # 222
        self.com_group2 = QGroupBox('Two Cla')
        self.two_cla_id = QLabel("       ID          ")
        self.two_cla_pw = QLabel("       PW        ")
        self.two_cla_ps = QLabel("       참고사항 ")

        self.two_cla_id_now = QLabel("       현재 내 아이디 : " + thismyid_two + "\n\n")
        self.two_cla_ps_now = QLabel("       무슨 참고 사항을 적었나요? " + thismyps_two)

        self.pushButton_login2 = QPushButton("로그인하기")
        self.pushButton_login2.clicked.connect(self.let_is_login_2)

        self.pushButton_right = QPushButton("우로 정렬")
        self.pushButton_right.clicked.connect(self.win_right)

        self.two_cla_id_in = QLineEdit(self)
        self.two_cla_id_in.setText(thismyid_two)
        self.two_cla_pw_in = QLineEdit(self)
        self.two_cla_pw_in.setText(thismypw_two)
        self.two_cla_ps_in = QLineEdit(self)
        self.two_cla_ps_in.setText(thismyps_two)
        self.pushButton_two = QPushButton("저장하기")
        self.pushButton_two.clicked.connect(self.button_event2)

        vbox2_1 = QHBoxLayout()
        vbox2_1.addWidget(self.two_cla_id_now)

        vbox2_2 = QHBoxLayout()
        vbox2_2.addWidget(self.two_cla_ps_now)

        vbox2_log = QHBoxLayout()
        vbox2_log.addStretch(5)
        vbox2_log.addWidget(self.pushButton_login2)
        vbox2_log.addStretch(5)

        vbox2_right = QHBoxLayout()
        vbox2_right.addStretch(1)
        vbox2_right.addWidget(self.pushButton_right)
        vbox2_right.addStretch(15)

        vbox2_3 = QHBoxLayout()
        vbox2_3.addWidget(self.two_cla_id)
        vbox2_3.addWidget(self.two_cla_id_in)

        vbox2_4 = QHBoxLayout()
        vbox2_4.addWidget(self.two_cla_pw)
        vbox2_4.addWidget(self.two_cla_pw_in)

        vbox2_5 = QHBoxLayout()
        vbox2_5.addWidget(self.two_cla_ps)
        vbox2_5.addWidget(self.two_cla_ps_in)

        vbox2_6 = QHBoxLayout()
        vbox2_6.addStretch(5)
        vbox2_6.addWidget(self.pushButton_two)

        Vbox2 = QVBoxLayout()
        Vbox2.addStretch(1)
        Vbox2.addLayout(vbox2_1)
        Vbox2.addLayout(vbox2_2)
        Vbox2.addStretch(1)
        Vbox2.addLayout(vbox2_log)
        Vbox2.addStretch(5)
        Vbox2.addLayout(vbox2_right)
        Vbox2.addStretch(3)
        Vbox2.addLayout(vbox2_3)
        Vbox2.addLayout(vbox2_4)
        Vbox2.addLayout(vbox2_5)
        Vbox2.addLayout(vbox2_6)
        Vbox2.addStretch(2)
        # maul_add = QPushButton('마을 의뢰 추가')
        # maul_add.clicked.connect(self.onActivated_maul_add)
        # vbox6.addWidget(maul_add)
        self.com_group2.setLayout(Vbox2)

        ###
        hbox_ = QHBoxLayout()
        hbox_.addWidget(self.com_group2)

        Vbox_ = QVBoxLayout()
        Vbox_.addLayout(hbox_)

        ###
        hbox__ = QHBoxLayout()
        hbox__.addWidget(self.com_group1)
        hbox__.addLayout(Vbox_)

        ###
        vbox = QVBoxLayout()
        vbox.addLayout(hbox__)
        self.setLayout(vbox)

    def win_left(self):
        print("왼쪽으로 정렬 합니다.")
        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\nightcrows_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1080, "one", img, 0.8)
        # imgs_ = pyautogui.locateCenterOnScreen(img, confidence=0.7)
        time.sleep(1)
        if imgs_ is not None and imgs_ != False:
            print("왼쪽 nightcrows 보여", imgs_)

            click_pos_reg(imgs_.x + 100, imgs_.y, "one")
            pyautogui.keyDown('win')
            pyautogui.press('left')
            pyautogui.keyUp('win')
            time.sleep(0.3)
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\nightcrows_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1080, "one", img, 0.8)
            time.sleep(0.3)
            if imgs_ is not None:
                click_pos_reg(imgs_.x + 100, imgs_.y, "one")

    def win_right(self):
        print("오른쪽으로 정렬 합니다.")
        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\nightcrows_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(960, 0, 1920, 1080, "one", img, 0.8)
        time.sleep(0.3)
        if imgs_ is not None and imgs_ != False:
            print("오른쪽 nightcrows 보여", imgs_)

            click_pos_reg(imgs_.x + 100, imgs_.y, "one")
            pyautogui.keyDown('win')
            pyautogui.press('right')
            pyautogui.keyUp('win')
            time.sleep(0.3)
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\nightcrows_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(960, 0, 1920, 1080, "one", img, 0.8)
            if imgs_ is not None:
                click_pos_reg(imgs_.x + 100, imgs_.y, "one")

    def let_is_login_1(self):
        print("로그인1 버튼 입니다.")

    def let_is_login_2(self):
        print("로그인2 버튼 입니다.")

    def button_event1(self):
        one_cla_id_ = self.one_cla_id_in.text()  # line_edit text 값 가져오기
        one_cla_pw_ = self.one_cla_pw_in.text()
        one_cla_ps_ = self.one_cla_ps_in.text()
        print(one_cla_id_)
        print(one_cla_pw_)

        one_cla_id_result = "       현재 내 아이디 : " + one_cla_id_ + "\n\n"
        one_cla_ps_result = "       무슨 참고 사항을 적었나요? " + one_cla_ps_
        self.one_cla_id_now.setText(one_cla_id_result)
        self.one_cla_ps_now.setText(one_cla_ps_result)
        shcedule = one_cla_id_ + "\n" + one_cla_pw_ + "\n" + one_cla_ps_
        dir_path = "C:\\my_games\\nightcrows"
        file_path_one = dir_path + "\\mysettings\\idpw\\onecla.txt"
        file_path_two = dir_path + "\\mysettings\\idpw\\twocla.txt"
        with open(file_path_one, "w", encoding='utf-8-sig') as file:
            file.write(shcedule)

    def button_event2(self):
        two_cla_id_ = self.two_cla_id_in.text()  # line_edit text 값 가져오기
        two_cla_pw_ = self.two_cla_pw_in.text()
        two_cla_ps_ = self.two_cla_ps_in.text()
        print(two_cla_id_)
        print(two_cla_pw_)

        two_cla_id_result = "       현재 내 아이디 : " + two_cla_id_ + "\n\n"
        two_cla_ps_result = "       무슨 참고 사항을 적었나요? " + two_cla_ps_
        self.two_cla_id_now.setText(two_cla_id_result)
        self.two_cla_ps_now.setText(two_cla_ps_result)
        shcedule = two_cla_id_ + "\n" + two_cla_pw_ + "\n" + two_cla_ps_
        dir_path = "C:\\my_games\\nightcrows"
        file_path_one = dir_path + "\\mysettings\\idpw\\onecla.txt"
        file_path_two = dir_path + "\\mysettings\\idpw\\twocla.txt"
        with open(file_path_two, "w", encoding='utf-8-sig') as file:
            file.write(shcedule)


class FirstTab(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_rand_int()

        # self.BackGroundPotion_ = BackGroundPotion(self)
        # self.BackGroundPotion_.start()

        # self.BackGroundOdin = BackGroundOdin_()
        # self.BackGroundOdin.start()

        # self.BackGroundOdin_ = BackGroundOdin()
        # self.BackGroundOdin_.start()

        # self.game = game_Playing(self)
        # self.game.start()

    def initUI(self):
        global rowcount, colcount, onCharacter, onDunjeon, onDunjeon_level, onMaul, onHunt, isgloballoop

        dir_path = "C:\\my_games\\nightcrows"
        file_path = dir_path + "\\mysettings\\myschedule\\schedule.txt"
        file_path3 = dir_path + "\\mysettings\\myschedule\\schedule2.txt"
        file_path5 = dir_path + "\\data_nc\\jadong\\jadong_force_list.txt"

        if os.path.isfile(file_path) == True:
            # 파일 읽기
            with open(file_path, "r", encoding='utf-8-sig') as file:
                lines = file.read().splitlines()
        else:
            print('파일 없당')
            if os.path.isdir(dir_path) == True:
                print('디렉토리 존재함')
                with open(file_path3, "r", encoding='utf-8-sig') as file:
                    shcedule = file.read().splitlines()
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(str(shcedule))
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            lines = file.read().splitlines()
            else:
                print('디렉토리 존재하지 않음')
                os.makedirs(dir_path)
                with open(file_path3, "r", encoding='utf-8-sig') as file:
                    shcedule = file.read().splitlines()
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(str(shcedule))
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            lines = file.read().splitlines()
        if os.path.isfile(file_path5) == True:
            # 파일 읽기
            with open(file_path5, "r", encoding='utf-8-sig') as file:
                jadong_list = file.read().splitlines()
                jadong_list_ = ["사냥터"]
                for i in range(len(jadong_list)):
                    result = jadong_list[i].split("/")
                    jadong_list_.append(result[0])
            # print(".......................................", jadong_list_)
        else:
            jadong_list = ["자동리스트 없당"]

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(lines))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)  # 행번호 안나오게 하는 코드
        self.tableWidget.setHorizontalHeaderLabels(["클라", "ID", "던전", "현재상태", "클라", "ID", "던전", "현재상태"])

        self.label = QLabel('')

        # 스케쥴 한칸 위로
        sche_up_modify = QPushButton('up')
        sche_up_modify.clicked.connect(self.sche_up_modify)
        # 스케쥴 한칸 아래로
        sche_down_modify = QPushButton('down')
        sche_down_modify.clicked.connect(self.sche_down_modify)
        # 스케쥴 변경 확인
        self.sche_add1 = QPushButton('one 대기중', self)
        self.sche_add1.clicked.connect(self.mySchedule_start1)
        self.sche_add2 = QPushButton('two 대기중', self)
        self.sche_add2.clicked.connect(self.mySchedule_start2)

        # 테스트 버튼
        self.mytestin = QPushButton('테스뚜')
        self.mytestin.clicked.connect(self.mytestin_)
        self.temporary_pause = QPushButton('일시정지')
        self.temporary_pause.clicked.connect(self.temporary_all_pause_game)
        self.again_restart = QPushButton('업데이트')
        self.again_restart.clicked.connect(self.again_restart_game)

        # 스케쥴 선택 삭제
        self.del_ = QPushButton('삭제')
        self.del_.clicked.connect(self.mySchedule_del)
        # 스케쥴 초기화
        self.clear = QPushButton('초기화')
        self.clear.clicked.connect(self.mySchedule_refresh)
        # 스케쥴 완전 초기화
        self.all_clear = QPushButton('완전 초기화')
        self.all_clear.clicked.connect(self.mySchedule_refresh_all)

        # self.setItems = QPushButton('Set Items')
        # self.setItems.clicked.connect(self.set_rand_int)

        # 강제 노역(서브퀘스트 강제수행)
        self.onActivated_slelect_gold_read()
        self.onActivated_slelect_spot_read()
        self.force_sub = QGroupBox('강제 서브퀘스트')

        self.my_limit_gold = QLabel("골드 : " + str(v_.onForceGold) + " 이하 강제노역 ㄱㄱ")
        self.my_limit_gold_spot = QLabel("사냥터 : " + str(v_.onForceGoldSpot))

        sub_q = QComboBox()
        limit_gold = ['얼마이하', '1만', '10만', '50만', '100만', '200만']
        sub_q.addItems(limit_gold)

        sub_h = QComboBox()
        gold_spot = jadong_list_
        sub_h.addItems(gold_spot)

        gold33 = QHBoxLayout()
        gold33.addWidget(self.my_limit_gold)

        sub_box = QVBoxLayout()
        sub_box.addLayout(gold33)
        sub_box.addWidget(self.my_limit_gold_spot)
        sub_box.addWidget(sub_q)
        sub_box.addWidget(sub_h)

        slelect_gold = QPushButton('골드 선택')
        slelect_gold.clicked.connect(self.onActivated_slelect_gold)
        slelect_spot = QPushButton('장소 선택')
        slelect_spot.clicked.connect(self.onActivated_slelect_spot)

        self.force_sub.setLayout(sub_box)

        # 콜렉션 온오프(수집 온오프)
        self.onActivated_slelect_collection_toggle_read()

        self.collection_on_off = QGroupBox('수집 On/Off')
        print("coleection", v_.onCollection)
        if v_.onCollection == True:
            tgl_now = "On"
        else:
            tgl_now = "Off"
        self.now_toggle = QLabel("수집 : "+ tgl_now + "\n")
        # 토글 버튼
        self.tgl = QCheckBox("On / Off")
        self.tgl.adjustSize()
        self.tgl.setChecked(v_.onCollection)
        self.tgl.toggled.connect(self.onActivated_slelect_collection_toggle)

        tgl33 = QHBoxLayout()
        tgl33.addWidget(self.now_toggle)

        collec_box = QVBoxLayout()
        collec_box.addLayout(tgl33)
        collec_box.addWidget(self.tgl)

        self.collection_on_off.setLayout(collec_box)






        # 캐릭터 아이디
        self.com_group3 = QGroupBox('캐릭터 선택')
        cb3 = QComboBox()
        list3 = ['캐릭터 선택', '1', '2', '3', '4', '5']
        cb3.addItems(list3)
        vbox3 = QVBoxLayout()
        vbox3.addWidget(cb3)
        character_ = QPushButton('캐릭터 선택')
        character_.clicked.connect(self.onActivated_character)
        self.com_group3.setLayout(vbox3)

        #self.one_cla_id_now = QLabel("       현재 내 아이디 : " + thismyid_one + "\n\n")

        # 일일퀘스트 요구 레벨(나의 레벨)
        read_level = '35'

        dir_path = "C:\\my_games\\nightcrows\\mysettings\\my_level"
        one_file_path = dir_path + "\\one_character.txt"
        two_file_path = dir_path + "\\two_character.txt"

        isreadlevel = False
        while isreadlevel is False:
            if os.path.isdir(dir_path) == True:
                print('디렉토리 존재함')
                isreadlevel = True
                one_re_ = False
                two_re_ = False
                while one_re_ is False:
                    if os.path.isfile(one_file_path) == True:
                        one_re_ = True
                        with open(one_file_path, "r", encoding='utf-8-sig') as file:
                            one_read_level = file.read()
                    else:
                        with open(one_file_path, "w", encoding='utf-8-sig') as file:
                            file.write(read_level)
                while two_re_ is False:
                    if os.path.isfile(two_file_path) == True:
                        two_re_ = True
                        with open(two_file_path, "r", encoding='utf-8-sig') as file:
                            two_read_level = file.read()
                    else:
                        with open(two_file_path, "w", encoding='utf-8-sig') as file:
                            file.write(read_level)

            else:
                print('디렉토리 존재하지 않음')
                os.makedirs(dir_path)
                with open(one_file_path, "w", encoding='utf-8-sig') as file:
                    file.write(read_level)
                with open(two_file_path, "w", encoding='utf-8-sig') as file:
                    file.write(read_level)




        self.com_group3_level = QGroupBox('일퀘요구레벨')
        self.one_require_level = QLabel("1배럭 요구레벨 : " + str(one_read_level))
        self.two_require_level = QLabel("2배럭 요구레벨 : " + str(two_read_level))
        self.require_level_in = QLineEdit(self)
        vbox_level = QVBoxLayout()
        vbox_level.addWidget(self.one_require_level)
        vbox_level.addWidget(self.two_require_level)
        vbox_level.addWidget(self.require_level_in)
        one_character_level = QPushButton('one_character_save')
        one_character_level.clicked.connect(self.onActivated_one_character_level)
        two_character_level = QPushButton('two_character_save')
        two_character_level.clicked.connect(self.onActivated_two_character_level)
        vbox_level.addWidget(one_character_level)
        vbox_level.addWidget(two_character_level)
        self.com_group3_level.setLayout(vbox_level)

        # 초기화 시간 수정
        self.com_group33 = QGroupBox('초기화 시간 수정')
        cb33 = QComboBox()
        list33 = ['시간 선택', '4', '5', '6', '7', '8', '9', '10', '11']
        cb33.addItems(list33)
        vbox33 = QVBoxLayout()
        vbox33.addWidget(cb33)
        refresh_time_ = QPushButton('시간 수정')
        refresh_time_.clicked.connect(self.onActivated_re_time)

        vbox33.addWidget(refresh_time_)
        self.com_group33.setLayout(vbox33)

        # 초기화 시간
        dir_path = "C:\\my_games\\nightcrows"
        file_path2 = dir_path + "\\mysettings\\refresh_time\\quest.txt"
        file_path13 = dir_path + "\\mysettings\\refresh_time\\refresh_time.txt"

        isRefresh = False
        while isRefresh is False:
            if os.path.isfile(file_path13) == True:
                with open(file_path13, "r", encoding='utf-8-sig') as file:
                    isRefresh = True
                    refresh_time = file.read()
                    print("refresh_time => ", refresh_time)
            else:
                with open(file_path13, "w", encoding='utf-8-sig') as file:
                    file.write(str(6))

        if os.path.isfile(file_path2) == True:
            # 파일 읽기
            with open(file_path2, "r", encoding='utf-8-sig') as file:
                lines2 = file.read().splitlines()
                day_ = lines2[0].split(":")
                re_time_ = str(day_[0]) + " => " + str(day_[1] + "시")
                print("최근 초기화 시간 : ", re_time_)
        else:
            re_time_ = "아직 모름..."

        self.com_group34 = QGroupBox('셋팅된 시간')
        # lbx = QBoxLayout(QBoxLayout.LeftToRight, parent=self)
        # self.com_group34.setLayout(lbx)
        self.my_refresh_time = QLabel("현재 초기화 시간 : " + str(refresh_time) + "\n\n" + "최근 초기화한 시간 : " + re_time_)
        # lbx.addWidget(self.my_refresh_time)

        self.pushButton_one = QPushButton("현재 내 상태 조회하기")
        self.pushButton_one.clicked.connect(self.mystatus_refresh)

        # vbox34 = QHBoxLayout()
        # vbox34.addWidget(self.my_refresh_time)
        #
        # Vbox3434 = QVBoxLayout()
        # Vbox3434.addLayout(vbox34)
        # Vbox3434.addWidget(self.pushButton_one)

        vbox34 = QHBoxLayout()
        vbox34.addWidget(self.my_refresh_time)

        Vbox3434 = QVBoxLayout()
        Vbox3434.addLayout(vbox34)
        Vbox3434.addWidget(self.pushButton_one)

        self.com_group34.setLayout(Vbox3434)

        # self.one_cla_id_now = QLabel("       현재 내 아이디 : " + thismyid_one + "\n\n")

        # 마을 의뢰
        self.com_group6 = QGroupBox('육성, 퀘스트, 각종템받기, 거래소등록하기')
        cb6 = QComboBox()
        list6 = ['스케쥴 선택', '캐릭터바꾸기', '튜토육성', '메인퀘스트', '서브퀘스트', '일일퀘스트_1', '일일퀘스트_2', '일일퀘스트_3', '각종템받기', '거래소등록', '격전지사냥']
        cb6.addItems(list6)
        vbox6 = QHBoxLayout()
        vbox6.addWidget(cb6)
        maul_add = QPushButton('육성 및 행동 추가')
        maul_add.clicked.connect(self.onActivated_maul_add)

        vbox6.addWidget(maul_add)
        self.com_group6.setLayout(vbox6)

        # 던전 종류
        self.com_group4 = QGroupBox('던전')
        cb4 = QComboBox()
        list4 = ['던전 선택', '던전_번영', '던전_수련', '던전_신전', '던전_유적', '던전_동굴']
        cb4.addItems(list4)
        cb44 = QComboBox()
        list44 = ['구역 및 전당', '1', '2', '3', '4', '5', '6']
        cb44.addItems(list44)

        vbox4 = QHBoxLayout()
        vbox4.addWidget(cb4)
        vbox4.addWidget(cb44)

        dunjeon = QPushButton('던전 추가')
        dunjeon.clicked.connect(self.onActivated_dunjeon_add)

        vbox4.addWidget(dunjeon)
        self.com_group4.setLayout(vbox4)

        # 사냥터
        dir_path = "C:\\my_games\\nightcrows\\data_nc"
        file_path1 = dir_path + "\\jadong\\abilius.txt"
        file_path2 = dir_path + "\\jadong\\bastium.txt"
        file_path3 = dir_path + "\\jadong\\chalano.txt"

        if os.path.isfile(file_path1) == True:
            with open(file_path1, "r", encoding='utf-8-sig') as file:
                read_1 = file.read()
                read_1 = read_1.split(":")
                read_1 = "< 아빌리우스 >/" + read_1[1]
                read_1 = read_1.split("/")
                list5 = []
                for i in range(len(read_1)):
                    list5.append(read_1[i])
            with open(file_path2, "r", encoding='utf-8-sig') as file:
                read_1 = file.read()
                read_1 = read_1.split(":")
                read_1 = "< 바스티움 >/" + read_1[1]
                read_1 = read_1.split("/")
                list55 = []
                for i in range(len(read_1)):
                    list55.append(read_1[i])
            with open(file_path3, "r", encoding='utf-8-sig') as file:
                read_1 = file.read()
                read_1 = read_1.split(":")
                read_1 = "< 첼라노 >/" + read_1[1]
                read_1 = read_1.split("/")
                list555 = []
                for i in range(len(read_1)):
                    list555.append(read_1[i])

        self.com_group5 = QGroupBox('자동사냥터')
        cb5 = QComboBox()
        #list5 = ['자동 사냥터 선택1', '사냥_콜리아 삼거리', '사냥_마른땅 벌목지', '사냥_실바인 진흙탕', '사냥_실바인 저수지']
        cb5.addItems(list5)
        jadong1 = QPushButton('아빌리우스 추가')
        jadong1.clicked.connect(self.onActivated_hunt_add)

        cb55 = QComboBox()
        #list55 = ['자동 사냥터 선택2', '사냥_콜리아 삼거리', '사냥_마른땅 벌목지', '사냥_실바인 진흙탕', '사냥_실바인 저수지']
        cb55.addItems(list55)
        jadong2 = QPushButton('바스티움 추가')
        jadong2.clicked.connect(self.onActivated_hunt_add_2)

        cb555 = QComboBox()
        #list555 = ['자동 사냥터 선택3', '사냥_콜리아 삼거리', '사냥_마른땅 벌목지', '사냥_실바인 진흙탕', '사냥_실바인 저수지']
        cb555.addItems(list555)
        jadong3 = QPushButton('첼라노 추가')
        jadong3.clicked.connect(self.onActivated_hunt_add_3)


        vbox5_1 = QHBoxLayout()
        vbox5_1.addWidget(cb5)
        vbox5_1.addWidget(jadong1)

        vbox5_2 = QHBoxLayout()
        vbox5_2.addWidget(cb55)
        vbox5_2.addWidget(jadong2)

        vbox5_3 = QHBoxLayout()
        vbox5_3.addWidget(cb555)
        vbox5_3.addWidget(jadong3)

        lastbox = QVBoxLayout()
        lastbox.addLayout(vbox5_1)
        lastbox.addLayout(vbox5_2)
        lastbox.addLayout(vbox5_3)


        self.com_group5.setLayout(lastbox)

        ###

        sub_h.activated[str].connect(self.onActivated_slelect_spot)  # 요건 함수
        sub_q.activated[str].connect(self.onActivated_slelect_gold)  # 요건 함수
        cb3.activated[str].connect(self.onActivated_character)  # 요건 함수
        cb33.activated[str].connect(self.onActivated_time)  # 요건 함수
        cb4.activated[str].connect(self.onActivated_dunjeon)  # 요건 함수
        cb44.activated[str].connect(self.onActivated_dunjeon_level)  # 요건 함수
        cb5.activated[str].connect(self.onActivated_hunt)  # 요건 함수
        cb55.activated[str].connect(self.onActivated_hunt2)  # 요건 함수
        cb555.activated[str].connect(self.onActivated_hunt3)  # 요건 함수
        cb6.activated[str].connect(self.onActivated_maul)  # 요건 함수

        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.cellClicked.connect(self.set_label)
        rowcount = self.tableWidget.rowCount()
        colcount = self.tableWidget.columnCount()

        # 레이아웃
        hbox1 = QHBoxLayout()
        # hbox1.addWidget(self.setItems)
        hbox1.addWidget(self.mytestin)
        hbox1.addWidget(self.temporary_pause)
        hbox1.addWidget(self.again_restart)
        hbox1.addWidget(self.del_)
        hbox1.addWidget(self.clear)
        hbox1.addWidget(self.all_clear)

        hbox7 = QHBoxLayout()
        hbox7.addWidget(sche_up_modify)
        hbox7.addWidget(sche_down_modify)
        hbox7.addStretch(4)
        hbox7.addWidget(self.sche_add1)
        hbox7.addWidget(self.sche_add2)
        hbox7.addStretch(8)
        hbox7.addLayout(hbox1)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.com_group4)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.com_group5)


        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.com_group6)

        hbox33 = QHBoxLayout()
        hbox33.addWidget(self.com_group33)

        first_box_1 = QHBoxLayout()
        first_box_1.addWidget(self.force_sub)

        first_box_2 = QHBoxLayout()
        first_box_2.addWidget(self.collection_on_off)

        first_vbox_1 = QVBoxLayout()
        first_vbox_1.addLayout(first_box_1)
        first_vbox_1.addLayout(first_box_2)

        Vbox33 = QVBoxLayout()
        Vbox33.addLayout(hbox33)
        Vbox33.addWidget(self.com_group34)


        CharacterAndLevel = QVBoxLayout()
        CharacterAndLevel.addWidget(self.com_group3)
        CharacterAndLevel.addWidget(self.com_group3_level)

        Vbox2 = QVBoxLayout()
        Vbox2.addLayout(hbox5)
        Vbox2.addLayout(hbox3)
        Vbox2.addLayout(hbox4)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(first_vbox_1)
        hbox2.addLayout(Vbox33)
        # hbox2.addWidget(self.com_group34)
        hbox2.addLayout(CharacterAndLevel)
        hbox2.addLayout(Vbox2)

        vbox = QVBoxLayout()

        # self.tableWidget.resizeColumnsToContents()
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(self.label)
        vbox.addLayout(hbox7)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)

    def temporary_all_pause_game(self):
        # change_ready_main = True
        # change_ready_step = True
        print("game_Playing(self): temporary_pause_game")
        # self.game.isCheck = False
        # self.game.quit()
        # self.game.wait(3000)
        # self.temporary_pause_background()

    def temporary_pause_background(self):

        print("game_Playing(self): temporary_pause_background")
        # self.BackGroundPotion_.potion_back_ = False
        # self.BackGroundPotion_.quit()
        # self.BackGroundPotion_.wait(3000)

    def temporary_pause_game(self):

        print("game_Playing(self): temporary_pause_game")
        # self.game.isCheck = False
        # self.game.quit()
        # self.game.wait(3000)
        time.sleep(5)

    def again_restart_game(self):
        # change_ready_main = False
        # change_ready_step = False

        print("업데이트 후 재시작")
        # git pull 실행 부분
        # git_dir = '{https://github.com/rntkdgnl932/ncs.git}'
        # g = git.cmd.Git(git_dir)
        # g.pull()
        # Repo('여기 비워진것은 현재 실행되는 창의 위치란 뜻...현재 실행되는 창의 위치 기준...상대경로임...')
        my_repo = git.Repo()
        my_repo.remotes.origin.pull()
        time.sleep(1)
        # 실행 후 재시작 부분
        os.execl(sys.executable, sys.executable, *sys.argv)

        # self.game.isCheck = True
        # self.game.start()
        # self.again_restart_background()

    def again_restart_background(self):

        print("game_Playing(self): again_restart_background")

        # self.BackGroundPotion_.potion_back_ = True
        # self.BackGroundPotion_.start()
        # time.sleep(1)
    def onActivated_slelect_spot_read(self):
        dir_path = "C:\\my_games\\nightcrows"
        dir_spot = "C:\\my_games\\nightcrows\\mysettings\\gold_force"
        file_path = dir_path + "\\mysettings\\gold_force\\limit_gold_spot.txt"

        islimitgold = False
        while islimitgold is False:
            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    v_.onForceGoldSpot = file.read()
                    islimitgold = True
            else:
                if os.path.isdir(dir_spot) == False:
                    print('강제노역 장소 디렉토리 존재하지 않음')
                    os.makedirs(dir_spot)
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write("콜리아삼거리")

        abilius = dir_path + "\\data_nc\\jadong\\abilius.txt"
        bastium = dir_path + "\\data_nc\\jadong\\bastium.txt"
        chalano = dir_path + "\\data_nc\\jadong\\chalano.txt"

        jadong_list = v_.onForceGoldSpot
        with open(abilius, "r", encoding='utf-8-sig') as file:
            abilius_list = file.read()
            abilius_list_ = abilius_list.split(":")
            abilius_list_result = abilius_list_[1].split("/")
            for i in range(len(abilius_list_result)):
                if jadong_list == abilius_list_result[i]:
                    spot_ = "사냥_아빌리우스_" + jadong_list
                    print("spot_1", spot_)
        with open(bastium, "r", encoding='utf-8-sig') as file:
            bastium_list = file.read()
            bastium_list_ = bastium_list.split(":")
            bastium_list_result = bastium_list_[1].split("/")
            for i in range(len(bastium_list_result)):
                if jadong_list == bastium_list_result[i]:
                    spot_ = "사냥_바스티움_" + jadong_list
                    print("spot_2", spot_)
        with open(chalano, "r", encoding='utf-8-sig') as file:
            chalano_list = file.read()
            chalano_list_ = chalano_list.split(":")
            chalano_list_result = chalano_list_[1].split("/")
            for i in range(len(chalano_list_result)):
                if jadong_list == chalano_list_result[i]:
                    spot_ = "사냥_첼라노_" + jadong_list
                    print("spot_3", spot_)


        v_.onForceGoldSpot_go = spot_

        return v_.onForceGoldSpot

    def onActivated_slelect_spot(self, e):
        if e != 0 and e != '사냥터':
            v_.onForceGoldSpot = e
            print('onForceGoldSpot : ', v_.onForceGoldSpot)
            dir_path = "C:\\my_games\\nightcrows"
            dir_spot = "C:\\my_games\\nightcrows\\mysettings\\gold_force"
            file_path = dir_path + "\\mysettings\\gold_force\\limit_gold_spot.txt"

            islimitgold = False
            while islimitgold is False:
                if os.path.isfile(file_path) == True:
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(e)
                        islimitgold = True
                else:
                    if os.path.isdir(dir_spot) == False:
                        print('강제노역 장소 디렉토리 존재하지 않음')
                        os.makedirs(dir_spot)
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(e)
        else:
            print("사냥터를 선택해 주세요.")
        self.my_limit_gold_spot.setText("사냥터 : " + str(v_.onForceGoldSpot))
        self.onActivated_slelect_spot_read()

    def onActivated_slelect_gold_read(self):
        dir_path = "C:\\my_games\\nightcrows"
        dir_gold = "C:\\my_games\\nightcrows\\mysettings\\gold_force"
        file_path = dir_path + "\\mysettings\\gold_force\\limit_gold.txt"

        islimitgold = False
        while islimitgold is False:
            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    v_.onForceGold = file.read()
                    islimitgold = True
            else:
                if os.path.isdir(dir_gold) == False:
                    print('강제노역 시작 골드 디렉토리 존재하지 않음')
                    os.makedirs(dir_gold)
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write("50만")

        return v_.onForceGold

    def onActivated_slelect_gold(self, e):
        if e != 0 and e != '얼마이하':
            v_.onForceGold = e
            print('onForceGold : ', v_.onForceGold)
            dir_path = "C:\\my_games\\nightcrows"
            dir_gold = "C:\\my_games\\nightcrows\\mysettings\\gold_force"
            file_path = dir_path + "\\mysettings\\gold_force\\limit_gold.txt"

            islimitgold = False
            while islimitgold is False:
                if os.path.isfile(file_path) == True:
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(e)
                        islimitgold = True
                else:
                    if os.path.isdir(dir_gold) == False:
                        print('강제노역 시작 골드 디렉토리 존재하지 않음')
                        os.makedirs(dir_gold)
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(e)
        else:
            print("금액을 선택해 주세요.")
        self.my_limit_gold.setText("골드 : " + str(e) + " 이하 강제노역 ㄱㄱ\n")
        self.onActivated_slelect_gold_read()

    def onActivated_slelect_collection_toggle_read(self):
        print('onCollection read', v_.onCollection)
        dir_path = "C:\\my_games\\nightcrows"
        dir_toggle = "C:\\my_games\\nightcrows\\mysettings\\collection"
        file_path = dir_path + "\\mysettings\\collection\\collection_toggle.txt"

        isToggle = False
        while isToggle is False:
            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='utf-8-sig') as file:

                    read_tgl = file.read()
                    if read_tgl == "on":
                        isToggle = True
                        v_.onCollection = True
                    else:
                        isToggle = True
                        v_.onCollection = False
            else:
                if os.path.isdir(dir_toggle) == False:
                    print('토글 디렉토리 존재하지 않음')
                    os.makedirs(dir_toggle)
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write("off")
        return v_.onCollection

    def onActivated_slelect_collection_toggle(self, e):
        # global onCollection
        v_.onCollection = e
        print('onCollection change', v_.onCollection)
        dir_path = "C:\\my_games\\nightcrows"
        dir_toggle = "C:\\my_games\\nightcrows\\mysettings\\collection"
        file_path = dir_path + "\\mysettings\\collection\\collection_toggle.txt"

        isToggle = False
        while isToggle is False:
            if os.path.isfile(file_path) == True:
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    isToggle = True
                    if e == True:
                        file.write("on")
                    else:
                        file.write("off")
            else:
                if os.path.isdir(dir_toggle) == False:
                    print('토글 디렉토리 존재하지 않음')
                    os.makedirs(dir_toggle)
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write("off")
        if v_.onCollection == True:
            tgl_now = "On"
        else:
            tgl_now = "Off"
        self.now_toggle.setText("수집 : " + str(tgl_now) + "\n")
        self.tgl.setChecked(v_.onCollection)
        #self.set_rand_int()

    def onActivated_character(self, text):
        global onCharacter
        if text != 0 and text != '캐릭터 선택':
            onCharacter = text
            print('onCharacter', onCharacter)
        else:
            onCharacter = 0
            print("캐릭터를 선택해 주세요.")

    def onActivated_one_character_level(self, text):
        character_level_ = self.require_level_in.text()  # line_edit text 값 가져오기
        print(character_level_)

        result_number_check = character_level_.isdigit()
        if result_number_check == True:
            character_level_result = "1배럭 요구레벨 : " + character_level_
            self.one_require_level.setText(character_level_result)
            dir_path = "C:\\my_games\\nightcrows"
            file_path = dir_path + "\\mysettings\\my_level\\one_character.txt"
            with open(file_path, "w", encoding='utf-8-sig') as file:
                file.write(character_level_)
        else:
            pyautogui.alert(button='넵', text='숫자만 입력해 주세요', title='일일퀘스트 요구 레벨')



    def onActivated_two_character_level(self, text):
        character_level_ = self.require_level_in.text()  # line_edit text 값 가져오기
        print(character_level_)

        result_number_check = character_level_.isdigit()
        if result_number_check == True:
            character_level_result = "2배럭 요구레벨 : " + character_level_
            self.two_require_level.setText(character_level_result)
            dir_path = "C:\\my_games\\nightcrows"
            file_path = dir_path + "\\mysettings\\my_level\\two_character.txt"
            with open(file_path, "w", encoding='utf-8-sig') as file:
                file.write(character_level_)
        else:
            pyautogui.alert(button='넵', text='숫자만 입력해 주세요', title='일일퀘스트 요구 레벨')


    def onActivated_time(self, text):
        global onRefresh_time
        if text != 0 and text != '시간 선택':
            onRefresh_time = text
            print('onRefresh_time : ', onRefresh_time)
        else:
            onRefresh_time = 6
            print("시간을 선택해 주세요.")

    def onActivated_dunjeon(self, text):
        global onDunjeon
        if text != 0 and text != '던전 선택':
            onDunjeon = text
            print('onDunjeon', onDunjeon)
        else:
            onDunjeon = 'none'
            print("던전을 선택해 주세요.")

    def onActivated_dunjeon_level(self, text):
        global onDunjeon_level
        if text != 0 and text != '층수 선택':
            onDunjeon_level = text
            print('onDunjeon_level', onDunjeon_level)
        else:
            onDunjeon_level = 'none'
            print("던전 층수를 선택해 주세요.")

    def onActivated_hunt(self, text):
        global onHunt
        if text != 0 and text != '< 아빌리우스 >':
            onHunt = text
            print('onHunt', onHunt)
        else:
            onHunt = 'none'
            pyautogui.alert(button='넵', text='사냥터를 선택해 주시지예', title='아빌리우스')
            print("자동 사냥터를 선택해 주세요.")
    def onActivated_hunt2(self, text):
        global onHunt2
        if text != 0 and text != '< 바스티움 >':
            onHunt2 = text
            print('onHunt2', onHunt2)
        else:
            onHunt2 = 'none'
            pyautogui.alert(button='넵', text='사냥터를 선택해 주시지예', title='바스티움')
            print("자동 사냥터를 선택해 주세요.")
    def onActivated_hunt3(self, text):
        global onHunt3
        if text != 0 and text != '< 첼라노 >':
            onHunt3 = text
            print('onHunt3', onHunt3)
        else:
            onHunt3 = 'none'
            pyautogui.alert(button='넵', text='사냥터를 선택해 주시지예', title='첼라노')
            print("자동 사냥터를 선택해 주세요.")

    def onActivated_maul(self, text):
        global onMaul
        if text != 0 and text != '마을 의뢰 장소 선택':
            onMaul = text
            print('onMaul', onMaul)
        else:
            onMaul = 'none'
            pyautogui.alert(button='넵', text='마을 의뢰 장소를 선택해 주시지예', title='뭐합니꺼')
            print("마을 의뢰 장소를 선택해 주세요.")

    def onActivated_re_time(self):
        global onRefresh_time
        if onRefresh_time == '시간 선택' or onRefresh_time == 'none':
            # pyautogui.alert(button='넵', text='던전을 선택해 주시지예', title='아 진짜 뭐합니꺼')
            reply = QMessageBox.question(self, '던전을 선택해 주시지예', '아 진짜 뭐합니꺼?',
                                         QMessageBox.Yes, QMessageBox.NoButton)


        else:
            print('onRefresh_time', onRefresh_time)
            dir_path = "C:\\my_games\\nightcrows"
            file_path13 = dir_path + "\\mysettings\\refresh_time\\refresh_time.txt"
            isRefresh = False
            while isRefresh is False:
                if os.path.isfile(file_path13) == True:
                    with open(file_path13, "w", encoding='utf-8-sig') as file:
                        file.write(onRefresh_time)
                    with open(file_path13, "r", encoding='utf-8-sig') as file:
                        isRefresh = True
                        refresh_time = file.read()
                        print("저장된 초기화 시간", onRefresh_time)
                else:
                    with open(file_path13, "w", encoding='utf-8-sig') as file:
                        file.write(onRefresh_time)

    def onActivated_dunjeon_add(self):
        global onCharacter, onDunjeon, onDunjeon_level
        char_ = onCharacter
        dun_ = str(onDunjeon) + "_" + str(onDunjeon_level)
        if onCharacter == 0:
            pyautogui.alert(button='넵', text='캐릭터를 선택해 주시지예', title='뭐합니꺼')
        elif onDunjeon == '던전 선택' or onDunjeon == 'none' or onDunjeon_level == 0 or onDunjeon_level == '층수 선택':
            pyautogui.alert(button='넵', text='던전 및 층수를 선택해 주시지예', title='아 진짜 뭐합니꺼')
        elif onCharacter != 0 and onDunjeon != '던전 선택':
            print('char_', char_)
            print('dun_', dun_)
            data = "One:" + char_ + ":" + dun_ + ":대기중:" + "Two:" + char_ + ":" + dun_ + ":대기중\n"
            print(data)
            self.onActivated_dunjeon_add2(data)
        #     result = self.mySchedule_add(data)
        # if result == True:
        #     # self.set_rand_int()
        #     self.__init__()

    def onActivated_dunjeon_add2(self, data):
        global onCharacter, onDunjeon, rowcount, colcount
        print("rowcount", rowcount)
        print("colcount", colcount)
        self.table_load()

        print("data", data)
        # self.tableWidget.removeRow(5)
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        row_add = self.tableWidget.rowCount() - 1
        data_ = re.sub("\n", "", data)
        datas = data_.split(":")
        # datas = dataed.replace("\n", "")
        print("datas", datas)
        print("datas", datas[0])
        print(len(datas))
        print(range(colcount))
        for i in range(len(datas)):
            self.tableWidget.setItem(row_add, i, QTableWidgetItem(datas[i]))
        self.mySchedule_add(data)
        rowcount = self.tableWidget.rowCount()

    def onActivated_hunt_add(self):
        global onCharacter, onHunt
        char_ = onCharacter
        hun_ = "사냥_" + "아빌리우스_" + onHunt
        if onCharacter == 0:
            pyautogui.alert(button='넵', text='캐릭터를 선택해 주시지예', title='뭐합니꺼')
        elif onHunt == '< 아빌리우스 >' or onHunt == 'none':
            pyautogui.alert(button='넵', text='던전을 선택해 주시지예', title='뭐합니꺼')
        elif onCharacter != 0 and onHunt != '< 아빌리우스 >':
            print('char_', char_)
            print('dun_', hun_)
            data = "One:" + char_ + ":" + hun_ + ":대기중:" + "Two:" + char_ + ":" + hun_ + ":대기중\n"
            print(data)
            self.onActivated_hunt_add2(data)
    def onActivated_hunt_add_2(self):
        global onCharacter, onHunt2
        char_ = onCharacter
        hun_ = "사냥_" + "바스티움_" + onHunt2
        if onCharacter == 0:
            pyautogui.alert(button='넵', text='캐릭터를 선택해 주시지예', title='뭐합니꺼')
        elif onHunt2 == '< 바스티움 >' or onHunt2 == 'none':
            pyautogui.alert(button='넵', text='던전을 선택해 주시지예', title='뭐합니꺼')
        elif onCharacter != 0 and onHunt2 != '< 바스티움 >':
            print('char_', char_)
            print('dun_', hun_)
            data = "One:" + char_ + ":" + hun_ + ":대기중:" + "Two:" + char_ + ":" + hun_ + ":대기중\n"
            print(data)
            self.onActivated_hunt_add2(data)
    def onActivated_hunt_add_3(self):
        global onCharacter, onHunt3
        char_ = onCharacter
        hun_ = "사냥_" + "첼라노_" + onHunt3
        if onCharacter == 0:
            pyautogui.alert(button='넵', text='캐릭터를 선택해 주시지예', title='뭐합니꺼')
        elif onHunt3 == '< 첼라노 >' or onHunt3 == 'none':
            pyautogui.alert(button='넵', text='던전을 선택해 주시지예', title='뭐합니꺼')
        elif onCharacter != 0 and onHunt != '< 첼라노 >':
            print('char_', char_)
            print('dun_', hun_)
            data = "One:" + char_ + ":" + hun_ + ":대기중:" + "Two:" + char_ + ":" + hun_ + ":대기중\n"
            print(data)
            self.onActivated_hunt_add2(data)

    def onActivated_hunt_add2(self, data):
        global onCharacter, onDunjeon, rowcount, colcount
        print("rowcount", rowcount)
        print("colcount", colcount)
        self.table_load()

        print("data", data)
        # self.tableWidget.removeRow(5)
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        row_add = self.tableWidget.rowCount() - 1
        data_ = re.sub("\n", "", data)
        datas = data_.split(":")
        # datas = dataed.replace("\n", "")
        print("datas", datas)
        print("datas", datas[0])
        print(len(datas))
        print(range(colcount))
        for i in range(len(datas)):
            self.tableWidget.setItem(row_add, i, QTableWidgetItem(datas[i]))
            self.tableWidget.item(row_add, i).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.mySchedule_add(data)
        rowcount = self.tableWidget.rowCount()

    def onActivated_maul_add(self):
        global onCharacter, onMaul
        char_ = onCharacter
        maul_ = onMaul
        if onCharacter == 0:
            pyautogui.alert(button='넵', text='캐릭터를 선택해 주시지예', title='뭐합니꺼')
        elif onMaul == '마을 의뢰 장소 선택' or onMaul == 'none':
            pyautogui.alert(button='넵', text='마을 의뢰 장소를 선택해 주시지예', title='아 진짜 뭐합니꺼')
        elif onCharacter != 0 and onMaul != '마을 의뢰 장소 선택':
            print('char_', char_)
            print('maul_', maul_)
            data = "One:" + char_ + ":" + maul_ + ":대기중:" + "Two:" + char_ + ":" + maul_ + ":대기중\n"
            print(data)
            self.onActivated_maul_add2(data)
        #     result = self.mySchedule_add(data)
        # if result == True:
        #     # self.set_rand_int()
        #     self.__init__()

    def onActivated_maul_add2(self, data):
        global onCharacter, onMaul, rowcount, colcount
        print("rowcount", rowcount)
        print("colcount", colcount)
        self.table_load()

        print("data", data)
        # self.tableWidget.removeRow(5)
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        row_add = self.tableWidget.rowCount() - 1
        data_ = re.sub("\n", "", data)
        datas = data_.split(":")
        # datas = dataed.replace("\n", "")
        print("datas", datas)
        print("datas", datas[0])
        print(len(datas))
        print(range(colcount))
        for i in range(len(datas)):
            self.tableWidget.setItem(row_add, i, QTableWidgetItem(datas[i]))
        self.mySchedule_add(data)
        rowcount = self.tableWidget.rowCount()

    def mystatus_refresh(self):
        print("현재상태 초기화")
        # 초기화 시간
        dir_path = "C:\\my_games\\nightcrows"
        file_path2 = dir_path + "\\mysettings\\refresh_time\\quest.txt"
        file_path13 = dir_path + "\\mysettings\\refresh_time\\refresh_time.txt"

        isRefresh = False
        while isRefresh is False:
            if os.path.isfile(file_path13) == True:
                with open(file_path13, "r", encoding='utf-8-sig') as file:
                    refresh_time = file.read()
                    refresh_time_bool = refresh_time.isdigit()
                    if refresh_time_bool == True:
                        isRefresh = True
                        print("refresh_time", refresh_time)
                    else:
                        with open(file_path13, "w", encoding='utf-8-sig') as file:
                            file.write(str(4))
            else:
                with open(file_path13, "w", encoding='utf-8-sig') as file:
                    file.write(str(4))

        if os.path.isfile(file_path2) == True:
            # 파일 읽기
            with open(file_path2, "r", encoding='utf-8-sig') as file:
                lines2 = file.read().splitlines()
                day_ = lines2[0].split(":")
                re_time_ = str(day_[0]) + " => " + str(day_[1] + "시")
                print("최근 초기화 시간 : ", re_time_)
        else:
            re_time_ = "아직 모름..."
        self.my_refresh_time.setText("현재 초기화 시간 : " + str(refresh_time) + "\n\n" + "최근 초기화한 시간 : " + re_time_)
        self.set_rand_int()

    def set_rand_int(self):
        try:
            dir_path = "C:\\my_games\\nightcrows"
            file_path = dir_path + "\\mysettings\\myschedule\\schedule.txt"
            file_path3 = dir_path + "\\mysettings\\myschedule\\schedule2.txt"
            if os.path.isfile(file_path) == True:
                # 파일 읽기
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    lines = file.read().splitlines()
            else:
                print('파일 없당')
                if os.path.isdir(dir_path) == True:
                    print('디렉토리 존재함')
                    with open(file_path3, "r", encoding='utf-8-sig') as file:
                        shcedule = file.read().splitlines()
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(str(shcedule))
                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                lines = file.read().splitlines()
                else:
                    print('디렉토리 존재하지 않음')
                    os.makedirs(dir_path)
                    with open(file_path3, "r", encoding='utf-8-sig') as file:
                        shcedule = file.read().splitlines()
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(shcedule)
                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                lines = file.read().splitlines()

            print("ggggggggggggggggg", lines)

            # self.tableWidget.insertRow(self.tableWidget.rowCount(2))
            self.tableWidget.setColumnWidth(0, 50)
            self.tableWidget.setColumnWidth(1, 40)
            self.tableWidget.setColumnWidth(2, 200)
            self.tableWidget.setColumnWidth(3, 100)
            self.tableWidget.setColumnWidth(4, 50)
            self.tableWidget.setColumnWidth(5, 40)
            self.tableWidget.setColumnWidth(6, 200)
            self.tableWidget.setColumnWidth(7, 100)

            for i in range(len(lines)):
                result = str(lines[i]).split(":")
                for j in range(len(result)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem())
                    self.tableWidget.item(i, j).setText(str(result[j].replace("\n", "")))
                    self.tableWidget.item(i, j).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                    # self.tableWidget.resizeColumnsToContents()

        except Exception as e:
            print(e)
            return 0

    def set_rand_int_jinhang(self, cla):
        try:
            dir_path = "C:\\my_games\\nightcrows"
            file_path = dir_path + "\\mysettings\\myschedule\\schedule.txt"
            file_path3 = dir_path + "\\mysettings\\myschedule\\schedule2.txt"
            if os.path.isfile(file_path) == True:
                # 파일 읽기
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    lines = file.read().splitlines()
                    print("lines", lines)
                    print("len(lines)", len(lines))
            else:
                print('파일 없당')
                if os.path.isdir(dir_path) == True:
                    print('디렉토리 존재함')
                    with open(file_path3, "r", encoding='utf-8-sig') as file:
                        shcedule = file.read().splitlines()
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(shcedule)
                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                lines = file.read().splitlines()
                else:
                    print('디렉토리 존재하지 않음')
                    os.makedirs(dir_path)
                    with open(file_path3, "r", encoding='utf-8-sig') as file:
                        shcedule = file.read().splitlines()
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(shcedule)
                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                lines = file.read().splitlines()

            ########################################
            cla_schedule = ""
            for i in range(len(lines)):
                complete_ = lines[i].split(":")
                for j in range(len(complete_)):
                    if cla == 'one':
                        if j < 3:
                            cla_schedule += complete_[j] + ":"
                        if j == 3:
                            cla_schedule += complete_[3] + "\n"
                    if cla == 'two':
                        if 3 < j < 7:
                            cla_schedule += complete_[j] + ":"
                        if j == 7:
                            cla_schedule += complete_[7] + "\n"
            # 시작 스케쥴 파악하기
            forBreak = False
            schedule_ = cla_schedule.split("\n")
            schedule_ = ' '.join(schedule_).split()
            print("schedule_", schedule_)
            for i in range(len(schedule_)):
                schedule_2 = schedule_[i].split(":")
                for j in range(len(schedule_2)):
                    if schedule_2[3] != "완료":
                        forBreak = True
                        print("대기중인 첫번째", i)
                        start_ = i
                        break
                if forBreak == True:
                    break
            print("진행중인 줄", start_)
            start = schedule_[start_].split(":")
            start = ' '.join(start).split()
            print("start[3]! 대기중을 진행중으로 보이게 하기", start[3])
            # start_ 줄(i), 진행중 (start[3])

            cla_schedule = ""
            for i in range(len(lines)):
                complete_ = lines[i].split(":")
                for j in range(len(complete_)):
                    if cla == 'one' and i == start_ and j == 3:
                        cla_schedule += complete_[j].replace("대기중", "진행중:")
                    elif cla == 'two' and i == start_ and j == 7:
                        cla_schedule += complete_[j].replace("대기중", "진행중\n")
                    else:
                        if j == 7:
                            cla_schedule += complete_[j] + "\n"
                        else:
                            cla_schedule += complete_[j] + ":"
            print("cla_schedule", cla_schedule)
            mycla_schedule = cla_schedule.split('\n')
            mycla_schedule = ' '.join(mycla_schedule).split()
            print("mycla_schedule", mycla_schedule)

            remove_ = self.tableWidget.rowCount()
            print("remove_", remove_)
            for i in range(remove_ - 1):
                self.tableWidget.removeRow(0)

            rowcount = self.tableWidget.rowCount()
            print("refresh_rowcount", self.tableWidget.rowCount())
            count_ = len(mycla_schedule) - rowcount
            for i in range(count_):
                self.tableWidget.insertRow(self.tableWidget.rowCount())
            print("refresh_rowcount2", self.tableWidget.rowCount())

            # self.tableWidget.clear

            # self.tableWidget.insertRow(self.tableWidget.rowCount(2))

            # self.tableWidget.setColumnWidth(0, 50)
            # self.tableWidget.setColumnWidth(1, 40)
            # self.tableWidget.setColumnWidth(2, 200)
            # self.tableWidget.setColumnWidth(3, 100)
            # self.tableWidget.setColumnWidth(4, 50)
            # self.tableWidget.setColumnWidth(5, 40)
            # self.tableWidget.setColumnWidth(6, 200)
            # self.tableWidget.setColumnWidth(7, 100)

            for i in range(len(mycla_schedule)):
                result = str(mycla_schedule[i]).split(":")
                for j in range(len(result)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem())
                    self.tableWidget.item(i, j).setText(str(result[j]))
                    self.tableWidget.item(i, j).setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            # time.sleep(0.2)
            self.tableWidget.clear


        except Exception as e:
            print(e)
            return 0

    def set_label(self, row, column):
        global thisRow, thisCol
        item = self.tableWidget.item(row, column)
        value = item.text()
        col = str(row + 1)
        col_ = int(col)
        col2 = str(column + 1)
        col_2 = int(col2)
        thisRow = col_
        thisCol = col_2
        print("0열 데이타", col_)  # good
        print("Row", str(row + 1))
        print("Column", str(column + 1))
        print("value", str(value))
        label_str = 'Row: ' + str(row + 1) + ', Column: ' + str(column + 1) + ', Value: ' + str(value)
        self.label.setText(label_str)

    # 스케쥴 수정 및 추가
    def sche_load_(self):
        global table_datas
        try:
            rowcount = self.tableWidget.rowCount()
            print("schedule!!!")
            datas = ""
            if rowcount != 0:
                for i in range(0, rowcount):
                    for j in range(0, colcount):
                        data = self.tableWidget.item(i, j)
                        if data is not None:
                            if j + 1 == colcount:
                                datas += str(data.text()) + "\n"
                            else:
                                datas += str(data.text()) + ":"

                        else:
                            print("blank")
            # redata = ' '.join(datas).split()
            table_datas = datas
            return table_datas
        except Exception as e:
            print(e)
            return 0

    def table_load(self):
        global rowcount, colcount
        print("rowcount", rowcount)
        print("colcount", colcount)
        if rowcount != 0:
            for i in range(0, rowcount):
                for j in range(0, colcount):
                    data = self.tableWidget.item(i, j)
                    if data is not None:
                        if j + 1 == colcount:
                            item = QTableWidgetItem()
                            item.setText(str(data.text()))
                            # datas += str(data.text()) + "\n"
                            self.tableWidget.setItem(i, j, item)
                        else:
                            item = QTableWidgetItem()
                            item.setText(str(data.text()))
                            # datas += str(data.text()) + ":"
                            self.tableWidget.setItem(i, j, item)

                    else:
                        print("blank")

    def sche_up_modify(self):
        global thisRow, thisCol, rowcount
        try:
            rowcount = self.tableWidget.rowCount()
            last_1 = ""
            last_2 = ""
            last_result = ""
            modi_result = ""
            print("sche_up_modify", thisRow)
            result_ = self.sche_load_()
            modi_ready__ = result_.split("\n")
            modi_ready_ = " ".join(modi_ready__).split()
            if thisRow > 1:
                print("len(modi_ready_up)", len(modi_ready_))
                for i in range(len(modi_ready_)):

                    # if i + 1 == len(modi_ready_):
                    #     modi_result += modi_ready_[i]

                    if i == thisRow - 2:
                        modi_result += modi_ready_[i + 1] + "\n"

                    elif i == thisRow - 1:
                        modi_result += modi_ready_[i - 1] + "\n"

                    else:
                        modi_result += modi_ready_[i] + "\n"

                modi_result__ = modi_result.split("\n")
                print("modi_ready__!!!!!!!!!!!!!", modi_ready__)
                print("modi_result__!!!!!!!!!!!", modi_result__)

                modi_spl_1 = modi_ready_[thisRow - 2].split(":")  # 바뀌기전 5678 => 그대로
                modi_spl_2 = modi_ready_[thisRow - 1].split(":")  # 바뀌기전 5678 => 그대로

                modi_spl_3 = modi_result__[thisRow - 2].split(":")  # 바뀐 후 1234 => 바꾸기 b
                modi_spl_4 = modi_result__[thisRow - 1].split(":")  # 바뀐후 1234 => 바꾸기 a

                #      4번기준
                #      thisRow - 2
                #      modi_spl_3 + modi_spl_2
                #      thisRow - 1
                #      modi_spl_1 + modi_spl_4
                # else:
                #     thisRow - 2
                #     modi_spl_1 + modi_spl_4
                #     thisRow - 1
                #     modi_spl_3 + modi_spl_2##################나중에 마지막줄을 올릴때 잘못 처리되는거 수정하기

                if thisCol < 5:

                    last_1 = str(modi_spl_3[0]) + ":" + str(modi_spl_3[1]) + ":" + str(modi_spl_3[2]) + ":" + str(
                        modi_spl_3[3]) + ":" + str(modi_spl_1[4]) + ":" + str(modi_spl_1[5]) + ":" + str(
                        modi_spl_1[6]) + ":" + str(modi_spl_1[7])
                    last_2 = str(modi_spl_4[0]) + ":" + str(modi_spl_4[1]) + ":" + str(modi_spl_4[2]) + ":" + str(
                        modi_spl_4[3]) + ":" + str(modi_spl_2[4]) + ":" + str(modi_spl_2[5]) + ":" + str(
                        modi_spl_2[6]) + ":" + str(modi_spl_2[7])
                else:

                    last_1 = str(modi_spl_1[0]) + ":" + str(modi_spl_1[1]) + ":" + str(modi_spl_1[2]) + ":" + str(
                        modi_spl_1[3]) + ":" + str(modi_spl_3[4]) + ":" + str(modi_spl_3[5]) + ":" + str(
                        modi_spl_3[6]) + ":" + str(modi_spl_3[7])
                    last_2 = str(modi_spl_2[0]) + ":" + str(modi_spl_2[1]) + ":" + str(modi_spl_2[2]) + ":" + str(
                        modi_spl_2[3]) + ":" + str(modi_spl_4[4]) + ":" + str(modi_spl_4[5]) + ":" + str(
                        modi_spl_4[6]) + ":" + str(modi_spl_4[7])

                for i in range(len(modi_result__)):
                    print("last_result", modi_result__[i])
                    # if i == len(modi_result__) - 1:
                    #     last_result += str(modi_result__[i]) + 'a'
                    #     # last_result += str(i) + str(modi_result__[i])
                    #     print("i", i)
                    if thisRow - 1 == i:
                        last_result += last_2 + "\n"
                    elif thisRow - 2 == i:
                        last_result += last_1 + "\n"
                    elif i == len(modi_result__) - 1:
                        last_result += str(modi_result__[i]) + ''
                        # last_result += str(i) + str(modi_result__[i])
                        print("i", i)
                    else:
                        last_result += str(modi_result__[i]) + "\n"

                print("last_result_up", last_result)
                how_ = 'modify'
                modi_result_ = self.mySchedule_change(how_, last_result)

                if modi_result_ == True:
                    thisRow -= 1
                    self.set_rand_int()
                else:
                    print("수정 실패")


            else:
                pyautogui.alert(button='넵', text='수정할 행을 선택해 주세요', title='확인해주이소')
                print("수정할 행을 선택해 주세요. 추후 알러트로...")

        #      4번기준
        #      thisRow - 2
        #      modi_spl_3 + modi_spl_2
        #      thisRow - 1
        #      modi_spl_1 + modi_spl_4
        # else:
        #     thisRow - 2
        #     modi_spl_1 + modi_spl_4
        #     thisRow - 1
        #     modi_spl_3 + modi_spl_2

        except Exception as e:
            print(e)
            return 0

    def sche_down_modify(self):
        global thisRow, thisCol, rowcount
        try:
            rowcount = self.tableWidget.rowCount()
            last_1 = ""
            last_2 = ""
            last_result = ""
            modi_result = ""
            print("sche_down_modify", thisRow)
            result_ = self.sche_load_()
            modi_ready__ = result_.split("\n")
            modi_ready_ = " ".join(modi_ready__).split()
            if thisRow < len(modi_ready_):
                print("len(modi_ready_down)", len(modi_ready_))
                for i in range(len(modi_ready_)):

                    # if i + 1 == len(modi_ready_):
                    #     modi_result += modi_ready_[i]
                    if thisRow == i:
                        modi_result += modi_ready_[i - 1] + "\n"
                    elif thisRow - 1 == i:
                        modi_result += modi_ready_[i + 1] + "\n"
                    else:
                        modi_result += modi_ready_[i] + "\n"

                modi_result__ = modi_result.split("\n")

                modi_spl_1 = modi_ready_[thisRow - 1].split(":")  # 바뀌기전 1234 => 바꾸기
                modi_spl_2 = modi_ready_[thisRow].split(":")  # 바뀌기전 5678 => 그대로
                modi_spl_3 = modi_result__[thisRow - 1].split(":")  # 바뀐 후 1234 => 바꾸기
                modi_spl_4 = modi_result__[thisRow].split(":")  # 바뀐후 5678 => 그대로

                if thisCol < 5:

                    last_1 = str(modi_spl_3[0]) + ":" + str(modi_spl_3[1]) + ":" + str(modi_spl_3[2]) + ":" + str(
                        modi_spl_3[3]) + ":" + str(modi_spl_1[4]) + ":" + str(modi_spl_1[5]) + ":" + str(
                        modi_spl_1[6]) + ":" + str(modi_spl_1[7])
                    last_2 = str(modi_spl_4[0]) + ":" + str(modi_spl_4[1]) + ":" + str(modi_spl_4[2]) + ":" + str(
                        modi_spl_4[3]) + ":" + str(modi_spl_2[4]) + ":" + str(modi_spl_2[5]) + ":" + str(
                        modi_spl_2[6]) + ":" + str(modi_spl_2[7])
                else:

                    last_1 = str(modi_spl_1[0]) + ":" + str(modi_spl_1[1]) + ":" + str(modi_spl_1[2]) + ":" + str(
                        modi_spl_1[3]) + ":" + str(modi_spl_3[4]) + ":" + str(modi_spl_3[5]) + ":" + str(
                        modi_spl_3[6]) + ":" + str(modi_spl_3[7])
                    last_2 = str(modi_spl_2[0]) + ":" + str(modi_spl_2[1]) + ":" + str(modi_spl_2[2]) + ":" + str(
                        modi_spl_2[3]) + ":" + str(modi_spl_4[4]) + ":" + str(modi_spl_4[5]) + ":" + str(
                        modi_spl_4[6]) + ":" + str(modi_spl_4[7])

                for i in range(len(modi_result__)):

                    if i + 1 == len(modi_result__):
                        last_result += str(modi_result__[i])
                    elif thisRow - 1 == i:
                        last_result += last_1 + "\n"
                    elif thisRow == i:
                        last_result += last_2 + "\n"
                    else:
                        last_result += str(modi_result__[i]) + "\n"

                print("last_result_down", last_result)
                how_ = 'modify'
                modi_result_ = self.mySchedule_change(how_, last_result)
                if modi_result_ == True:
                    thisRow += 1
                    self.set_rand_int()
                else:
                    print("수정 실패")

            else:
                pyautogui.alert(button='넵', text='수정할 행을 선택해 주세요', title='확인해주이소')
                print("수정할 행을 선택해 주세요. 추후 알러트로...")

        except Exception as e:
            print(e)
            return 0

    def mySchedule_del(self):
        global rowcount, colcount
        try:
            self.table_load()
            rowcount = self.tableWidget.rowCount()
            print("rowcount", rowcount)
            self.tableWidget.removeRow(thisRow - 1)
            rowcount = self.tableWidget.rowCount()
            print("rowcount", rowcount)
            print("del")
            result = self.sche_load_()
            print("result", result)
            how_ = "modify"
            self.mySchedule_change(how_, result)
            self.mystatus_refresh()

        except Exception as e:
            print(e)
            return 0

    def mySchedule_refresh(self):
        try:
            ##############다시 코딩

            v_.one_cla_count = 0
            v_.two_cla_count = 0
            v_.one_cla_ing = 'check'
            v_.two_cla_ing = 'check'
            v_.one_cla_get_event = False
            v_.two_cla_get_event = False

            # myQuest_number_check('all', 'refresh')

            dir_path = "C:\\my_games\\nightcrows"
            file_path = dir_path + "\\mysettings\\myschedule\\schedule.txt"
            file_path2 = dir_path + "\\mysettings\\refresh_time\\quest.txt"
            file_path3 = dir_path + "\\mysettings\\myschedule\\schedule2.txt"
            file_path13 = dir_path + "\\mysettings\\refresh_time\\refresh_time.txt"

            if os.path.isdir(dir_path) == False:
                print('디렉토리 존재하지 않음')
                os.makedirs(dir_path)

            isRefresh = False
            while isRefresh is False:
                if os.path.isfile(file_path13) == True:
                    with open(file_path13, "r", encoding='utf-8-sig') as file:
                        refresh_time = file.read()
                        refresh_time_bool = refresh_time.isdigit()
                        if refresh_time_bool == True:
                            isRefresh = True
                            print("refresh_time", refresh_time)
                        else:
                            with open(file_path13, "w", encoding='utf-8-sig') as file:
                                file.write(str(4))
                else:
                    with open(file_path13, "w", encoding='utf-8-sig') as file:
                        file.write(str(4))

            with open(file_path3, "r", encoding='utf-8-sig') as file:
                lines = file.read()
                # lines = file.read().splitlines()
                print('line_refresh', lines)
            with open(file_path, "w", encoding='utf-8-sig') as file:
                file.write(lines)

            nowDay_ = datetime.today().strftime("%Y%m%d")
            nowDay = int(nowDay_)
            nowTime = int(datetime.today().strftime("%H"))
            yesterday_ = date.today() - timedelta(1)
            yesterday = int(yesterday_.strftime('%Y%m%d'))

            if nowTime >= int(refresh_time):
                nowDay = str(nowDay)
            else:
                nowDay = yesterday
                nowDay = str(nowDay)
            with open(file_path2, "w", encoding='utf-8-sig') as file:
                file.write(str(nowDay) + ":" + str(refresh_time) + "\n")

            remove_ = self.tableWidget.rowCount()
            print("remove_", remove_)
            for i in range(remove_ - 1):
                self.tableWidget.removeRow(0)

            refresh_result = lines.split("\n")
            rowcount = self.tableWidget.rowCount()
            print("refresh_rowcount", self.tableWidget.rowCount())
            count_ = len(refresh_result) - rowcount - 1
            for i in range(count_):
                self.tableWidget.insertRow(self.tableWidget.rowCount())
            print("refresh_rowcount2", self.tableWidget.rowCount())
            self.set_rand_int()

        except Exception as e:
            print(e)
            return 0


    def mySchedule_refresh_all(self):
        try:
            ##############다시 코딩

            v_.one_cla_count = 0
            v_.two_cla_count = 0
            v_.one_cla_ing = 'check'
            v_.two_cla_ing = 'check'
            v_.one_cla_get_event = False
            v_.two_cla_get_event = False

            # myQuest_number_check('all', 'refresh')

            dir_path = "C:\\my_games\\nightcrows"
            file_path = dir_path + "\\mysettings\\myschedule\\schedule.txt"
            file_path2 = dir_path + "\\mysettings\\refresh_time\\quest.txt"
            file_path3 = dir_path + "\\mysettings\\myschedule\\schedule2.txt"
            file_path13 = dir_path + "\\mysettings\\refresh_time\\refresh_time.txt"

            if os.path.isdir(dir_path) == False:
                print('디렉토리 존재하지 않음')
                os.makedirs(dir_path)

            isRefresh = False
            while isRefresh is False:
                if os.path.isfile(file_path13) == True:
                    with open(file_path13, "r", encoding='utf-8-sig') as file:
                        refresh_time = file.read()
                        refresh_time_bool = refresh_time.isdigit()
                        if refresh_time_bool == True:
                            isRefresh = True
                            print("refresh_time", refresh_time)
                        else:
                            with open(file_path13, "w", encoding='utf-8-sig') as file:
                                file.write(str(4))
                else:
                    with open(file_path13, "w", encoding='utf-8-sig') as file:
                        file.write(str(4))

            with open(file_path3, "r", encoding='utf-8-sig') as file:
                reset_schedule_ = ""
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    lines = file.read().splitlines()
                    lines = ' '.join(lines).split()

                    isSchedule_ = False
                    while isSchedule_ is False:
                        if lines == [] or lines == "":
                            print("스케쥴이 비었다 : myQuest_play_check")
                            with open(file_path3, "r", encoding='utf-8-sig') as file:
                                schedule_ready = file.read()
                            with open(file_path, "w", encoding='utf-8-sig') as file:
                                file.write(schedule_ready)
                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                lines = file.read().splitlines()
                        else:
                            isSchedule_ = True

                    for i in range(len(lines)):
                        complete_ = lines[i].split(":")
                        for j in range(len(complete_)):
                            if j < 3:
                                reset_schedule_ += complete_[j] + ":"
                            if j == 3:
                                reset_schedule_ += '대기중:'
                            if 3 < j < 7:
                                reset_schedule_ += complete_[j] + ":"
                            if j == 7:
                                reset_schedule_ += "대기중\n"
                    print('reset_schedule_', reset_schedule_)
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(reset_schedule_)
                    with open(file_path3, "w", encoding='utf-8-sig') as file:
                        file.write(reset_schedule_)
            # with open(file_path, "w", encoding='utf-8-sig') as file:
            #     file.write(lines)
            with open(file_path3, "r", encoding='utf-8-sig') as file:
                lines = file.read()

            nowDay_ = datetime.today().strftime("%Y%m%d")
            nowDay = int(nowDay_)
            nowTime = int(datetime.today().strftime("%H"))
            yesterday_ = date.today() - timedelta(1)
            yesterday = int(yesterday_.strftime('%Y%m%d'))

            if nowTime >= int(refresh_time):
                nowDay = str(nowDay)
            else:
                nowDay = yesterday
                nowDay = str(nowDay)
            with open(file_path2, "w", encoding='utf-8-sig') as file:
                file.write(str(nowDay) + ":" + str(refresh_time) + "\n")

            remove_ = self.tableWidget.rowCount()
            print("remove_", remove_)
            for i in range(remove_ - 1):
                self.tableWidget.removeRow(0)

            refresh_result = lines.split("\n")
            rowcount = self.tableWidget.rowCount()
            print("refresh_rowcount", self.tableWidget.rowCount())
            count_ = len(refresh_result) - rowcount - 1
            for i in range(count_):
                self.tableWidget.insertRow(self.tableWidget.rowCount())
            print("refresh_rowcount2", self.tableWidget.rowCount())
            self.set_rand_int()

        except Exception as e:
            print(e)
            return 0


    def mySchedule_is(self):
        try:
            ##############다시 코딩
            dir_path = "C:\\my_games\\nightcrows"
            file_path = dir_path + "\\mysettings\\myschedule\\schedule.txt"
            if os.path.isfile(file_path) == True:
                # 파일 읽기
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    lines = file.read()

            remove_ = self.tableWidget.rowCount()
            print("remove_", remove_)
            for i in range(remove_ - 1):
                self.tableWidget.removeRow(0)

            refresh_result = lines.split("\n")
            rowcount = self.tableWidget.rowCount()
            print("refresh_rowcount", self.tableWidget.rowCount())
            count_ = len(refresh_result) - rowcount - 1
            for i in range(count_):
                self.tableWidget.insertRow(self.tableWidget.rowCount())
            print("refresh_rowcount2", self.tableWidget.rowCount())
            self.tableWidget.clear
            self.set_rand_int()
            self.tableWidget.clear
        except Exception as e:
            print(e)
            return 0

    def mySchedule_add(self, data):
        try:
            schedule_add = False
            how_ = 'add'
            datas = str(data)
            result = self.mySchedule_change(how_, datas)
            print("added_", result)
            if result == True:
                schedule_add = True
                self.mystatus_refresh()
                print('스케쥴 추가 됨')

            return schedule_add
        except Exception as e:
            print(e)
            return 0

    def mySchedule_change(self, how_, datas):
        try:
            ishow_ = False
            dir_path = "C:\\my_games\\nightcrows"
            file_path = dir_path + "\\mysettings\\myschedule\\schedule.txt"
            file_path3 = dir_path + "\\mysettings\\myschedule\\schedule2.txt"
            print(os.path.isfile(file_path))
            print(os.path.isdir(dir_path))

            if os.path.isdir(dir_path) == True:
                print('디렉토리 존재')
            else:
                os.makedirs(dir_path)

            print("how_", how_)
            if how_ == "add":
                with open(file_path, "a", encoding='utf-8-sig') as file:
                    print("add????", datas)
                    file.write(datas)
                    ishow_ = True
                # reset_schedule_ = ""
                # with open(file_path, "r", encoding='utf-8-sig') as file:
                #     lines = file.read().splitlines()
                #     lines = ' '.join(lines).split()
                #     print("lineslineslineslineslineslineslineslineslineslineslines", lines)
                #     for i in range(len(lines)):
                #         complete_ = lines[i].split(":")
                #         for j in range(len(complete_)):
                #             if j < 3:
                #                 reset_schedule_ += complete_[j] + ":"
                #             if j == 3:
                #                 reset_schedule_ += '대기중:'
                #             if 3 < j < 7:
                #                 reset_schedule_ += complete_[j] + ":"
                #             if j == 7:
                #                 reset_schedule_ += "대기중\n"
                #     print("reset_schedule_reset_schedule_reset_schedule_reset_schedule_reset_schedule_",
                #           reset_schedule_)
                #     with open(file_path3, "w", encoding='utf-8-sig') as file:
                #         file.write(reset_schedule_)
                ishow_ = True
                reset_schedule_ = ""
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    lines = file.read().splitlines()
                    lines = ' '.join(lines).split()

                    isSchedule_ = False
                    while isSchedule_ is False:
                        if lines == [] or lines == "":
                            print("스케쥴이 비었다 : myQuest_play_check")
                            with open(file_path3, "r", encoding='utf-8-sig') as file:
                                schedule_ready = file.read()
                            with open(file_path, "w", encoding='utf-8-sig') as file:
                                file.write(schedule_ready)
                            with open(file_path, "r", encoding='utf-8-sig') as file:
                                lines = file.read().splitlines()
                        else:
                            isSchedule_ = True

                    for i in range(len(lines)):
                        complete_ = lines[i].split(":")
                        for j in range(len(complete_)):
                            if j < 3:
                                reset_schedule_ += complete_[j] + ":"
                            if j == 3:

                                if '_' in complete_[2]:
                                    dunjeon_spl_ = complete_[2].split("_")
                                    print("dunjeon_spl_[0]", dunjeon_spl_[0])
                                    print("dunjeon_spl_[1]", dunjeon_spl_[1])

                                    # if dunjeon_spl_[1] == "신전" or dunjeon_spl_[1] == "동굴":
                                    if dunjeon_spl_[1] == "신전":
                                        reset_schedule_ += complete_[j] + ":"
                                    else:
                                        reset_schedule_ += '대기중:'
                                else:
                                    reset_schedule_ += '대기중:'

                                # if complete_[2] == "지하감옥":
                                #     reset_schedule_ += complete_[j] + ":"
                                # else:
                                #     reset_schedule_ += '대기중:'
                            if 3 < j < 7:
                                reset_schedule_ += complete_[j] + ":"
                            if j == 7:

                                if '_' in complete_[6]:
                                    dunjeon_spl_ = complete_[6].split("_")
                                    print("dunjeon_spl_[0]", dunjeon_spl_[0])
                                    print("dunjeon_spl_[1]", dunjeon_spl_[1])

                                    # if dunjeon_spl_[1] == "신전" or dunjeon_spl_[1] == "동굴":
                                    if dunjeon_spl_[1] == "신전":
                                        reset_schedule_ += complete_[j] + "\n"
                                    else:
                                        reset_schedule_ += "대기중\n"
                                else:
                                    reset_schedule_ += "대기중\n"

                                # if complete_[6] == "지하감옥":
                                #     reset_schedule_ += complete_[j] + "\n"
                                # else:
                                #     reset_schedule_ += "대기중\n"

                    print('reset_schedule_', reset_schedule_)
                    # with open(file_path, "w", encoding='utf-8-sig') as file:
                    #     file.write(reset_schedule_)
                    with open(file_path3, "w", encoding='utf-8-sig') as file:
                        file.write(reset_schedule_)
                self.set_rand_int()

            elif how_ == "modify":

                # with open(file_path, "w", encoding='utf-8-sig') as file:
                #     file.write(datas)
                #     ishow_ = True
                #     reset_schedule_ = ""
                #     lines = datas
                #     lines = lines.split('\n')
                #     lines = ' '.join(lines).split()
                #     for i in range(len(lines)):
                #         complete_ = lines[i].split(":")
                #         for j in range(len(complete_)):
                #             if j < 3:
                #                 reset_schedule_ += complete_[j] + ":"
                #             if j == 3:
                #                 reset_schedule_ += '대기중:'
                #             if 3 < j < 7:
                #                 reset_schedule_ += complete_[j] + ":"
                #             if j == 7:
                #                 reset_schedule_ += "대기중\n"
                #
                # with open(file_path3, "w", encoding='utf-8-sig') as file:
                #     file.write(reset_schedule_)

                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write(datas)

                ishow_ = True
                reset_schedule_ = ""
                lines = datas
                lines = lines.split('\n')
                lines = ' '.join(lines).split()



                for i in range(len(lines)):
                    complete_ = lines[i].split(":")
                    for j in range(len(complete_)):
                        if j < 3:
                            reset_schedule_ += complete_[j] + ":"
                        if j == 3:

                            if '_' in complete_[2]:
                                dunjeon_spl_ = complete_[2].split("_")
                                print("dunjeon_spl_[0]", dunjeon_spl_[0])
                                print("dunjeon_spl_[1]", dunjeon_spl_[1])

                                # if dunjeon_spl_[1] == "신전" or dunjeon_spl_[1] == "동굴":
                                if dunjeon_spl_[1] == "신전":
                                    reset_schedule_ += complete_[j] + ":"
                                else:
                                    reset_schedule_ += '대기중:'
                            else:
                                reset_schedule_ += '대기중:'

                            # if complete_[2] == "지하감옥":
                            #     reset_schedule_ += complete_[j] + ":"
                            # else:
                            #     reset_schedule_ += '대기중:'
                        if 3 < j < 7:
                            reset_schedule_ += complete_[j] + ":"
                        if j == 7:

                            if '_' in complete_[6]:
                                dunjeon_spl_ = complete_[6].split("_")
                                print("dunjeon_spl_[0]", dunjeon_spl_[0])
                                print("dunjeon_spl_[1]", dunjeon_spl_[1])

                                # if dunjeon_spl_[1] == "신전" or dunjeon_spl_[1] == "동굴":
                                if dunjeon_spl_[1] == "신전":
                                    reset_schedule_ += complete_[j] + "\n"
                                else:
                                    reset_schedule_ += "대기중\n"
                            else:
                                reset_schedule_ += "대기중\n"

                            # if complete_[6] == "지하감옥":
                            #     reset_schedule_ += complete_[j] + "\n"
                            # else:
                            #     reset_schedule_ += "대기중\n"

                print('reset_schedule_', reset_schedule_)
                # with open(file_path, "w", encoding='utf-8-sig') as file:
                #     file.write(reset_schedule_)
                with open(file_path3, "w", encoding='utf-8-sig') as file:
                    file.write(reset_schedule_)
                self.set_rand_int()

            return ishow_
        except Exception as e:
            print(e)
            return 0

    def mySchedule_start1(self):
        try:
            self.sche_add1.setText("one 실행중")
            self.sche_add2.setText("two")
            self.sche_add1.setDisabled(True)
            self.sche_add2.setDisabled(True)
            start_onecla = game_Playing_onecla(self)
            start_onecla.start()

        except Exception as e:
            print(e)
            return 0

    def mySchedule_start2(self):
        try:
            self.sche_add1.setText("one")
            self.sche_add2.setText("two 실행중")
            self.sche_add1.setDisabled(True)
            self.sche_add2.setDisabled(True)
            start_twocla = game_Playing_twocla(self)
            start_twocla.start()

        except Exception as e:
            print(e)
            return 0

    def hello2(self):
        print("hello!!!!!!!!!!")

    def mytestin_(self):
        try:
            x = Test_check(self)
            # self.mytestin.setText("GootEvening")
            # self.mytestin.setDisabled(True)
            x.start()
        except Exception as e:
            print(e)
            return 0

    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_Escape:
    #         self.close()
    #     elif e.key() == Qt.Key_F:
    #         self.showFullScreen()
    #     elif e.key() == Qt.Key_N:
    #         self.showNormal()


###########BackGround(백그라운드) 관련############################nowtest


class Test_check(QThread):

    # parent = MainWidget을 상속 받음.
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        # self.parent.hello2()

        # cla = "one"



        print("여긴 테스트 모드(ver " + version + ")")
        go_test()





        # money_ = text_check_get(233, 48, 300, 65, cla)
        # # started_ = start_.split("\n")
        # print("money?", money_)
        # if len(money_) != 0:
        #     end_ = int_put_(money_)
        #     print("now_money?", end_)
        #     # for list in end_:
        #     #     try:
        #     #         if list == '레' or list == '벨':
        #     #             dunjeon_0_check = False
        #     #             isdungeon_ing = False
        #     #             print("공허 끝?", end_)
        #     #
        #     #     except:
        #     #         pass







        print(cv2.__file__)


def pause_ing(cla):
    try:
        print("pause")
        go_ = False
        if cla == 'one':
            if int(v_.myId_1) >= 0 and int(v_.mylevel_1) > 0 and int(v_.mypower_1) > 0 and int(
                    v_.mymoney_1) > 0 and v_.one_cla_ing != 'none' and int(v_.one_cla_count) > 0:
                go_ = True
        if cla == 'two':
            if int(v_.myId_2) >= 0 and int(v_.mylevel_2) > 0 and int(v_.mypower_2) > 0 and int(
                    v_.mymoney_2) > 0 and v_.two_cla_ing != 'none' and int(v_.two_cla_count) > 0:
                go_ = True
        return go_
    except Exception as e:
        print(e)
        return 0


# class just_loginstart_one(QThread):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.parent = parent
#     def run(self):
#         try:
#             just_login('one')
#         except Exception as e:
#             print(e)
#             return 0
#
# class just_loginstart_two(QThread):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.parent = parent
#     def run(self):
#         try:
#             just_login('two')
#         except Exception as e:
#             print(e)
#             return 0

class Monitoring_one(QThread):
    # def __init__(self, parent):
    #     super().__init__(parent)
    #     self.parent = parent
    def __init__(self):
        super().__init__()

    def run(self):
        try:
            print("monitoring start")
            line_monitor("nightcrows", "one")
        except Exception as e:
            print(e)
            return 0

class Monitoring_two(QThread):
    # def __init__(self, parent):
    #     super().__init__(parent)
    #     self.parent = parent
    def __init__(self):
        super().__init__()

    def run(self):
        try:
            print("monitoring start")
            line_monitor("nightcrows", "two")
        except Exception as e:
            print(e)
            return 0


class game_Playing_onecla(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        try:
            howcla = 'onecla'

            v_.now_cla = 'one'
            v_.global_howcla = 'onecla'

            self.m_ = Monitoring_one()
            self.m_.start()


            self.x_ = game_Playing()
            self.x_.start()

            # result_ = login_start_ready(howcla)
            # if result_ == True:
            #     print("이제 시작 했다 다 죽었다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", howcla)
            #
            #     v_.now_cla = 'one'
            #     v_.global_howcla = 'onecla'
            #
            #     # self.parent.again_restart_game()
            #     self.x_ = game_Playing()
            #     self.x_.start()
            #
            #     self.y_ = BackGroundPotion()
            #     self.y_.start()
        except Exception as e:
            print(e)
            return 0


class game_Playing_twocla(QThread):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        try:
            howcla = 'twocla'

            v_.now_cla = 'two'
            v_.global_howcla = 'twocla'

            self.m_ = Monitoring_two()
            self.m_.start()

            self.x_ = game_Playing()
            self.x_.start()

            # result_ = login_start_ready(howcla)
            # if result_ == True:
            #     print("이제 시작 했다 다 죽었다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", howcla)
            #
            #     v_.now_cla = 'one'
            #     v_.global_howcla = 'onetwocla'
            #     self.x_ = game_Playing()
            #     self.x_.start()
            #
            #     self.y_ = BackGroundPotion()
            #     self.y_.start()
            # else:
            #     print("아직 2클라 덜 돌아갔다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print('return!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        except Exception as e:
            print(e)
            return 0


# 실제 게임 플레이 부분 #################################################################
################################################
################################################


class game_Playing(QThread):

    def __init__(self):
        super().__init__()
        # self.parent = parent

        self.isCheck = True

    def run(self):

        try:
            # 튜토육성, 전기육성 스케쥴 불러오기

            print("nightcrows go", v_.now_cla)

            while self.isCheck is True:

                print("나이트크로우 실행 모드(ver " + version + ")")



                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\touching.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, v_.now_cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("touching", imgs_)
                else:
                    print("touching 없")

                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\nightcrows_start_ready.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 960, 1030, v_.now_cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("매크로를 내려야 실행됨")
                    else:


                        # 대기자 명단
                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\ready_cancle.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 600, 560, 660, v_.now_cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:

                            ready_ = False
                            while ready_ is False:
                                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\ready_cancle.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 600, 560, 660, v_.now_cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    just_ready = text_check_get(390, 470, 570, 495, v_.now_cla)
                                    print("대기자?", just_ready)
                                    time.sleep(10)
                                else:
                                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\character_start\\delete_character.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(20, 990, 150, 1040, v_.now_cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        ready_ = True
                                        time.sleep(1)


                        result_schedule = myQuest_play_check(v_.now_cla, "check")
                        print("result_schedule", result_schedule)
                        character_id = result_schedule[0][1]
                        result_schedule_ = result_schedule[0][2]

                        dongool_check = "none"

                        if "_" in result_schedule_:
                            dungeon_ = result_schedule_.split("_")
                            if dungeon_[1] == "동굴":
                                dongool_check = "dongool"

                        # 동굴던전인지...
                        isjuljun = False
                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\dungeon\juljun_mode.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 120, 600, 160, v_.now_cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            isjuljun = True
                            if dongool_check == "dongool" or result_schedule_ == "격전지사냥":
                                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\dungeon\\dongool_hunting.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(450, 640, 540, 710, v_.now_cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    print("사냥중", imgs_)
                                else:
                                    print("던전 사냥중이 아니니 해제하겠다.")
                                    drag_pos(360, 550, 600, 550, v_.now_cla)

                            else:
                                print("던전이 아니니 절전모드는 해제 하겠다.")
                                drag_pos(360, 550, 600, 550, v_.now_cla)

                        # 먼저 캐릭터 변환할 것인지 물어보기
                        if result_schedule_ == "캐릭터바꾸기":
                            character_change(v_.now_cla, character_id)
                            myQuest_play_add(v_.now_cla, result_schedule_)
                        else:
                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\character_start\\delete_character.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(20, 990, 150, 1040, v_.now_cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                character_change(v_.now_cla, character_id)

                            else:

                                # 현재 진행중인 스케쥴 내 캐릭터 id와 기존 캐릭터 id 비교해서 다르면 캐릭터 바꾸기
                                dir_path = "C:\\my_games\\nightcrows"
                                if v_.now_cla == 'one':
                                    file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
                                if v_.now_cla == 'two':
                                    file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"

                                if os.path.isfile(file_path) == True:

                                    with open(file_path, "r", encoding='utf-8-sig') as file:
                                        read_id = file.read()

                                    if str(character_id) != str(read_id):
                                        character_change(v_.now_cla, character_id)
                                else:
                                    character_change(v_.now_cla, character_id)


                            # 우측 상단 퀘스트 보이게 하기
                            quest_look(v_.now_cla)

                            # 먼저 가방 꽉 찼는지 확인부터...
                            bag_full_check(v_.now_cla)

                            # 새로운 아이템 받을 것 체크하기
                            get_item_checking(v_.now_cla)

                            # 길드지령 있을 경우 선택하기
                            # guild_jilyung(v_.now_cla)

                            # 최초1회만...
                            if result_schedule_ != "각종템받기" and result_schedule_ != "튜토육성" and isjuljun != True and dongool_check != "dongool":
                                if v_.just_one == False:

                                    v_.just_one = True

                                    # print("최초 1회 : 마을일 경우 물약 ㄱㄱ", v_.just_one)
                                    # v_.just_one = True
                                    print("마을일경우 물약 등 체크하기")
                                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\potion\\janhwa_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 90, 220, 350, v_.now_cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        print("마을이면 물약 ㄱㄱ", imgs_)
                                        maul_potion(v_.now_cla)
                                    else:
                                        result_maul = maul_check(v_.now_cla)
                                        if result_maul == True:
                                            click_pos_2(230, 90, v_.now_cla)
                                            maul_potion(v_.now_cla)
                                            time.sleep(1)


                            if v_.force_sub_quest == True and result_schedule_ != "튜토육성":
                                # 죽었을때 돈 50만 골드 이하일때 강제노역 보내기

                                jadong_play(v_.now_cla, v_.onForceGoldSpot_go)
                                # 자체에 스케쥴 완료 없음 돈 벌어야 빠져나옴
                                my_gold_check(v_.now_cla)

                            else:

                                v_.now_ing_schedule = result_schedule_




                                if "_" in result_schedule_:

                                    dungeon_ = result_schedule_.split("_")

                                    if dungeon_[0] == "던전":
                                        result = dungeon_play(v_.now_cla, result_schedule_)
                                        if result == True:
                                            myQuest_play_add(v_.now_cla, result_schedule_)

                                    if dungeon_[0] == "사냥":
                                        jadong_play(v_.now_cla, result_schedule_)

                                    if dungeon_[0] == "일일퀘스트":
                                        select_daily_quest_grow(v_.now_cla, character_id, dungeon_[0])
                                        # 자체에 스케쥴 완료 있음
                                else:
                                    if result_schedule_ == "튜토육성":
                                        tuto_grow(v_.now_cla)
                                        # tuto_grow에 스케쥴 완료 있음
                                    if result_schedule_ == "각종템받기":

                                        # 아래는 특별 이벤트 진행하기
                                        daily_one(v_.now_cla)

                                        get_items(v_.now_cla)
                                        # 자체에 스케쥴 완료 있음
                                        if v_.just_one == False:
                                            v_.just_one = True
                                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\potion\\janhwa_1.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(0, 90, 220, 350, v_.now_cla, img, 0.9)
                                            if imgs_ is not None and imgs_ != False:
                                                print("마을이면 물약 ㄱㄱ", imgs_)
                                                maul_potion(v_.now_cla)
                                    if result_schedule_ == "메인퀘스트":
                                        main_quest_grow(v_.now_cla)
                                        # 자체에 스케쥴 완료 있음
                                    if result_schedule_ == "서브퀘스트":
                                        sub_quest_grow(v_.now_cla)
                                        # 자체에 스케쥴 완료 있음
                                    if result_schedule_ == "일일퀘스트":

                                        daily_step = '1'
                                        select_daily_quest_grow(v_.now_cla, character_id, daily_step)
                                        # 자체에 스케쥴 완료 있음
                                    if result_schedule_ == "격전지사냥":
                                        gyucjunji_play(v_.now_cla)
                                        # 자체에 스케쥴 완료 있음



                time.sleep(3)
        except Exception as e:
            print(e)
            return 0


####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    # sys.exit(1)


# if __name__ == '__main__':
#     try:
#         app = QApplication(sys.argv)
#         ex = MyApp()
#
#         # Back up the reference to the exceptionhook
#         sys._excepthook = sys.excepthook
#
#         # Set the exception hook to our wrapping function
#         sys.excepthook = my_exception_hook
#
#         sys.exit(app.exec_())
#     except Exception as e:
#         print(e)
#         print("프로그램 꺼지기전 정지")
#         os.system("pause")
