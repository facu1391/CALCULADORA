from time import sleep
import tkinter as tk
from tkinter import messagebox


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x450')
        self.resizable(0,0)
        self.title('Calculadora')
        #2self.iconbitmap('calculadora.ico')
        #atributo de clase
        self.expresion = ''
        #caja de texto (input)
        self.entrada = None
        #stringVar lo utilizamos para obtener el valor de input
        self.entrada_texto = tk.StringVar()
        #creamos los componentes
        self._creacion_componentes()

    #metodo de clase 
    #metodo para crear los componentes
    def _creacion_componentes(self):
        #creamos un frame para la caja de texto
        entrada_frame = tk.Frame(self, width=400, height=50, bg='grey')
        entrada_frame.pack(side=tk.TOP)
        #caja de texto 
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'), textvariable=self.entrada_texto, width=30, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10)

        #creamos otro frame para la parte inferior
        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        botones_frame.pack()

        #primer renglon
        #boton de limpiar
        boton_limpiar = tk.Button(botones_frame, text='C', width=32, height=3, bd=0, bg='#eee', cursor='hand2', command=self._evento_limpiar)
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        #boton de dividir
        boton_divir = tk.Button(botones_frame, text='/', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._envento_click('/'))
        boton_divir.grid(row=0, column=3, padx=1, pady=1)

        #segundo rebglon
        boton_siete = tk.Button(botones_frame, text='7', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._envento_click(7))
        boton_siete.grid(row=1, column=0, padx=1, pady=1)

        boton_ocho = tk.Button(botones_frame, text='8', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._envento_click(8))
        boton_ocho.grid(row=1, column=1, padx=1, pady=1)

        boton_nueve = tk.Button(botones_frame, text='9', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._envento_click(9))
        boton_nueve.grid(row=1, column=2, padx=1, pady=1)

        boton_multiplicar = tk.Button(botones_frame, text='*', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._envento_click('*'))
        boton_multiplicar.grid(row=1, column=3, padx=1, pady=1)

        #tercer rebglon
        boton_cuatro = tk.Button(botones_frame, text='4', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._envento_click(4))
        boton_cuatro.grid(row=2, column=0, padx=1, pady=1)

        boton_cinco = tk.Button(botones_frame, text='5', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._envento_click(5))
        boton_cinco.grid(row=2, column=1, padx=1, pady=1)

        boton_seis = tk.Button(botones_frame, text='6', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._envento_click(6))
        boton_seis.grid(row=2, column=2, padx=1, pady=1)

        boton_restar = tk.Button(botones_frame, text='-', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._envento_click('-'))
        boton_restar.grid(row=2, column=3, padx=1, pady=1)

        #cuarto rebglon
        boton_uno = tk.Button(botones_frame, text='1', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._envento_click(1))
        boton_uno.grid(row=3, column=0, padx=1, pady=1)

        boton_dos = tk.Button(botones_frame, text='2', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._envento_click(2))
        boton_dos.grid(row=3, column=1, padx=1, pady=1)

        boton_tres = tk.Button(botones_frame, text='3', width=10, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._envento_click(3))
        boton_tres.grid(row=3, column=2, padx=1, pady=1)

        boton_sumar = tk.Button(botones_frame, text='+', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._envento_click('+'))
        boton_sumar.grid(row=3, column=3, padx=1, pady=1)

        #quinto renglon
        boton_cero = tk.Button(botones_frame, text='0', width=21, height=3, bd=0, bg='#fff', cursor='hand2', command=lambda: self._envento_click(0))
        boton_cero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        boton_punto = tk.Button(botones_frame, text='.', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=lambda: self._envento_click('.'))
        boton_punto.grid(row=4, column=2, padx=1, pady=1)

        boton_evaluar = tk.Button(botones_frame, text='=', width=10, height=3, bd=0, bg='#eee', cursor='hand2', command=self._envento_evaluar)
        boton_evaluar.grid(row=4, column=3, padx=1, pady=1)

    def _envento_evaluar(self):
        #eval evalua la expresion str como una expresion arismetica
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrio un error: {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion =''



    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)  

    def _envento_click(self, elemento):
        #cocatenamos el nuevo elemento a la expresion ya existente 
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)   
    
if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()