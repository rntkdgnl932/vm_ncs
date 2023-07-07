import time

import requests
import json
# import os
import sys
sys.path.append('C:/my_games/nightcrows/data_nc/mymodule')

import variable as v_

def jadong_play(cla, result_schedule_):
    try:
        import cv2
        import os
        import numpy as np
        from function import text_check_get, int_put_, imgs_set_, click_pos_reg
        from action import out_check, clean_screen, in_maul_check
        from massenger import line_to_me
        from potion import maul_potion

        dungeon_ = result_schedule_.split("_")

        print("자동사냥냥터 : ", dungeon_[2])

        complete_ = False

        result_out = out_check(cla)
        if result_out == False:
            clean_screen(cla)

        if "_" in result_schedule_:
            dungeon_ = result_schedule_.split("_")

        dir_path = "C:\\my_games\\nightcrows\\data_nc"

        if dungeon_[1] == "아빌리우스":
            file_path = dir_path + "\\jadong\\abilius.txt"
        if dungeon_[1] == "바스티움":
            file_path = dir_path + "\\jadong\\bastium.txt"
        if dungeon_[1] == "첼라노":
            file_path = dir_path + "\\jadong\\chalano.txt"
        file_path2 = dir_path + "\\jadong\\jadong.txt"

        if os.path.isfile(file_path) == True:
            with open(file_path, "r", encoding='utf-8-sig') as file:
                read_ready = file.read()
                read_ready = read_ready.split(":")
                read_ = read_ready[1].split("/")
                print("read_", read_)

                # for i in range(len(read_)):
                #     if read_[i] == dungeon_[2]:
                #         hunter_spot =
        else:
            print("자료가 없다")
            line_to_me(cla, "나크 자동사냥 자료 없다.")


        if os.path.isfile(file_path2) == True:
            with open(file_path2, "r", encoding='utf-8-sig') as file:
                read_line = file.read().splitlines()
                for i in range(len(read_line)):
                    result_ = read_line[i].split("/")
                    if result_[0] == dungeon_[2]:
                        hunter_spot = result_[2]


        else:
            print("자료가 없다")
            line_to_me(cla, "나크 자동사냥 자료 없다.2")


        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\" + read_ready[0] + "\\" + hunter_spot + ".PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(40, 80, 160, 110, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("도착한 상태")
            now_playing(cla)
        else:
            print("사냥터 진입하러 가자")
            # 자동사냥 진입
            clean_screen(cla)
            # result_maul = in_maul_check(cla)
            # if result_maul == True:
            #     maul_potion(cla)
            in_world(cla)
            in_spot(cla, result_schedule_)
            go_to_spot(cla, "jadong")

        return complete_
    except Exception as e:
        print(e)

def in_world(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, click_pos_2, imgs_set_

        in_worldmap = False
        in_worldmap_count = 0
        while in_worldmap is False:
            in_worldmap_count += 1
            if in_worldmap_count > 7:
                in_worldmap = True
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(450, 990, 510, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("worldmap", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                in_worldmap = True

                last_in = False
                last_in_count = 0
                while last_in is False:
                    last_in_count += 1
                    if last_in_count > 20:
                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 990, 510, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("worldmap~!", imgs_)
                            last_in_count = 0
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            last_in = True
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(450, 990, 510, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("진입 대기중")

                    else:
                        last_in = True
                    time.sleep(0.1)

            else:
                # dead_die_before 끄기
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\dead_die\\exp_.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 80, 150, 115, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\clean_screen\\exit_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 200, 600, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("exp_ exit_22", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\dead_die\\jangbi_.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 80, 150, 115, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\clean_screen\\exit_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 200, 600, cla, img, 0.83)
                    if imgs_ is not None and imgs_ != False:
                        print("jangbi_ exit_22", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)

                # maul_ = False
                # full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_ready_3.PNG"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                # if imgs_ is not None and imgs_ != False:
                #     print("world_ready_3", imgs_)
                #     maul_ = True
                #
                # full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_ready_4.PNG"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                # if imgs_ is not None and imgs_ != False:
                #     print("world_ready_4", imgs_)
                #     maul_ = True

                maul_ = False

                maul_list = ["maul_", "maul_a", "maul_b", "maul_c"]
                for i in range(len(maul_list)):
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\maul\\" + maul_list[i] + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 70, 160, 110, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print(maul_list[i], imgs_)
                        maul_ = True
                if maul_ == False:
                    # click_pos_2(230, 90, cla)
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\maul\\jabhwa_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("여긴 마을!!!!!!!!!!!!!")
                        click_pos_2(230, 90, cla)

                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\maul_eye_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 55, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("눈알 있다.", imgs_)
                else:
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\close_eye_check.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 0, 55, 80, cla, img, 0.84)
                    if imgs_ is not None and imgs_ != False:
                        print("눈알 없다.", imgs_)
                        click_pos_2(30, 55, cla)

                world_check = False
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_ready_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 40, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("world_ready_1", imgs_)
                    world_check = True
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_ready_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 70, 40, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("world_ready_2", imgs_)
                    world_check = True
                world_check_count = 0
                while world_check is True:
                    world_check_count += 1
                    if world_check_count > 10:
                        world_check = False
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(450, 990, 510, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("월드맵에 들어옴", imgs_)
                        world_check = False
                    else:
                        click_pos_2(110, 160, cla)
                    time.sleep(0.3)
            time.sleep(0.3)


    except Exception as e:
        print(e)


def in_spot(cla, result_schedule_):
    try:
        import cv2
        import numpy as np
        import os.path
        from function import text_check_get, int_put_, click_pos_reg, click_pos_2, imgs_set_, drag_pos
        from massenger import line_to_me

        in_map = False
        in_map_count = 0
        while in_map is False:
            in_map_count += 1
            if in_map_count > 20:
                in_map = True
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\sin_triesde.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sin_triesde", imgs_)
                click_pos_reg(imgs_.x, imgs_.y - 50, cla)
                in_map = True
                time.sleep(1)
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\bastium.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("bastium", imgs_)
                in_map = True
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\abilius.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                in_map = True
                print("abilius", imgs_)
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\chalano.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                in_map = True
                print("chalano", imgs_)
            if in_map == True:
                # 사냥터에 따라 지도 클릭 달라짐

                if "_" in result_schedule_:

                    dungeon_ = result_schedule_.split("_")


                dir_path = "C:\\my_games\\nightcrows\\data_nc"

                if dungeon_[1] == "아빌리우스":
                    file_path = dir_path + "\\jadong\\abilius.txt"
                if dungeon_[1] == "바스티움":
                    file_path = dir_path + "\\jadong\\bastium.txt"
                if dungeon_[1] == "첼라노":
                    file_path = dir_path + "\\jadong\\chalano.txt"
                file_path2 = dir_path + "\\jadong\\jadong.txt"



                if os.path.isfile(file_path) == True:
                    with open(file_path, "r", encoding='utf-8-sig') as file:
                        read_ready = file.read()
                        read_ready = read_ready.split(":")
                        read_ = read_ready[1].split("/")
                        print("read_", read_)

                        # for i in range(len(read_)):
                        #     if read_[i] == dungeon_[2]:
                        #         hunter_spot
                else:
                    print("자료가 없다")
                    line_to_me(cla, "나크 자동사냥 자료 없다.")
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\" + read_ready[0] + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y - 50, cla)
                    in_worldmap = False
                    in_worldmap_count = 0
                    while in_worldmap is False:
                        in_worldmap_count += 1
                        if in_worldmap_count > 20:
                            in_worldmap = True
                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 990, 510, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("worldmap", imgs_)
                            if os.path.isfile(file_path2) == True:
                                with open(file_path2, "r", encoding='utf-8-sig') as file:
                                    read_line = file.read().splitlines()
                                    for i in range(len(read_line)):
                                        result_ = read_line[i].split("/")
                                        if result_[0] == dungeon_[2]:
                                            in_worldmap = True
                                            print("완벽", result_[1])
                                            in_spot_start = False
                                            in_spot_start_count = 0
                                            while in_spot_start is False:
                                                in_spot_start_count += 1
                                                if in_spot_start_count > 7:
                                                    in_spot_start = True

                                                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\confirm_1.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:

                                                    last_move = False
                                                    last_move_count = 0
                                                    while last_move is False:
                                                        last_move_count += 1
                                                        if last_move_count > 10:
                                                            last_move = True
                                                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\confirm_1.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                                                        if imgs_ is not None and imgs_ != False:
                                                            click_pos_reg(imgs_.x, imgs_.y, cla)

                                                            #돈 없다고 할때....
                                                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\dead_die\\not_enough_gold.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                                            if imgs_ is not None and imgs_ != False:
                                                                print("not_enough_gold~!!!!")
                                                                last_move = True
                                                                in_spot_start = True
                                                                # in_spot_to_walking_ready(cla)
                                                            else:
                                                                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\dead_die\\not_enough_gold.PNG"
                                                                img_array = np.fromfile(full_path, np.uint8)
                                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                                imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                                                if imgs_ is not None and imgs_ != False:
                                                                    print("not_enough_gold2~!!!!")
                                                                    last_move = True
                                                                    in_spot_start = True
                                                                    # in_spot_to_walking_ready(cla)
                                                            if last_move == True:
                                                                in_spot_to_walking_ready(cla)

                                                        else:
                                                            last_move = True
                                                            in_spot_start = True
                                                else:
                                                    if result_[1] == "like":
                                                        click_pos_2(880, 130, cla)
                                                        time.sleep(0.5)
                                                        click_pos_2(800, int(result_[2]), cla)
                                                    elif result_[1] == "drag":
                                                        drag_pos(800, 900, 800, 200, cla)
                                                        time.sleep(0.5)
                                                        click_pos_2(800, int(result_[2]), cla)
                                                    else:
                                                        drag_pos(800, 200, 800, 900, cla)
                                                        time.sleep(0.5)
                                                        click_pos_2(800, int(result_[1]), cla)
                                                time.sleep(0.2)
                            else:
                                print("자료가 없다..")
                                line_to_me(cla, "나크 자동사냥 자료 없다.")

                        else:

                            print("다시 월드맵 진입중")
                        time.sleep(0.3)



    except Exception as e:
        print(e)


def in_spot_to_walking_ready(cla):
    try:
        import cv2
        import numpy as np
        import os.path
        from function import text_check_get, int_put_, click_pos_reg, click_pos_2, imgs_set_, drag_pos
        from massenger import line_to_me
        from action import out_check, clean_screen

        out_ = False
        while out_ is False:
            result_out = out_check(cla)
            if result_out == True:
                out_ = True
            else:
                click_pos_2(400, 610, cla)

                clean_screen(cla)

        if out_ == True:

            # 우선 월드 지도 펼치기
            in_worldmap = False
            in_worldmap_count = 0
            while in_worldmap is False:
                in_worldmap_count += 1
                if in_worldmap_count > 20:
                    in_worldmap = True
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(450, 990, 510, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("worldmap", imgs_)
                    in_worldmap = True

                else:
                    maul_ = False
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_ready_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("world_ready_3", imgs_)
                        maul_ = True

                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_ready_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 70, 220, 330, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("world_ready_4", imgs_)
                        maul_ = True

                    if maul_ == True:
                        click_pos_2(230, 90, cla)

                    else:
                        world_check = False
                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_ready_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 70, 40, 110, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("world_ready_1", imgs_)
                            world_check = True
                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\world_ready_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 70, 40, 110, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("world_ready_2", imgs_)
                            world_check = True
                        if world_check == True:
                            click_pos_2(110, 160, cla)
            #미리 정해진 뛸곳 가기
            dir_path = "C:\\my_games\\nightcrows\\data_nc"
            #지도 캡쳐 후 장소 정하기
            file_path2 = dir_path + "\\jadong\\jadong.txt"
            # 아빌리우스 => 몬테노폐허
            # 바스티움 => 콜리아기슭
            # 첼라노 => 알레인고지대
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\a_list.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 70, 870, 120, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("a_list", imgs_)
                gold_spot = "몬테노폐허"
                spot_global = "사냥_아빌리우스_" + gold_spot
                v_.onForceGoldSpot_go = spot_global
            else:
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\b_list.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(770, 70, 870, 120, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("a_list", imgs_)
                    gold_spot = "콜리아기슭"
                    spot_global = "사냥_바스티움_" + gold_spot
                    v_.onForceGoldSpot_go = spot_global
                else:
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\c_list.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(770, 70, 870, 120, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("a_list", imgs_)
                        gold_spot = "알레인고지대"
                        spot_global = "사냥_첼라노_" + gold_spot
                        v_.onForceGoldSpot_go = spot_global

            if os.path.isfile(file_path2) == True:
                with open(file_path2, "r", encoding='utf-8-sig') as file:
                    read_line = file.read().splitlines()
                    for i in range(len(read_line)):
                        result_ = read_line[i].split("/")
                        if result_[0] == gold_spot:
                            print("완벽", result_[1])
                            in_spot_start = False
                            in_spot_start_count = 0
                            while in_spot_start is False:
                                in_spot_start_count += 1
                                if in_spot_start_count > 20:
                                    in_spot_start = True
                                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\confirm_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:

                                    last_move = False
                                    last_move_count = 0
                                    while last_move is False:
                                        last_move_count += 1
                                        if last_move_count > 10:
                                            last_move = True
                                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\confirm_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(480, 580, 630, 630, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)

                                            # 돈 없다고 할때....
                                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\dead_die\\not_enough_gold.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("not_enough_gold")
                                                last_move = True
                                                in_spot_start = True
                                            else:
                                                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\dead_die\\not_enough_gold.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(400, 60, 600, 120, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("not_enough_gold2")
                                                    last_move = True
                                                    in_spot_start = True
                                            if last_move == True:

                                                dir_path = "C:\\my_games\\nightcrows"
                                                file_path = dir_path + "\\mysettings\\gold_force\\limit_gold_spot.txt"

                                                with open(file_path, "w", encoding='utf-8-sig') as file:
                                                    file.write(gold_spot)


                                                in_spot_to_walking(cla)


                                        else:
                                            last_move = True
                                            in_spot_start = True
                                else:
                                    if result_[1] == "like":
                                        click_pos_2(880, 130, cla)
                                        time.sleep(0.5)
                                        click_pos_2(800, int(result_[2]), cla)
                                    elif result_[1] == "drag":
                                        drag_pos(800, 900, 800, 200, cla)
                                        time.sleep(0.5)
                                        click_pos_2(800, int(result_[2]), cla)
                                    else:
                                        drag_pos(800, 200, 800, 900, cla)
                                        time.sleep(0.5)
                                        click_pos_2(800, int(result_[1]), cla)
                                time.sleep(0.2)
            else:
                print("자료가 없다..")
                line_to_me(cla, "나크 자동사냥 자료 없다.")





    except Exception as e:
        print(e)



def in_spot_to_walking(cla):
    try:
        import cv2
        import numpy as np
        import os.path
        from function import text_check_get, int_put_, click_pos_reg, click_pos_2, imgs_set_, drag_pos
        from massenger import line_to_me
        from action import out_check, clean_screen
        print("뛰어가자!!!")
        # 뛰어가기
        spot_walking = False
        spot_walking_count = 0
        while spot_walking is False:
            spot_walking_count += 1
            if spot_walking_count > 15:
                spot_walking = True
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\in_spot_walking_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 500, 600, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("in_spot_walking~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\in_spot_walking_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 60, 600, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("in_spot_walking...")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    click_pos_2(930, 60, cla)
                    time.sleep(2)

                    last_move = False
                    last_move_count = 0
                    while last_move is False:
                        if last_move_count > 10:
                            last_move = True
                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            last_move_count = 0
                            print("in_spot_walking_2 보여", last_move_count)
                        else:
                            last_move_count += 1
                            print("in_spot_walking_2 안 보여", last_move_count)
                        time.sleep(0.5)

                        if last_move == True:
                            spot_walking = True
                            print("도착!!")
                            click_pos_2(930, 850, cla)

                    # full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
                    # img_array = np.fromfile(full_path, np.uint8)
                    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    # imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
                    # if imgs_ is not None and imgs_ != False:
                    #     print("in_spot_walking_2", imgs_)
                    #     spot_walking = True
                    #     # 여기 걷기 시전
                    # else:
                    #     click_pos_2(110, 160, cla)

            else:
                print("뛰어가", spot_walking_count)
                click_pos_2(400, 610, cla)
            time.sleep(0.3)
    except Exception as e:
        print(e)


def go_to_spot(cla, data):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_reg, click_pos_2, imgs_set_
        from action import skip_click, go_quest_ing_, clean_screen
        from schedule import myQuest_play_add
        import pyautogui

        print("사냥터 이동중")

        attack_ready = False

        move_ = False
        move_count = 0
        while move_ is False:
            move_count += 1
            if move_count > 40:
                move_ = True
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("in_spot_walking_2 보여")
                move_ = True
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\bag_check.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 80, 910, 120, cla, img, 0.83)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(935, 100, cla)
            time.sleep(0.2)

        bihangjang = False
        bihangjang_count = 0
        while bihangjang is False:
            bihangjang_count += 1
            if bihangjang_count > 25:
                bihangjang = True
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\bihangjang.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 80, 160, 110, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("여긴 비행장")
                bihangjang = True
            else:
                print("비행장 이동중?")
                skip_click(cla)
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    bihangjang = True
            time.sleep(0.2)



        flying = False
        flying_count = 0
        while flying is False:
            flying_count += 1
            if flying_count > 25:
                flying = True


            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\flying_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(820, 880, 910, 970, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                flying = True
                fly_to_the_sky = False
                fly_to_the_sky_count = 0
                while fly_to_the_sky is False:
                    fly_to_the_sky_count += 1

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

                            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\flying_.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(820, 880, 910, 970, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\fly_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(770, 970, 960, 1030, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            print("플라잉 부스터!!!")

                    else:
                        full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("in_spot_walking_2 보여...이동중")
                            if fly_to_the_sky_count > 20:
                                fly_to_the_sky = True
                                attack_ready = True
                                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\random_move_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    if data == "sub":
                                        myQuest_play_add(cla, "서브퀘스트")
                                        clean_screen(cla)

                        else:
                            fly_to_the_sky = True

                            #공격
                    time.sleep(3.5)
            else:
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("날려고 달리는 중??")
                else:
                    flying = True
            time.sleep(0.2)

        # attack_ready = False
        attack_ready_count = 0
        overwalking_count = 0
        while attack_ready is False:
            overwalking_count += 1
            if overwalking_count > 100:
                attack_ready = True
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\in_spot_walking_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 880, 500, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                attack_ready_count += 1
                if attack_ready_count < 2:
                    print("열심히 이동중")
                elif attack_ready_count > 200:
                    attack_ready_count = 0
                    full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\random_move_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 960, 420, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        if data == "sub":
                            attack_ready = True
                            myQuest_play_add(cla, "서브퀘스트")
                            clean_screen(cla)
            else:
                full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\jadong\\attack_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(820, 880, 910, 970, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    attack_ready = True
                    result_ = go_quest_ing_(cla)
                    if result_ == False:
                        if data == "jadong":
                            click_pos_2(930, 850, cla)
                        if data == "sub":
                            click_pos_2(800, 150, cla)
            time.sleep(0.3)


    except Exception as e:
        print(e)

def now_playing(cla):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_, click_pos_2, click_pos_reg, imgs_set_, drag_pos
        from potion import potion_check
        from action import clean_screen, out_check, bag_open, go_quest_ing_
        from get_item import guild_jilyung

        print("now_jadong_playing")

        play_ = False

        in_ = False
        while in_ is False:

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
                    time.sleep(0.4)

            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\hunting_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("hunting_1", imgs_)
                in_ = True
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\hunting_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("hunting_2", imgs_)
                in_ = True
            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\check\\hunting_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 850, 600, 900, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("hunting_3", imgs_)
                in_ = True

            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_1\\quest_soolock_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 90, 960, 300, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("quest_soolock_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_1\\quest_complete_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 90, 960, 900, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("quest_complete_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\nightcrows\\data_nc\\imgs\\grow\\grow_1\\quest_complete_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 90, 960, 900, cla, img, 0.83)
            if imgs_ is not None and imgs_ != False:
                print("quest_complete_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

            if in_ == False:
                clean_screen(cla)
                # 공격하기
                result_ = go_quest_ing_(cla)
                if result_ == False:
                    click_pos_2(930, 850, cla)


            else:
                print("정상적으로 사냥중...5초 딜레이중")
                potion_check(cla)
                time.sleep(5)
                play_ = True

        return play_
    except Exception as e:
        print(e)
