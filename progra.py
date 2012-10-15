# -*- coding: utf-8 -*-
#Lenguajes de Programacion
#Administracion de tecnologias de informacion
#Segunda tarea programada

#Fernanda Fernandez-Miguel Angel Gutierrez-Yessenia Montiel

######################### Importación de Librerías #########################

from Tkinter import * #importar librería gráfica TkInter
import tkMessageBox #importar el módulo para los mensajes de alerta, pregunta etc.
import os #importar la clase os, que ayuda a cerrar ventanas desde funciones
from pyswip import Functor, Variable, Query, call, Prolog
import tkSimpleDialog
from string import * #Modulo de manejo de Strings
import sys #Modulo sys para cerrar el programa
from pyswip import *  #Importa la libreria pyswip para el uso de prolog

#Inicia prolog
p = Prolog()

#Funcion para agregar las recetas a la base de conocimiento
#Recibe los datos de las recetas en strings separadas
def agregar_receta(nbr,ingredientes,pasos,autor,ori,comida):
    #construye la instruccion de prolog
    agregar ="animal("+nbr+","+ingredientes+","+pasos+","+autor+","+ori+","+comida+")"
    #Utiliza el metodo assertz de la libreria pyswip para agregar el animal
    p.assertz(agregar)#Agrega la informacion a la base de conocimientos


#Funcion de despliegue en consola
#Utilizado solo en consola
def desplegar_receta():
    print "Receta:\n"
    print "------------"
    #Ciclo que recorre la base de conocmimientos (como usar un ; en prolog)
    for soln in p.query("animal(Nombre,Ingredientes,Pasos,Autor,Origen,Comida)"):
        print "Nombre: ",soln["Nombre"]
        print "Ingredientes: ", soln["Ingredientes"]
        print "Pasos: ", soln["Pasos"]
        print "Autor: ", soln["Autor"]
        print "Origen: ", soln["Origen"]
        print "Temperatura: ", soln["Comida"]
        print "------------------------"

#Funcion de consulta variable
#Devuelve una lista de respuestas
def ConsultarReceta(nbr,ingredientes,pasos,autor,ori,comida):
    #Construye la consulta
    cons ="animal("+nbr+","+ingredientes+","+pasos+","+autor+","+ori+","+comida+")"

    #Realiza la consulta utilizando el metodo query y lo enlista
    solucion = list(p.query(cons))
    
    #Rellena la lista de soluciones con la informacion no variable
    for temp in solucion:
        if(nbr != "Nombre"):
            temp["Nombre"]=nbr
        if(ingredientes != "Ingredientes"):
            temp["Ingredientes"]=ingredientes
        if(pasos != "Pasos"):
            temp["Pasos"]= pasos
        if(autor != "Autor"):
            temp["Autor"]=autor
        if(ori != "Ori"):
            temp["Ori"]=ori
        if(comida != "Comida"):
            temp["Comida"]=comida
    return solucion


#-----------------------------------------
#Funciones directas de los botones
#-----------------------------------------

#Funcion para salir y cerrar la apliacion
def salir():
    #Salir del programa
    os._exit(100)

#Funcion para abrir el manual de usuario
def info():
    #devolver cuadro de mensaje, con la informacion del programa
    tkMessageBox.showinfo("Acerca de...", 'Es un sistema de ayuda por el chef Giovanni, implementado para el curso de Lenguajes de Programacion.')

#Funcion para ingresar recetas
def IngresarReceta():

    #Recupera los datos de los entrys
    Txt_Nombre = lower(entry_mant_1.get())
    Txt_Ingredientes = lower(entry_mant_2.get())
    Txt_Autor = lower(entry_mant_3.get())
    Txt_Pasos = lower(entry_mant_4.get())
    Txt_Origen = lower(entry_mant_5.get())
    Txt_Comida = lower(entry_mant_6.get())

    #Verificacion de totalidad de datos (No espacios vacios)
    if(Txt_Nombre == "" or Txt_Ingredientes == "" or Txt_Autor == "" or
       Txt_Pasos == "" or Txt_Origen == "" or Txt_Comida == ""):
        info_error=("Toda la información es indispensable")
        tkMessageBox.showerror(title="Error", message=info_error)
        return False
    
    #Verifica que los datos sean alphanumericos
    if(not(Txt_Nombre.isalnum() and Txt_Ingredientes.isalnum() and Txt_Autor.isalnum()
           and Txt_Pasos.isalnum() and Txt_Origen.isalnum() and
           Txt_Comida.isalnum())):
        info_error=("Solo es válido utilizar caracteres alfanuméricos")
        tkMessageBox.showerror(title="Error", message=info_error)
        return False

##    elif(Txt_Comida != "c" and Txt_Comida != "f"):
##        info_error=("Formato invalido en \"Temperatura\"\nIngrese \"f=frio\" o \"c=caliente\"")
##        tkMessageBox.showerror(title="Error", message=info_error)
##        return False


    #Verifica nombres repetidos
    elif(ConsultarReceta(Txt_Nombre,"Ingredientes","Pasos","Autor","Ori"
                            ,"Comida") !=[]):
        info_error=("Ese nombre ya se encuentra en la base de datos")
        tkMessageBox.showerror(title="Error", message=info_error)
        return False

    #Todo OK, llama a la funcion de agregar el receta y despliega mensaje.
    else:
        agregar_receta(Txt_Nombre,Txt_Ingredientes,Txt_Pasos,Txt_Autor,
                       Txt_Origen,Txt_Comida)
        informacion = "La receta fue agregada con exito!"
        tkMessageBox.showinfo(title="Exito!!!!",message=informacion)
        limpieza_entrys()
        return True


#Funcion para realizar consultas
def consultar_animal():
    #Recupera los datos de las entrys
    Txt_Nombre = lower(entry_mant_1.get())
    Txt_Ingredientes = lower(entry_mant_2.get())
    Txt_Autor = lower(entry_mant_3.get())
    Txt_Pasos = lower(entry_mant_4.get())
    Txt_Origen = lower(entry_mant_5.get())
    Txt_Comida = lower(entry_mant_6.get())

    #Verifica que los datos sean alphanumericos
    if(not((Txt_Nombre.isalnum()or Txt_Nombre == "") and
           (Txt_Ingredientes.isalnum()or Txt_Ingredientes == "") and
           (Txt_Autor.isalnum()or Txt_Autor == "") and
           (Txt_Pasos.isalnum()or Txt_Pasos == "") and
           (Txt_Origen.isalnum()or Txt_Origen == "") and
           (Txt_Comida.isalnum()or Txt_Comida == ""))):
        info_error=("Solo es válido utilizar caracteres alfanuméricos")
        tkMessageBox.showerror(title="Error", message=info_error)
        return False
##
##    elif(Txt_Comida != "c" and Txt_Comida != "f"):
##        info_error=("Formato invalido en \"Temperatura\"\nIngrese \"f=frio\" o \"c=caliente\"")
##        tkMessageBox.showerror(title="Error", message=info_error)
##        return False

 
    #Realiza la consulta a la Base de conocimiento
    else:
        #Transforma los espacios vacios en variables de prolog
        if(Txt_Nombre == ""):
            Txt_Nombre = "Nombre"
        if(Txt_Ingredientes == ""):
            Txt_Ingredientes = "Ingredientes"
        if(Txt_Autor == ""):
            Txt_Autor = "Autor"
        if(Txt_Pasos == ""):
            Txt_Pasos = "Pasos"
        if(Txt_Origen == ""):
            Txt_Origen = "Ori"
        if(Txt_Comida == ""):
            Txt_Comida = "Comida"

        #Realiza la consulta y la almacena en una lista de diccionarios
        respuesta =ConsultarReceta(Txt_Nombre,Txt_Ingredientes,Txt_Pasos,
                                      Txt_Autor,Txt_Origen,Txt_Comida)

        res_text = ""
        #Crea el texto con las respuestas
        if (respuesta == []):
            res_text= "No se encontraron recetas son esas caracteristicas"
        else:
            indice = 1
            for cons in respuesta:
                res_text =(res_text + "-------------------------" +
                           "\nResultado Número: " + str(indice) +
                           "\nNombre: "+ str(cons["Nombre"]) +
                           "\nIngredientes: "+ str(cons["Ingredientes"]) +
                           "\nPasos: "+ str(cons["Pasos"]) +
                           "\nAutor: "+ str(cons["Autor"]) +
                           "\nOrigen: "+ str(cons["Ori"]) +
                           "\nComida: "+ str(cons["Comida"]) + "\n")
                indice = indice +1
            res_text =(res_text + "-------------------------")

        #Coloca el texto en la ventana
        colocar_respuesta(res_text)
        return True
        

#Funciones de Manejo Grafico
def limpieza_entrys():
    #Limpia los campos de las entrys
    entry_mant_1.delete(0,END)
    entry_mant_2.delete(0,END)
    entry_mant_3.delete(0,END)
    entry_mant_4.delete(0,END)
    entry_mant_5.delete(0,END)
    entry_mant_6.delete(0,END)
    return

def limpieza_general():
    #Quita de la ventana principal los botones, entrys y frames
    limpieza_entrys()
    label_mant_0.grid_remove()
    label_mant_1.grid_remove()
    entry_mant_1.grid_remove()
    label_mant_2.grid_remove()
    entry_mant_2.grid_remove()
    label_mant_3.grid_remove()
    entry_mant_3.grid_remove()
    label_mant_4.grid_remove()
    entry_mant_4.grid_remove()
    label_mant_5.grid_remove()
    entry_mant_5.grid_remove()
    label_mant_6.grid_remove()
    entry_mant_6.grid_remove()
    label_res_0.pack_forget()
    boton_ingresar.grid_remove()
    boton_consultar.grid_remove()
    frame_respuesta.pack_forget()
    return

def colocar_mantenimiento():
    #Coloca en la ventana principal los labes y entrys para la captura de datos
    limpieza_general()
    label_mant_0.grid(row=0, sticky=W, columnspan=2)
    label_mant_1.grid(row=1, sticky=E)
    entry_mant_1.grid(row=1,column=1, sticky=W)
    label_mant_2.grid(row=2, sticky=E)
    entry_mant_2.grid(row=2,column=1, sticky=W)
    label_mant_3.grid(row=3, sticky=E)
    entry_mant_3.grid(row=3, column=1, sticky=W)
    label_mant_4.grid(row=4, sticky=E)
    entry_mant_4.grid(row=4, column=1, sticky=W)
    label_mant_5.grid(row=5, sticky=E)
    entry_mant_5.grid(row=5, column=1, sticky=W)
    label_mant_6.grid(row=6, sticky=E)
    entry_mant_6.grid(row=6, column=1, sticky=W)
    boton_ingresar.grid(row=1, column=2, sticky=E, rowspan=8, columnspan=8)
    return

def colocar_consultar():
    #Coloca en la ventana principal los labes y entrys para la captura de datos
    limpieza_general()
    label_mant_0.grid(row=0, sticky=W, columnspan=2)
    label_mant_1.grid(row=1, sticky=E)
    entry_mant_1.grid(row=1,column=1, sticky=W)
    label_mant_2.grid(row=2, sticky=E)
    entry_mant_2.grid(row=2,column=1, sticky=W)
    label_mant_3.grid(row=3, sticky=E)
    entry_mant_3.grid(row=3, column=1, sticky=W)
    label_mant_4.grid(row=4, sticky=E)
    entry_mant_4.grid(row=4, column=1, sticky=W)
    label_mant_5.grid(row=5, sticky=E)
    entry_mant_5.grid(row=5, column=1, sticky=W)
    label_mant_6.grid(row=6, sticky=E)
    entry_mant_6.grid(row=6, column=1, sticky=W)
    boton_consultar.grid(row=1, column=2, sticky=E, rowspan=8, columnspan=8)
    return

def colocar_respuesta(respuesta_text):
    #Coloca en la venta principal el frame con el texto de la respuesta
    #De una consulta
    limpieza_general()
    label_res_0.pack()
    texto_respuesta.delete(1.0, END)
    frame_respuesta.pack()
    texto_respuesta.insert(END, respuesta_text)

########################################################
#Interfaz Grafica
########################################################
#------------------

#Crear la ventana principal y configurarla

raiz = Tk()

raiz.title("Bienvenue au restaurant Le Puolet")


#Configuracion de columnas y filas para ver de la forma esperada

raiz.columnconfigure(1,weight=2)

raiz.rowconfigure(2,weight=2)



#Crear la barra de menu

barra_menu = Menu(raiz)

raiz.config(menu=barra_menu)


#Crear los botones del menu

barra_menu.add_command(label="Inicio", command =limpieza_general)

barra_menu.add_command(label="Mantenimiento", command =colocar_mantenimiento)

barra_menu.add_command(label="Consuta", command =colocar_consultar)

barra_menu.add_command(label="Acerca de...", command=info)

barra_menu.add_command(label="Salir", command=salir)

#Imagen del restaurante y "Frame" general
fondo = PhotoImage(file="fo.gif")
principal = Label(raiz, image=fondo)
principal.image_zoo = fondo
w = fondo.width()
h = fondo.height()
raiz.geometry("%dx%d+0+0" % (w, h))
principal.pack(side='top', fill='both', expand='yes')



###################
## Mantenimiento y Consulta
###################
#Labels, Entrys y Botones para ingreso y consulta de recetas
label_mant_0 = Label(principal, text="Ingrese los datos de la receta",
                     font=("", 15),bg ="white", relief=RIDGE, bd=5)
label_mant_1 = Label(principal, text="Nombre",font=("", 10))
entry_mant_1 = Entry(principal,takefocus="",bg="White",width=10)
label_mant_2 = Label(principal, text="Ingredientes",font=("", 10))
entry_mant_2 = Entry(principal,takefocus="",bg="White",width=10)
label_mant_3 = Label(principal, text="Pasos",font=("", 10))
entry_mant_3 = Entry(principal,takefocus="",bg="White",width=10)
label_mant_4 = Label(principal, text="Autor",font=("", 10))
entry_mant_4 = Entry(principal,takefocus="",bg="White",width=10)
label_mant_5 = Label(principal, text="Pais",font=("", 10))
entry_mant_5 = Entry(principal,takefocus="",bg="White",width=10)
label_mant_6 = Label(principal, text="Temperatura",font=("", 10))
entry_mant_6 = Entry(principal,takefocus="",bg="White",width=10)
boton_ingresar = Button(principal,takefocus="", text="Ingresar Receta!!",
                        command=IngresarReceta)#, height=7, width=15)
boton_consultar = Button(principal,takefocus="",
                         text="Realizar Consulta!!!",
                         command=consultar_animal)#, height=7, width=15)
label_res_0 = Label(principal, text="Resultado de la Consulta",
                     font=("", 15),bg ="white", relief=RIDGE, bd=5)

#frame ,texarea y scroll para resultado de consulta
frame_respuesta=Frame(principal)
texto_respuesta=Text(frame_respuesta,height=15,width=50,background='white')
scroll_respuesta=Scrollbar(frame_respuesta)
texto_respuesta.configure(yscrollcommand=scroll_respuesta.set)
texto_respuesta.pack(side=LEFT)
scroll_respuesta.pack(side=RIGHT,fill=Y)


mainloop()
