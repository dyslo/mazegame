import tkinter
import random
import generateMaze

# 게임 세팅 기본 변수 설정
# 위 변수들은 대문자로 선언
GAME_MAZE_STRUCT        = generateMaze.generateMaze(20)                 #미로 구조 변수, 만지지 말기
GAME_TITLE = "Maze Game"                #Default: "Maze Game"
GAME_RESIZEABLE_TB      = False              #Default: False
GAME_RESIZEABLE_LR      = False              #Default: False 
GAME_MAZE_BLOCK_SIZE_WIDTH  = 20
GAME_MAZE_BLOCK_SIZE_HEIGHT = 20
GAME_WINDOW_SIZE_WIDTH  = len(GAME_MAZE_STRUCT[0]) * GAME_MAZE_BLOCK_SIZE_WIDTH         #윈도우 넓이, Default: 640
GAME_WINDOW_SIZE_HEIGHT = len(GAME_MAZE_STRUCT) * GAME_MAZE_BLOCK_SIZE_HEIGHT         #윈도우 높이, Default: 400
GAME_WINDOW_STARTPOS_X  = 100         #윈도우 시작 X좌표, Default: 100
GAME_WINDOW_STARTPOS_Y  = 100         #윈도우 시작 Y좌표, Default: 100
GAME_WINDOW_PADDING_X   = 20
GAME_WINDOW_PADDING_Y   = 20
GAME_WINDOW_SIZE = str(GAME_WINDOW_SIZE_WIDTH) + "x" \
                    + str(GAME_WINDOW_SIZE_HEIGHT) + "+" \
                    + str(GAME_WINDOW_STARTPOS_X) + "+" \
                    + str(GAME_WINDOW_STARTPOS_Y) #윈도우 사이즈 

def main():
    window = tkinter.Tk()
    window.title(GAME_TITLE)
    window.geometry(GAME_WINDOW_SIZE)
    window.resizable(GAME_RESIZEABLE_TB, GAME_RESIZEABLE_LR)

    canvas = tkinter.Canvas(width=GAME_WINDOW_SIZE_WIDTH, height=GAME_WINDOW_SIZE_HEIGHT)
    canvas.pack()

    def DrawMaze():
        for y in range(len(GAME_MAZE_STRUCT)):
            for x in range(len(GAME_MAZE_STRUCT[y])):
                if GAME_MAZE_STRUCT[y][x] == 1:
                    canvas.create_rectangle(x * GAME_MAZE_BLOCK_SIZE_WIDTH, y * GAME_MAZE_BLOCK_SIZE_HEIGHT, \
                                            x * GAME_MAZE_BLOCK_SIZE_WIDTH + GAME_MAZE_BLOCK_SIZE_WIDTH, \
                                            y * GAME_MAZE_BLOCK_SIZE_HEIGHT + GAME_MAZE_BLOCK_SIZE_HEIGHT, fill="green")

    DrawMaze()

    window.mainloop()

if __name__ == "__main__":
    main()

