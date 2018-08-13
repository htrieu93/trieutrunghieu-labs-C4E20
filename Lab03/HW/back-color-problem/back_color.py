from random import *
from inside import is_inside

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    text = []
    color = []
    
    for box in shapes:
        text.append(box['text'].upper())
    for box in shapes:
        color.append(box['color'].upper())

    return [
                choice(text),
                choice(color),
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    rect_answer = []
    for box in shapes:
        if quiz_type == 0:
            if box['text'].upper() == text:
                rect_answer = box['rect']
        elif quiz_type == 1:
            if box['color'] == color:
                rect_answer = box['rect']
    
    if is_inside([x, y], rect_answer):
        return True
    else:
        return False

