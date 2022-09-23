import tkinter as tk

class Operaciones:

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Mi calculadora magica: ")
        self.ventana.geometry("520x480")
        self.ventana.configure(bg="lightblue")
        
        #este nos permite poder modificar la ventana el ancho y alto pero como yo no quiero que esta se modifique lo dejo en 0,0
        self.ventana.resizable=("0,0")
        
        # definimos fuente de letra color y ubicaion de los botones y labels
        self.lblnumero1=tk.Label(self.ventana, text="Ingrese el primer número: ", font=("Verdana",10),bg="lightblue")
        self.lblnumero1.grid(column=0, row=0,padx=20, pady=10)
        self.dato1=tk.DoubleVar(value="")
        self.valor1=tk.Entry(self.ventana, width=20, textvariable=self.dato1, font=("Verdana",10))
        self.valor1.focus()
        self.valor1.grid(column=0, row=1, padx=80, pady=20)
        
        self.lblnumero2=tk.Label(self.ventana, text="Ingrese el segundo número: ",font=("Verdana",10),bg="lightblue")
        self.lblnumero2.grid(column=0, row=2, padx=20, pady=10)
        self.dato2=tk.DoubleVar(value="")
        
        self.valor2=tk.Entry(self.ventana, width=20, textvariable=self.dato2, font=("Verdana",10))
        self.valor2.grid(column=0, row=3, padx=120, pady=20)

        self.btnSuma=tk.Button(self.ventana, text="Suma", font=("Verdana",10), width=10, height=1, bg="#004777", fg="#ffffff", activebackground="#743c92",activeforeground="#ffffff" , command=self.suma)
        self.btnSuma.grid(column=0,row=4,padx=120, pady=5)

        self.btnResta=tk.Button(self.ventana, text="Resta", font=("Verdana",10), width=10, height=1, bg="#004777", fg="#ffffff", activebackground="#743c92",activeforeground="#ffffff" , command=self.resta)
        self.btnResta.grid(column=0,row=5, padx=120, pady=5)

        self.btnMulti=tk.Button(self.ventana, text="Multiplicación", font=("Verdana",10), width=10, height=1, bg="#004777", fg="#ffffff", activebackground="#743c92",activeforeground="#ffffff" ,command=self.multiplicacion)
        self.btnMulti.grid(column=0,row=6, padx=120, pady=5)
        
        self.btnDivision=tk.Button(self.ventana, text="División", font=("Verdana",10), width=10, height=1, bg="#004777", fg="#ffffff", activebackground="#743c92",activeforeground="#ffffff" , command=self.division)
        self.btnDivision.grid(column=0,row=7, padx=120, pady=5)

        self.lblresultado=tk.Label(self.ventana, text="Resultado", font=("Verdana",10),bg="lightblue")
        self.lblresultado.grid(column=0, row=8, padx=120, pady=5)

        self.ventana.mainloop()
        
        
 # definimos las operaciones
    def suma(self):
        
        sumar=int(self.dato1.get())+int(self.dato2.get())
        self.lblresultado.configure(text=sumar)
        

    def resta(self):
        restar=int(self.dato1.get())-int(self.dato2.get())
        self.lblresultado.configure(text=restar)

    def multiplicacion(self):
        multiplicar=int(self.dato1.get())*int(self.dato2.get())
        self.lblresultado.configure(text=multiplicar)

    def division(self):
        dividir=int(self.dato1.get())/int(self.dato2.get())
        self.lblresultado.configure(text=dividir)
    

operacion1=Operaciones()

#integrantes 
#Alfredo jose zelaya lainez
#David isaac fernandez chicas