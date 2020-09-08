import time

# windows
default_resolution = (1920, 1080)
left_mid_right = (553, 814, 553)
title_h = 55
window_shift = 15
region_dict = {}
duel_step_words = (1117, 109, 1271, 147)
end_step_words = (861, 1055, 1063, 1103)

# gate button
btn_dict = {}
btn_dict_shift = {
    'gate': (666, 1080),
    'center': (960, 552),
    'duel_btn': (960, 552),
    'step_btn': (1315, 743),
    'summon_btn': (886, 854),
    'attack_btn': (963, 852),
    'down_btn': (939, 1074),
    'monster0': (961, 666),
    'monster1': (1086, 666),
    'monster2': (835, 666),
    'end_btn': (960, 1050),
}

color_dict = {
    'yellow': (18, 0, 160, 36, 255, 255),
    'white': (83, 0, 10, 255, 255, 176)
}
# duel step
words_dict = {'active_step': ['你', '行'],
              'battle_step': ['你', '战'],
              'end_step': ['你','结'],
              'finish_step': ['好', '下']
              }

pos = None


def get_pos(p):
    global pos
    if p:
        pos = p


def init_region():
    global region_dict
    mid_region = (pos[0] + left_mid_right[0] + window_shift,
                  pos[1] + title_h,
                  left_mid_right[1],
                  default_resolution[1]
                  )
    left_region = (pos[0] + left_mid_right[0] + left_mid_right[1] + window_shift,
                   pos[1] + title_h,
                   left_mid_right[2],
                   default_resolution[1]
                   )
    step_region = (pos[0] + duel_step_words[0] + window_shift,
                   pos[1] + duel_step_words[1],
                   pos[0] + duel_step_words[2] + window_shift,
                   pos[1] + duel_step_words[3]
                   )

    end_region = (pos[0] + end_step_words[0] + window_shift,
                  pos[1] + end_step_words[1],
                  pos[0] + end_step_words[2] + window_shift,
                  pos[1] + end_step_words[3]
                  )
    region_dict['middle'] = mid_region
    region_dict['right'] = left_region
    region_dict['duel_words'] = step_region
    region_dict['end_words'] = end_region


def init_btn():
    global btn_dict
    for k, v in btn_dict_shift.items():
        tmp = (v[0] + pos[0] + window_shift, v[1] + pos[1])
        btn_dict[k] = tmp


def init_context():
    while not pos:
        time.sleep(1)
        print('wait position!')
        continue
    init_region()
    init_btn()
