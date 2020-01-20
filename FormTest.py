# モジュールのインポート
import numpy as np
import glob
import os, tkinter, tkinter.filedialog, tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def jagge(imgfile):
    imagefile = Image.open(imgfile)

    imagefile.show()
    # 画像の読込
    #global imgfile
    #img_path = (imgfile)
    #img = img_to_array(load_img(img_path, target_size=(256,256)))

    # 取り込んだ画像の表示
    #win = Tk()
    #win.title('ワンコ')
    #imagefile = ImageTk.PhotoImage(file=imgfile) 
    #cv=Canvas(bg="black",width=400-1,height=266-1)
    #cv.create_image(1,1,image=imagefile,anchor=tkinter.NW)
    #win.mainloop()


# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('犬種判別プログラム','処理ファイルを選択してください！')
imgfile = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

# 処理ファイル名の出力
tkinter.messagebox.showinfo('犬種判別プログラム',imgfile)
print('取り込んだファイル名:',imgfile)
jagge(imgfile)
