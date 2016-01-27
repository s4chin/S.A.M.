import os

def open_app(app_name):
    os.system(app_name + ' & disown')
open_app('software-center')
