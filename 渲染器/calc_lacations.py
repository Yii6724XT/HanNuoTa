import pygame

def calc_locations(screen):
    #确定屏幕宽高
    screen_rect=screen.get_rect()
    width=screen_rect.width
    height=screen_rect.height
    anchor_points = {}
    left_x = width*(1/6)
    mid_x = width*(1/2)
    right_x = width*(5/6)
    #ABC按钮
    abc_bt_y = height*(17/18)
    anchor_points['ABC_bt'] = {
                               'A':(left_x,abc_bt_y),
                               'B':(mid_x,abc_bt_y),
                               'C':(right_x,abc_bt_y)
                              }
    #底层塔片（midbuttom锚点）
    piece_y = height*(8/9)
    anchor_points['piece'] = {
                              'A':(left_x,piece_y),
                              'B':(mid_x,piece_y),
                              'C':(right_x,piece_y)
                             }
    left_hud_x = width*(1/32)
    #左侧工具栏
    left_hud_y_1 = height*(1/18)
    left_hud_y_2 = (left_hud_y_1)+height*(1/12)
    anchor_points['left_hud'] = {
                                 'undo':(left_hud_x,left_hud_y_1),
                                 'redo':(left_hud_x,left_hud_y_2) 
                                }
    #对话框
    title_x = width*(1/2)
    title_y = height*(7/18)
    confirm_bt_x = width*(13/32)
    cancel_bt_x = width*(19/32)
    add_bt_x = width*(2/3)
    reduce_bt_x = width*(1/3)
    bt_y = height*(11/18)
    step_x = width*(1/16)
    anchor_points['chat_box'] = {
                                 'title':(title_x,title_y),
                                 'confirm_bt':(confirm_bt_x,bt_y),
                                 'cancel_bt':(cancel_bt_x,bt_y),
                                 'add_bt':(add_bt_x,title_y),
                                 'reduce_bt':(reduce_bt_x,title_y),
                                 'step':(step_x,left_hud_y_1)
                                }
    #右侧暂停按钮
    right_bt_x = width*(31/32)
    right_bt_y = height*(1/18)
    anchor_points['right_hud'] = {
                                  'pause':(right_bt_x,right_bt_y)
                                 }
    return anchor_points