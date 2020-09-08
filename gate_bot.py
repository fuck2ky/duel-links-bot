from window import *
from locate import *
from colorocr import Ocr
from mclick import *


def finish_ops():
    finish_conut = 0
    while not locate.locate_img('./image/mail.png', 'middle'):
        # if not ocr.do(c=color_dict['white'], region=region_dict['end_words'], words='finish_step',
        #               orway=True):
        #     click.click_btn('center')
        # else:
        click.click_btn('end_btn')
        click.click_btn('center')
        finish_conut += 1
        print('end loop is %d' % finish_conut)
        if finish_conut >= 20:
            ag.press('esc')
            finish_conut = 0

    return True


if __name__ == "__main__":
    win = Window(3)
    win.start_window_watch(get_pos)
    win.start()

    init_context()

    locate = Location()
    click = Click()
    ocr = Ocr()

    print('start gate duel')
    gate_duel_step = 0

    while True:
        # step0  from main to gate
        gate_duel_step = 0
        if gate_duel_step == 0 and not locate.locate_img('./image/mail.png', 'middle'):
            time.sleep(0.5)
            click.click_btn('center')
            continue
        click.click_btn('gate', times=2, wait=1)
        if not locate.locate_img('./image/gate.png', 'middle', timeout=12):
            print('not find gate.try return')
            gate_duel_step = 0
        else:
            print('start duel!')
            # step1 duel
            gate_duel_step = 1

        if gate_duel_step == 1:
            while not locate.locate_img('./image/duel1.png', 'middle', click=True):
                continue
            while not locate.locate_img('./image/duel1.png', 'middle', click=True):
                click.click_btn('center')
            while not ocr.do(c=color_dict['yellow'], region=region_dict['duel_words'], words='active_step'):
                click.click_btn('center')
            gate_duel_step = 2
        # step1 duel start. my turn
        monster = 0
        while True and gate_duel_step == 2:

            active_loop = 0
            while not ocr.do(c=color_dict['yellow'], region=region_dict['duel_words'], words='active_step'):
                click.click_btn('center')
                active_loop += 1
                if active_loop > 10 and monster >= 2 and finish_ops():
                    print('2 monster finish')
                    break
            if active_loop > 10:
                break
            if monster < 3:
                # summon
                click.click_btn('down_btn', wait=1)
                click.click_btn('summon_btn', wait=0.5)
                monster += 1
                print('moster is %d summon ' % monster)
                click.click_btn('center', times=2)
            battle_loop = 0
            click.click_btn('step_btn', times=2, wait=1, interval=0.5)
            while not ocr.do(c=color_dict['yellow'], region=region_dict['duel_words'], words='battle_step'):
                if ocr.do(c=color_dict['yellow'], region=region_dict['duel_words'], words='end_step'):
                    break
                if ocr.do(c=color_dict['yellow'], region=region_dict['duel_words'], words='active_step'):
                    break
                click.click_btn('center', times=2)
                battle_loop += 1
                if battle_loop == 4:
                    break
            if ocr.do(c=color_dict['yellow'], region=region_dict['duel_words'], words='battle_step'):
                for i in range(monster):
                    click.click_btn('monster' + str(i), wait=0.5)
                    click.click_btn('attack_btn')
                    print('monster' + str(i) + ' attack!')
                    click.click_btn('center', times=2)
            if ocr.do(c=color_dict['yellow'], region=region_dict['duel_words'], words='battle_step'):
                click.click_btn('step_btn', times=2, interval=0.3)
            time.sleep(1)
            if monster == 3:
                if finish_ops():
                    print('finish!!')
                    gate_duel_step = 0
                    break

        gate_duel_step = 0
