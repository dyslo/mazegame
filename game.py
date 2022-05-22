import tkinter
import tkinter.font as tkFont
import generateMaze
from datetime import datetime

# 게임 세팅 기본 변수 설정
# 위 변수들은 대문자로 선언
GAME_MAZE_STRUCT        = generateMaze.generateMaze(5)                 #미로 구조 변수, 만지지 말기
GAME_TITLE              = "Maze Game"                #Default: "Maze Game"
GAME_RESIZEABLE_TB      = False              #Default: False
GAME_RESIZEABLE_LR      = False              #Default: False 
GAME_MAZE_BLOCK_SIZE_WIDTH  = 15
GAME_MAZE_BLOCK_SIZE_HEIGHT = 15
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
GAME_START_POS = [[j,i] for i in range(len(GAME_MAZE_STRUCT)) for j in range(len(GAME_MAZE_STRUCT[i])) if GAME_MAZE_STRUCT[i][j] == 2] # 시작 위치
GAME_END_POS   = [[j,i] for i in range(len(GAME_MAZE_STRUCT)) for j in range(len(GAME_MAZE_STRUCT[i])) if GAME_MAZE_STRUCT[i][j] == 3]
GAME_STOPWATCH_START = None
GAME_STOPWATCH_END   = None


key = 0
#print(GAME_START_POS[0])
posx = GAME_START_POS[0][0]
posy = GAME_START_POS[0][1]
#print(posx, posy)
#state = 0

#task = None
start_pos = None

def main():

    window = tkinter.Tk()
    window.title(GAME_TITLE)
    window.geometry(GAME_WINDOW_SIZE)
    window.resizable(GAME_RESIZEABLE_TB, GAME_RESIZEABLE_LR)

    canvas = tkinter.Canvas(width=GAME_WINDOW_SIZE_WIDTH, height=GAME_WINDOW_SIZE_HEIGHT)
    
    def DrawMaze():
        global start_pos
        canvas.pack()
        canvas.delete("walls")
        if start_pos is not None:
            canvas.delete(start_pos)
            start_pos = None
        for y in range(len(GAME_MAZE_STRUCT)):
            for x in range(len(GAME_MAZE_STRUCT[y])):
                if GAME_MAZE_STRUCT[y][x] == 1:
                    canvas.create_rectangle(x * GAME_MAZE_BLOCK_SIZE_WIDTH, y * GAME_MAZE_BLOCK_SIZE_HEIGHT, \
                                            x * GAME_MAZE_BLOCK_SIZE_WIDTH + GAME_MAZE_BLOCK_SIZE_WIDTH, \
                                            y * GAME_MAZE_BLOCK_SIZE_HEIGHT + GAME_MAZE_BLOCK_SIZE_HEIGHT, fill="green", outline="green", tags="walls")
                if GAME_MAZE_STRUCT[y][x] == 2:
                    #print("start pos:", x, y)
                    start_pos = canvas.create_rectangle(x * GAME_MAZE_BLOCK_SIZE_WIDTH, y * GAME_MAZE_BLOCK_SIZE_HEIGHT, \
                                            x * GAME_MAZE_BLOCK_SIZE_WIDTH + GAME_MAZE_BLOCK_SIZE_WIDTH, \
                                            y * GAME_MAZE_BLOCK_SIZE_HEIGHT + GAME_MAZE_BLOCK_SIZE_HEIGHT, fill="red", outline="red", tags="start_pos")

    def key_down(e):
        global key, posx, posy
        key = e.keysym
        #print(str(key))
        if key == "Up" and GAME_MAZE_STRUCT[posy-1][posx] != 1:
            posy -= 1
            canvas.move("start_pos", 0, -GAME_MAZE_BLOCK_SIZE_HEIGHT)
        if key == "Down" and GAME_MAZE_STRUCT[posy+1][posx] != 1:
            posy += 1
            canvas.move("start_pos", 0, GAME_MAZE_BLOCK_SIZE_HEIGHT)
        if key == "Left" and GAME_MAZE_STRUCT[posy][posx-1] != 1:
            posx -= 1
            canvas.move("start_pos", -GAME_MAZE_BLOCK_SIZE_WIDTH, 0)
        if key == "Right" and GAME_MAZE_STRUCT[posy][posx+1] != 1:
            posx += 1
            canvas.move("start_pos", GAME_MAZE_BLOCK_SIZE_WIDTH, 0)
        if [posx, posy] == GAME_END_POS[0]:
            endPage()
        #canvas.move("start_pos", posx, posy)
        #print(canvas.coords("start_pos"))
        print(posx, posy)
    
    def mainPage():
        frm_main  = tkinter.Frame(window, bd=1)

        def gameStart():
            global GAME_STOPWATCH_START, key, posx, posy
            key = 0
            posx = GAME_START_POS[0][0]
            posy = GAME_START_POS[0][1] 
            GAME_STOPWATCH_START = datetime.now()
            frm_main.place_forget()
            #stateEventListener()
            DrawMaze()
            window.bind("<Key>", key_down)

        lbl_title = tkinter.Label(frm_main, text="미로 게임", fg="black", font=tkFont.Font(size=30))
        lbl_start = tkinter.Button(frm_main, text="게임 시작", width=15, command=gameStart, padx=20)
        lbl_title.pack()
        lbl_start.pack()
        frm_main.place(relx=.5, rely=.5, anchor="c")

    def endPage():
        global GAME_STOPWATCH_END
        GAME_STOPWATCH_END = datetime.now()
        elapsed_time = GAME_STOPWATCH_END - GAME_STOPWATCH_START
        canvas.pack_forget()
        frm_end = tkinter.Frame(window, bd=1)

        def returnPage():
            global GAME_MAZE_STRUCT
            GAME_MAZE_STRUCT = None
            GAME_MAZE_STRUCT = generateMaze.generateMaze(5)
            frm_end.place_forget()
            mainPage()

        lbl_title = tkinter.Label(frm_end, text="게임 끝", fg="black", font=tkFont.Font(size=30))
        lbl_elapsed_time = tkinter.Label(frm_end, text=str(elapsed_time), fg="black", font=tkFont.Font(size=30))
        lbl_return = tkinter.Button(frm_end, text="게임 시작", width=15, command=returnPage, padx=20)
        lbl_title.pack()
        lbl_elapsed_time.pack()
        lbl_return.pack()
        frm_end.place(relx=.5, rely=.5, anchor="c")
        window.unbind("<Key>")

    '''def stateEventListener():
        global task, GAME_STOPWATCH_START
        #global state
        if [posx, posy] == GAME_END_POS[0]:
            #state = 1
            endPage()
            window.after_cancel(task)
            #return
        task = window.after(10, stateEventListener)'''
    
    mainPage()
    #stateEventListener()
    #window.after(10, stopwatch)
    window.mainloop()

if __name__ == "__main__":
    main()

