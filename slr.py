from tkinter import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from tkinter import ttk,ttk
from PIL import Image,ImageTk
from tkinter.font import BOLD
import pandas as pd
class Slr:
    def __init__(self,root):
        self.root=root
        self.root.title("SLR Model")
        self.root.geometry("1000x600+0+0")
        self.year=IntVar()
        dataset=pd.read_csv("hw.csv")
        x=dataset.iloc[:,:-1].values
        y=dataset.iloc[:,-1].values
        x_train,self.x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)
        print(self.x_test)
        self.slr=LinearRegression()
        self.slr.fit(x_train,y_train)
        
        self.frame=Frame(self.root,bg="white")
        self.frame.place(x=20,y=20,width=940,height=500)
        exp=Label(self.frame,text="Height(In Inches)",font=("times new roman",15,"bold"),fg="white",bg="black")
        exp.place(x=400,y=20)
        entryuser=ttk.Entry(self.frame,width=70,textvariable=self.year,font=("arial",13,BOLD))
        entryuser.place(x=150,y=80)
        
        but=Button(self.frame,text="Predict(In KG)",font=("arial",12,BOLD),command=self.pred,fg="silver",bg="black",width=8,padx=10)
        but.place(x=400,y=130)
    def pred(self):
        y_pred=self.slr.predict([[self.year.get()]])*0.45359237
        ep=Label(self.frame,text=y_pred,font=("times new roman",15,"bold"),fg="white",bg="black")
        ep.place(x=380,y=180)
if __name__=="__main__":
    root=Tk()
    obj=Slr(root)
    root.mainloop()