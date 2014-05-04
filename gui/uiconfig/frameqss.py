

def makeFrameQss(color):
    frameqss =  '''
        QFrame#TitleBar{
            background-color: %s;
        }

        QLabel#TitleLabel{
            color: white;
            font-family: 'Verdana';
            font-size: 12px;
            padding-left: 10px;
        }

        QFrame#NavgationBar{
            background-color: %s;
            border-bottom: 2px solid black;
        }

        QFrame#CenterWindow{
            border-left: 5px solid %s;
            border-right: 5px solid %s;
            border-bottom: none;
            border-top: none;
        }
    '''% (color, color, color, color)
    return frameqss

frameqss = makeFrameQss('rgb(41, 153, 66)')
