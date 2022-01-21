from typing import Dict, Union, Tuple


def direction(facing: str, turn: int):
    """
   direction(facing: str, turn: int)

   Optional keyword arguments:
   facing:  start direction, string of 'N,NE,E,SE,S,SW,W,NW'.
   turn:   number between -1080 and 1080, step=45.
   """
    resultDirection = 'None'
    dictCompass: Dict[str, Union[Tuple[int, int, int, int, int], Tuple[int, int, int, int]]] = {
        'N': (0, 360, 720, 1080, 1440),
        'NE': (45, 405, 765, 1125),
        'E': (90, 450, 810, 1170),
        'SE': (135, 495, 855, 1215),
        'S': (180, 540, 900, 1260),
        'SW': (225, 585, 945, 1305),
        'W': (270, 630, 990, 1350),
        'NW': (315, 675, 1035, 1395),

    }

    try:
        facing = facing.upper()
        if 0 != turn % 45 or \
                turn not in range(-1080, 1081) or \
                facing not in dictCompass.keys():
            return print('Please enter correct arguments !')

        facingTwoInt: int = turn + dictCompass.get(facing)[0]
        if 0 >= facingTwoInt:
            facingTwoInt += 1080

        for i in dictCompass.items():
            facingIter, listDegree = i
            if facingTwoInt in listDegree:
                resultDirection = facingIter

    except Exception as e:
        print('Error:\n', e)

    return resultDirection


print(direction('s', -900))
