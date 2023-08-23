import tkinter as tk
ventana=tk.Tk()
ventana.geometry("200x300")
def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
        
    
    

et=tk.Label(ventana, text="NUMERO")
et.place(x=10, y=10)
resul=tk.Label(ventana, text="RESULTADO: ")
resul.place(x=10, y=80)
resu=tk.Label(ventana, text="")
resu.place(x=100, y=80)
camp=tk.Entry(ventana)
camp.place(x=80, y=10, width=50)
cal=tk.Button(ventana, text="calcular", command=factorial)
cal.place(x=40, y=50)
n=int(camp.get())
resu.config(text=factorial(n))

num=int(input("digite  el numero"))
fac=1
for i in range(1,num+1):
    fac*=i
    
print("el factorial de {} es {}".format(num,fac))
et.pack()
ventana.mainloop()