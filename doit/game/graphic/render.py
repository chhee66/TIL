
# render.py
'''
from game.sound.echo import echo_test 
def render_test():
    print("render")
    echo_test()
'''

# relative 버전 render.py
from ..sound.echo import echo_test #cd.. 하듯이 이 파일이 존재하는 디렉터리에서 하나 

def render_test():
    print("render")
    echo_test()
