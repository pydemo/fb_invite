from ui.include.UiLayout import UiLayout


def init(**kwargs):
    global  uilyt
    pipeline=kwargs['pipeline']
    uilyt = UiLayout(pipeline)

    