'''Tetris'''

def new_block():
    '''generate a new random block, place it at top of screen'''

def input_keys():
    '''fetch and decode user input'''

def rotate_block():
    '''rotate block as needed'''

def translate_block_down():
    '''redraw block one row down screen'''

def is_collision()->bool:
    '''test if block in new position has collided with anything'''
    return True|False

def test_and_remove_full_lines():
    '''check for presence of full lines, if any remove and re-render'''

def is_screen_full() -> bool:
    '''test if game over'''
    return True|False

def await_timer()->bool:
    '''returns True until move timer expires'''
    yield True|False

while True: # game loop should continue until interrupted
    new_block()
    while True:
        while await_timer():
            input_keys()
            rotate_block()
        translate_block_down()
        if is_collision():
            test_and_remove_full_lines()
            break
    if is_screen_full():
        break # game over
