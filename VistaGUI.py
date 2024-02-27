from tkinter import *
from tkinter import ttk
from JuegoGUI import Juego
from Jugador import Jugador

class VistaGUI: 
    raiz : Tk
    newFrame : Frame 
    num_jug : IntVar
    entradas : list[Entry]
    texto1 : Label
    

    def __init__(self) -> None:
        self.raiz = Tk()
        self.juego = Juego()
        # self.raiz.geometry("900x500")
        self.raiz.title("Ruleta de la suerte")
        self.newFrame = Frame(self.raiz, width=900, height=450)
        self.newFrame.pack()
        self.newFrame.config(bg="blue")
        self.num_jug = IntVar()
        self.entradas = []
       


    def bienvenida(self):
       textoBienvenida = Label(self.newFrame, text="¡Bienvenidx a la ruleta!")
       textoBienvenida.grid(row=0, column=0,pady=100, columnspan=12)
       textoBienvenida.config(font=(20))
       
       self.foto_dados = PhotoImage(file="./Multimedia/dados.png")
       Label(self.newFrame, image=self.foto_dados).grid(row=1, column=0, columnspan=12, pady=5)

    
    def cuantos_jugadores(self):
        texto1 = Label(self.newFrame, text="Número de jugadores:" )
        texto1.grid(row=3, column=0, columnspan=12, pady=10, sticky="ew")
        b2jug = Button(self.newFrame, text=2, command=lambda: self.crear_etiquetas_y_entrys(int(b2jug["text"]), texto1))
        b2jug.grid(row=4, column=1, padx=5, sticky="ew")

        b3jug = Button(self.newFrame, text=3, command=lambda: self.crear_etiquetas_y_entrys(int(b3jug["text"]), texto1))
        b3jug.grid(row=4, column=3, padx=5, sticky="ew")

        b4jug = Button(self.newFrame, text=4, command=lambda: self.crear_etiquetas_y_entrys(int(b4jug["text"]), texto1))
        b4jug.grid(row=4, column=5, padx=5, sticky="ew")

        b5jug = Button(self.newFrame, text=5, command=lambda: self.crear_etiquetas_y_entrys(int(b5jug["text"]), texto1))
        b5jug.grid(row=4, column=7, padx=5, sticky="ew")

        b6jug = Button(self.newFrame, text=6, command=lambda: self.crear_etiquetas_y_entrys(int(b6jug["text"]), texto1))
        b6jug.grid(row=4, column=9, padx=5, sticky="ew")

    def establecer_num_jugadores(self): 
        return len(self.entradas)

    def crear_etiquetas_y_entrys(self, num_elementos, texto1):
        j = -1
        for i in range(num_elementos):
            j +=  1
            etiqueta = Label(self.newFrame, text=f"Jugador {i+1}:")
            etiqueta.grid(row=5, column=j, padx=5, pady=5)
            j += 1
            entrada = Entry(self.newFrame)
            entrada.grid(row=5, column=j, padx=5, pady=5)
            self.entradas.append(entrada)
        enviar = Button(self.newFrame, text="Enviar", command=self.botonenviar)
        enviar.grid(row=6, column=12)
      

    def enviar(self): 
        nombres_jugadores = []
        for entrada in self.entradas: 
            nombres_jugadores.append(entrada.get())
        self.juego.crear_jugadores(nombres_jugadores)
        print(self.juego.lista_jugadores)
        
    def botonenviar(self):
        self.enviar()
        self.limpiar_vista()
        

    def limpiar_vista(self):
        for widget in self.raiz.winfo_children():
            widget.destroy()

    def numero_jug(self, x: int): 
        self.num_jug.set(x)
    
    def mostrar_turno(self, i):
        
        texto = Label(self.newFrame, text="Jugador"+ ", es tu turno, ¿Qué quieres hacer?")
        texto.grid(row=0, column=0, columnspan=3)
        girar = Button(self.newFrame, text="Girar la ruleta")
        girar.grid(row=1, column=0)
        comprar = Button(self.newFrame, text="Comprar una vocal")
        comprar.grid(row=1, column=2)
        resolver = Button(self.newFrame, text="Resolver el panel")
        resolver.grid(row=2, column=0)
        salir = Button(self.newFrame, text="Salir del juego")
        salir.grid(row=2, column=2)
        Label(self.newFrame, text=f"Puntuación:self.juego.lista_jugadores[i].puntuacion").grid(row=3, column=1)




    
        
if __name__ == "__main__":
    t = VistaGUI() 
    jueg = Juego()
    j1 = Jugador("Nadia")
    j2 = Jugador("Marquez")
    jueg.anhadirJugador(j1)
    jueg.anhadirJugador(j2)

    print(jueg.lista_jugadores)

    # Verificar si hay jugadores en la lista antes de llamar a mostrar_turno
    if jueg.lista_jugadores:
        t.mostrar_turno(0)
        print(jueg.lista_jugadores[0].nombre)
    else:
        print("No hay jugadores en la lista")

    t.raiz.mainloop()
# print(btn.configure().keys()) para saber las cositas