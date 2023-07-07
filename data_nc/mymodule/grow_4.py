import sys
import time

import pyautogui

sys.path.append('C:/my_games/nightcrows/data_nc/mymodule')

import variable as v_

fly_ = 0
daily_quest = False

def select_daily_quest_grow(cla, character_id, step):
    try:
        global camera_, media_, talchool_, prison_, boonji_, force_quest, fly_, daily_quest

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from massenger import line_to_me
        from schedule import myQuest_play_add
        from potion import potion_check, maul_potion
        from action import go_quest_ing_, go_auto_ing_, clean_screen, dead_die, in_maul_check

        import pyautogui
        import random
        import numpy as np
        import cv2

        print("nightcrows daily quest")
        print("v_.sub_quest_count(10이면 일일퀘스트 끝) =>", v_.sub_quest_count)

        result_dead = dead_die(cla)
        print("죽었당!!!!!!!!!!!!!!!!!!!!?????????????", result_dead)
        if result_dead == True:
            myQuest_play_add(cla, "일일퀘스트")

        # result_check = talgut_board_check
        # if result_check == True:
        # dfasdfasfasf
        if daily_quest == False:

            quest_get(cla, character_id, step)
            clean_screen(cla)

        result_potion = potion_check(cla)
        print("내 물약 갯수? ", result_potion)

        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\clean_screen\\gabang_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(820, 80, 910, 120, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(935, 100, cla)

        result_ = go_quest_ing_(cla)
        if result_ == False:

            result_auto = go_auto_ing_(cla)
            if result_auto == True:
                quest_check(cla)
            #
            #
            # result_maul = in_maul_check(cla)
            # if result_maul == True:
            #     maul_potion(cla)

            # skip
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_1\\skip_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 45, 960, 130, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("skip_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_1\\skip_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 45, 960, 130, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("skip_3", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

            # skip
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_1\\skip_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(580, 880, 680, 920, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("skip_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)




            # 아이템 장착
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_1\\fit_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(660, 760, 750, 830, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("fit_1", imgs_)
                click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)
                time.sleep(0.5)

            # 확인 버튼
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\clean_screen\\confirm_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(490, 620, 620, 660, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("confirm_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)




        else:
            print("진행중")
            quest_check(cla)

    except Exception as e:
        print(e)

def quest_get(cla, character_id, step):
    try:
        global daily_quest
        import numpy as np
        import cv2
        from action import menu_open, clean_screen
        from function import click_pos_2, click_pos_reg, imgs_set_, text_check_get, int_put_
        from schedule import myQuest_play_add
        from jadong_crow import go_to_spot
        print("일일퀘스트 받기")
        daily_quest = True

        # clear_sub_quest = False


        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        if cla == 'three':
            plus = 960 + 960

        step = int(step)


        # 요구레벨 불러오기
        dir_path = "C:\\my_games\\nightcrows\\mysettings\\my_level"

        if character_id == "1":
            file_path = dir_path + "\\one_character.txt"
        if character_id == "2":
            file_path = dir_path + "\\two_character.txt"


        with open(file_path, "r", encoding='utf-8-sig') as file:
            read_level = file.read()

        in_quest_1 = False
        in_quest_1_count = 0
        while in_quest_1 is False:
            in_quest_1_count += 1
            if in_quest_1_count > 10:
                in_quest_1 = True
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_3\\quest_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("quest_", imgs_)

                daily_click = False
                daily_click_count = 0
                while daily_click is False:
                    daily_click_count += 1
                    if daily_click_count > 10:
                        daily_click = True
                        in_quest_1 = True
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\daily_check_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(160, 990, 220, 1015, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("daily_check_1", imgs_)


                        if step == 1:
                            # 바스티움
                            click_pos_2(60, 185, cla)
                            click_pos_2(60, 185, cla)
                            time.sleep(1)
                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\daily_check_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            for i in pyautogui.locateAllOnScreen(img, region=(160 + plus, 230, 60, 750), confidence=0.8):
                                last_x = i.left
                                if cla == "two":
                                    last_x = last_x - 960
                                if cla == "three":
                                    last_x = last_x - 960 - 960
                                last_y = i.top

                                print("check point!!!!!!!!!!!!!", last_x, last_y)



                                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\daily_check_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(last_x - 7, last_y - 7, last_x + 43, last_y + 18, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    level_check = text_check_get(last_x - 7, last_y - 7, last_x + 43, last_y + 18, cla)
                                    result_lev = int_put_(level_check)
                                    num_bool = result_lev.isdigit()
                                    if num_bool == True:
                                        if int(result_lev) < int(read_level) and int(result_lev) != 4 and int(result_lev) != 5 and int(result_lev) != 6 and int(result_lev) != 7:
                                            print("result_lev", result_lev)

                                            click_pos_2(last_x + 200, last_y, cla)
                                            time.sleep(0.1)

                                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\soolock.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(640, 970, 770, 1020, cla, img, 0.83)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            print("result_lev", result_lev)
                                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\give_up_2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(850, 120, 950, 200, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.3)
                                                for z in range(3):
                                                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\y_1.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                                        break
                                                    time.sleep(0.3)
                                    else:
                                        print("요구레벨이 숫자 아니라고 읽음", result_lev)

                        if step == 2:
                            # 첼라노
                            click_pos_2(60, 220, cla)
                            click_pos_2(60, 220, cla)
                            time.sleep(1)
                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\daily_check_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            for i in pyautogui.locateAllOnScreen(img, region=(160 + plus, 230, 60, 750), confidence=0.8):
                                last_x = i.left
                                if cla == "two":
                                    last_x = last_x - 960
                                if cla == "three":
                                    last_x = last_x - 960 - 960
                                last_y = i.top

                                print("check point!!!!!!!!!!!!!", last_x, last_y)

                                # click_pos_2(last_x + 200, last_y, cla)

                                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\daily_check_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(last_x - 7, last_y - 7, last_x + 43, last_y + 18, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    level_check = text_check_get(last_x - 7, last_y - 7, last_x + 43, last_y + 18, cla)
                                    result_lev = int_put_(level_check)
                                    num_bool = result_lev.isdigit()
                                    if num_bool == True:
                                        if int(result_lev) < int(read_level) and int(result_lev) != 4 and int(result_lev) != 5 and int(
                                                result_lev) != 6 and int(result_lev) != 7:

                                            click_pos_2(last_x + 200, last_y, cla)
                                            time.sleep(0.1)

                                            print("result_lev", result_lev)
                                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\soolock.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(640, 970, 770, 1020, cla, img, 0.83)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            print("result_lev", result_lev)
                                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\give_up_2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(850, 120, 950, 200, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.3)
                                                for z in range(3):
                                                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\y_1.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                                        break
                                                    time.sleep(0.3)
                                    else:
                                        print("요구레벨이 숫자 아니라고 읽음", result_lev)
                            # time.sleep(1)
                            # full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\give_up_1.PNG"
                            # img_array = np.fromfile(full_path, np.uint8)
                            # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            # for i in pyautogui.locateAllOnScreen(img, region=(560 + plus, 150, 630, 330), confidence=0.8):
                            #     last_x = i.left
                            #     if cla == "two":
                            #         last_x = last_x - 960
                            #     last_y = i.top
                            #
                            #     click_pos_reg(last_x, last_y, cla)
                            #
                            #     full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\give_up_2.PNG"
                            #     img_array = np.fromfile(full_path, np.uint8)
                            #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            #     imgs_ = imgs_set_(850, 120, 950, 200, cla, img, 0.8)
                            #     if imgs_ is not None and imgs_ != False:
                            #         click_pos_reg(imgs_.x, imgs_.y, cla)
                            #         time.sleep(0.3)
                            #         for z in range(3):
                            #             full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\y_1.PNG"
                            #             img_array = np.fromfile(full_path, np.uint8)
                            #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            #             imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                            #             if imgs_ is not None and imgs_ != False:
                            #                 click_pos_reg(imgs_.x, imgs_.y, cla)
                            #                 break
                            #             time.sleep(0.3)
                        if step == 3:
                            # 아빌리우스
                            click_pos_2(60, 260, cla)
                            click_pos_2(60, 260, cla)
                            time.sleep(1)
                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\daily_check_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            for i in pyautogui.locateAllOnScreen(img, region=(160 + plus, 230, 60, 750), confidence=0.8):
                                last_x = i.left
                                if cla == "two":
                                    last_x = last_x - 960
                                if cla == "three":
                                    last_x = last_x - 960 - 960
                                last_y = i.top

                                print("check point!!!!!!!!!!!!!", last_x, last_y)

                                # click_pos_2(last_x + 200, last_y, cla)

                                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\daily_check_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(last_x - 7, last_y - 7, last_x + 43, last_y + 18, cla, img, 0.83)
                                if imgs_ is not None and imgs_ != False:
                                    level_check = text_check_get(last_x - 7, last_y - 7, last_x + 43, last_y + 18, cla)
                                    result_lev = int_put_(level_check)
                                    num_bool = result_lev.isdigit()
                                    if num_bool == True:
                                        if int(result_lev) < int(read_level) and int(result_lev) != 4 and int(
                                                result_lev) != 5 and int(
                                                result_lev) != 6 and int(result_lev) != 7:

                                            click_pos_2(last_x + 200, last_y, cla)
                                            time.sleep(0.1)

                                            print("result_lev", result_lev)
                                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\soolock.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(640, 970, 770, 1020, cla, img, 0.83)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            print("result_lev", result_lev)
                                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\give_up_2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(850, 120, 950, 200, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.3)
                                                for z in range(3):
                                                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\y_1.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                                        break
                                                    time.sleep(0.3)
                                    else:
                                        print("요구레벨이 숫자 아니라고 읽음", result_lev)

                        time.sleep(1)
                        # 일일퀘스트 받기 끝
                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\y_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        in_quest_2 = False
                        in_quest_2_count = 0
                        while in_quest_2 is False:
                            in_quest_2_count += 1
                            if in_quest_2_count > 10:
                                in_quest_2 = True
                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_3\\quest_.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.83)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(930, 60, cla)
                            else:
                                in_quest_1 = True
                                in_quest_2 = True
                    else:
                        click_pos_2(350, 110, cla)
                    time.sleep(0.5)

            else:
                menu_open(cla)
                click_pos_2(745, 195, cla)

            time.sleep(0.3)

        # if clear_sub_quest == True:
        #     myQuest_play_add(cla, "서브퀘스트")
        #     clean_screen(cla)
        # else:
        #     go_to_spot(cla, "sub")
        #
        # full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\clean_screen\\quest_title.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(80, 40, 160, 80, cla, img, 0.83)
        # if imgs_ is not None and imgs_ != False:
        #     print("quest_title", imgs_)
        #     click_pos_2(930, 60, cla)

    except Exception as e:
        print(e)

def quest_check(cla):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import go_quest_ing_
        from get_item import guild_jilyung
        import numpy as np
        import cv2

        # 길드 지령..
        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            jilyung_is_ = False
            jilyung_is_count = 0
            while jilyung_is_ is False:
                jilyung_is_count += 1
                if jilyung_is_count > 5:
                    jilyung_is_ = True

                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\guild\\guild_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 30, 100, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    guild_jilyung(cla, "jadong")
                    jilyung_is_ = True
                else:
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\dungeon\\chogwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(390, 70, 470, 120, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("초과가 보여")
                            jilyung_is_ = True
                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\quest_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 170, 720, 220, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                v_.sub_quest_count = 0
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                time.sleep(0.4)

        # # 퀘스트 수락
        # full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_1\\quest_soolock_2.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(800, 90, 960, 900, cla, img, 0.83)
        # if imgs_ is not None and imgs_ != False:
        #     print("quest_soolock_2", imgs_)
        #     click_pos_reg(imgs_.x, imgs_.y, cla)


        # 퀘스트 완료
        is_daily = False
        is_daily_count = 0
        while is_daily is False:
            is_daily_count += 1
            if is_daily_count > 5:
                is_daily = True
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_1\\quest_complete_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 90, 960, 900, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("quest_complete_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            else:
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_1\\quest_complete_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 90, 960, 900, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    print("quest_complete_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    is_daily = True
                    result_ = go_quest_ing_(cla)
                    if result_ == False:
                        talgut_board_(cla)

                #
                # is_daily = True
                # result_ = go_quest_ing_(cla)
                # if result_ == False:
                #     talgut_board_(cla)



        # 붕붕 날아다니자
        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\flying_.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(820, 880, 910, 970, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_3\\gyunway_bawigil.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 75, 160, 110, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                time.sleep(0.1)
                pyautogui.keyDown('a')
                time.sleep(0.1)
                pyautogui.keyUp('a')
                time.sleep(0.1)
                print("pyautogui.press('a')")

            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\fly_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 970, 960, 1030, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                print("플라잉 부스터!!!")




    except Exception as e:
        print(e)




def talgut_board_(cla):
    try:
        from schedule import myQuest_play_add
        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import menu_open, clean_screen, go_quest_ing_, go_auto_ing_
        from jadong_crow import go_to_spot
        import numpy as np
        import cv2
        import pyautogui

        result = talgut_board_check(cla)
        if result == True:
            v_.sub_quest_count = 0

            # 확인 버튼
            time.sleep(1)
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\clean_screen\\confirm_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(490, 620, 620, 660, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("confirm_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            time.sleep(0.5)

            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_1\\no_talgut_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(365, 85, 450, 115, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("no_talgut_1", imgs_)
                click_pos_2(880, 110, cla)

            #비행장?
            go_to_spot(cla, "sub")
        else:
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\quest_check.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(895, 95, 925, 120, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("quest_check", imgs_)
                click_pos_2(700, 110, cla)
            else:
                click_pos_2(930, 110, cla)
                time.sleep(0.2)
                click_pos_2(700, 110, cla)
            v_.sub_quest_count += 1
            if v_.sub_quest_count > 10:
                v_.sub_quest_count = 0
                myQuest_play_add(cla, "일일퀘스트")

    except Exception as e:
        print(e)

def talgut_board_check(cla):
    try:
        from schedule import myQuest_play_add
        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from action import menu_open, clean_screen, go_quest_ing_, go_auto_ing_
        from get_item import guild_jilyung
        import numpy as np
        import cv2
        import pyautogui

        go_ = False

        # 가방 열려있는지 체크 후 닫기
        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\bag_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
        if imgs_ is not None and imgs_ != False:
            print("가방이 열려 있다. 닫아버리자. 퀘스트 있는지 체크하기 위해...", imgs_)
            click_pos_2(935, 100, cla)

        # 메뉴 열려있는지 체크 후 닫기
        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\pvp_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 275, 960, 365, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("메뉴가 열려 있다. 닫아버리자. 퀘스트 있는지 체크하기 위해...", imgs_)
            click_pos_2(930, 60, cla)

        # 길드 지령..
        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            jilyung_is_ = False
            jilyung_is_count = 0
            while jilyung_is_ is False:
                jilyung_is_count += 1
                if jilyung_is_count > 5:
                    jilyung_is_ = True

                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\guild\\guild_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 30, 100, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    guild_jilyung(cla, "jadong")
                    jilyung_is_ = True
                else:
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\dungeon\\chogwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(390, 70, 470, 120, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("초과가 보여")
                            jilyung_is_ = True
                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\quest_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 170, 720, 220, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                v_.sub_quest_count = 0
                                go_ = True
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.4)

        # 탈것
        if go_ == False:
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\quest_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 130, 720, 220, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                go_ = True
                v_.sub_quest_count = 0
                click_pos_reg(imgs_.x, imgs_.y, cla)

        sojin_ = False
        jilyung = False
        for i in range(10):
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\sub_sojin_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 70, 550, 120, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sub_sojin_1", imgs_)
                sojin_ = True
                break
            else:
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\sub_sojin_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 70, 550, 120, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("sub_sojin_1", imgs_)
                    sojin_ = True
                    break
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\guild_jilyung_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 70, 550, 120, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("guild_jilyung_1", imgs_)
                jilyung = True
                break
            else:
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\guild_jilyung_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 70, 550, 120, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("guild_jilyung_2", imgs_)
                    jilyung = True
                    break
        if jilyung == True:
            print("지령 관련 퀘스트 여긴 일일퀘스트")
            # 길드 지령..
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                jilyung_is_ = False
                jilyung_is_count = 0
                while jilyung_is_ is False:
                    jilyung_is_count += 1
                    if jilyung_is_count > 5:
                        jilyung_is_ = True

                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\guild\\guild_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 30, 100, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        guild_jilyung(cla, "jadong")
                        jilyung_is_ = True
                    else:
                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\guild\\guild_jilyung.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(660, 90, 730, 300, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\dungeon\\chogwa.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(390, 70, 470, 120, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("초과가 보여")
                                jilyung_is_ = True
                                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\quest_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(680, 170, 720, 220, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    v_.sub_quest_count = 0
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.4)
            # myQuest_play_add(cla, "일일퀘스트")
        if sojin_ == True:
            in_quest_title = False
            in_quest_title_count = 0
            while in_quest_title is False:
                in_quest_title_count += 1
                if in_quest_title_count > 5:
                    in_quest_title = True
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\quest_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\in_quest_dungeon.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 130, 160, 900, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        give_up_ready = False
                        give_up_ready_count = 0
                        while give_up_ready is False:
                            give_up_ready_count += 1
                            if give_up_ready_count > 10:
                                give_up_ready = True

                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\in_quest_dungeon.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 130, 160, 900, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("in_quest_dungeon", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y + 30, cla)

                                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\give_up_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(560, 150, 630, 330, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\give_up_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(850, 120, 950, 200, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    give_up_ready = True
                                    in_quest_title = True
                            time.sleep(1)
                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\y_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 580, 600, 630, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        click_pos_2(345, 105, cla)
                else:
                    menu_open(cla)
                    click_pos_2(745, 190, cla)
            time.sleep(0.5)
            clean_screen(cla)
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\quest\\quest_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(930, 60, cla)
        if sojin_ == True:
            go_ = False

        return go_
    except Exception as e:
        print(e)


