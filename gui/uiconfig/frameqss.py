

def makeFrameQss(color):
    frameqss =  '''
        QFrame#CenterWindow{
            background-color: %s;
            border-left: 1px solid transparent;
            border-right: 1px solid transparent;
            border-bottom: none;
            border-top: none;
        }
    '''% (color)
    return frameqss

frameqss = makeFrameQss('rgb(41, 153, 66)')
