import tkinter as tk

calcul=""

def ajout_calcul(symbol):
    global calcul
    calcul+=str(symbol)
    text_resultat.delete(1.0, "end")
    text_resultat.insert(1.0,calcul)

def eval_calcul():
    global calcul
    try:
        calcul=str(eval(calcul))
        text_resultat.delete(1.0, "end")
        text_resultat.insert(1.0, calcul)
    except:
        effacer_ecran()
        text_resultat.insert(1.0, "Erreur")
def effacer_ecran():
    global calcul
    calcul = ""
    text_resultat.delete(1.0, "end")

#interface écran
root=tk.Tk()
root.geometry("300x275")

text_resultat=tk.Text(root,height=2, width=16, font=('Arial',24))
text_resultat.grid(columnspan=5)


#touches
btn_1=tk.Button(root,text="1", command=lambda:ajout_calcul(1), width=5, font=('Arial',14))
btn_1.grid(row=2,column=1)

btn_2=tk.Button(root,text="2", command=lambda:ajout_calcul(2), width=5, font=('Arial',14))
btn_2.grid(row=2,column=2)

btn_3=tk.Button(root,text="3", command=lambda:ajout_calcul(3), width=5, font=('Arial',14))
btn_3.grid(row=2,column=3)

btn_4=tk.Button(root,text="4", command=lambda:ajout_calcul(4), width=5, font=('Arial',14))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(root,text="5", command=lambda:ajout_calcul(5), width=5, font=('Arial',14))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(root,text="6", command=lambda:ajout_calcul(6), width=5, font=('Arial',14))
btn_3.grid(row=3,column=3)

btn_7=tk.Button(root,text="7", command=lambda:ajout_calcul(7), width=5, font=('Arial',14))
btn_7.grid(row=4,column=1)

btn_8=tk.Button(root,text="8", command=lambda:ajout_calcul(8), width=5, font=('Arial',14))
btn_8.grid(row=4,column=2)

btn_9=tk.Button(root,text="9", command=lambda:ajout_calcul(9), width=5, font=('Arial',14))
btn_1.grid(row=4,column=3)

btn_0=tk.Button(root,text="0", command=lambda:ajout_calcul(0), width=5, font=('Arial',14))
btn_0.grid(row=5,column=2)

btn_open=tk.Button(root,text="(", command=lambda:ajout_calcul("("), width=5, font=('Arial',14))
btn_open.grid(row=5,column=1)

btn_close=tk.Button(root,text=")", command=lambda:ajout_calcul(")"), width=5, font=('Arial',14))
btn_close.grid(row=5,column=3)

btn_som=tk.Button(root,text="+", command=lambda:ajout_calcul("+"), width=5, font=('Arial',14))
btn_som.grid(row=2,column=5)

btn_sous=tk.Button(root,text="-", command=lambda:ajout_calcul("-"), width=5, font=('Arial',14))
btn_sous.grid(row=3,column=5)

btn_mult=tk.Button(root,text="x", command=lambda:ajout_calcul("*"), width=5, font=('Arial',14))
btn_mult.grid(row=4,column=5)

btn_div=tk.Button(root,text="/", command=lambda:ajout_calcul("/"), width=5, font=('Arial',14))
btn_div.grid(row=5,column=5)

btn_egal=tk.Button(root,text="=", command=eval_calcul, width=5, font=('Arial',14))
btn_egal.grid(row=6,column=3, columnspan=2)

btn_clear=tk.Button(root,text="C", command=effacer_ecran, width=5, font=('Arial',14))
btn_clear.grid(row=6,column=1, columnspan=2)

root.mainloop()