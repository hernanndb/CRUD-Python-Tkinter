from tkinter import *
from tkinter import messagebox
import sqlite3



#-------------funciones---------------------------------------------------------------------------#

def conexionBBDD():

    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()

    try:

        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIOS VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIO VARCHAR(100))
            ''')

        messagebox.showinfo("BBDD", "BBDD creada con exito")

    except:

        messagebox.showwarning("¡Atencion!", "la BBDD ya existe")



def salirAplicacion():
    valorSalir=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")

    if valorSalir=="yes":
        root.destroy()





def limpiarCampos():


    variableNombre.set("")
    variableID.set("")
    variablePass.set("")
    variableApellido.set("")
    variableDireccion.set("")
    textoComentario.delete(1.0,END)



def crear():
    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + variableNombre.get() +
        "','" + variablePass.get() +
        "','" + variableApellido.get() +
        "','" + variableDireccion.get() +
        "','" + textoComentario.get(1.0,END) + "')")

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro insertado con exito")


def leer():
    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + variableID.get() )

    elUsuario=miCursor.fetchall()

    for usuario in elUsuario:
        variableID.set(usuario[0])
        variableNombre.set(usuario[1])
        variablePass.set(usuario[2])
        variableApellido.set(usuario[3])
        variableDireccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5])

    miConexion.commit()

def actualizar():
    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIOS='" + variableNombre.get() +
        "', PASSWORD='" + variablePass.get() +
        "', APELLIDO='" + variableApellido.get() +
        "', DIRECCION='" + variableDireccion.get() +
        "', COMENTARIOS='" + textoComentario.get("1.0, END") +
        "', WHERE ID=" + variableID.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "El registro se a actualizado con exito")


def borrar():
    miConexion=sqlite3.connect("Usuarios")

    miCursor=miConexion.cursor()

    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" +variableID.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "El registro se borro con exito")





root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)


bbddMenu=Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)


borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Borrar Campos", command=limpiarCampos)

crudMenu=Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=borrar)

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Ayuda")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="Crud", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#-------------------Comienzo de los camposde la app---------------------------------#
miFrame=Frame(root)
miFrame.pack()

variableID=StringVar()
variableNombre=StringVar()
variablePass=StringVar()
variableApellido=StringVar()
variableDireccion=StringVar()


cuadroID=Entry(miFrame, textvariable=variableID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=variableNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame, textvariable=variablePass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="?")

cuadroApellido=Entry(miFrame, textvariable=variableApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=variableDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)


textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

#-----------------aqui comienzan los label------------------------------------#

idLabel=Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

NombreLabel=Label(miFrame, text="Nombre:")
NombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

PassLabel=Label(miFrame, text="Password:")
PassLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

ApellidoLabel=Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

DireccionLabel=Label(miFrame, text="Direccion:")
DireccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

ComentarioLabel=Label(miFrame, text="Comentario:")
ComentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#----------------aQUI EMPIESASN LOS BOTONES ----------------------------------------#

miFrame2=Frame(root)
miFrame2.pack()


botonCrear=Button(miFrame2, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Leer", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Borrar", command=borrar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)





root.mainloop()


