import flet as ft


def main(page:ft.page):

    page.window_width=500
    page.window_height=700
    textField =ft.TextField()
    addBtn = ft.ElevatedButton(text="Agregar")

    page.add(textField, addBtn)



#Aplicacion de escritorio
ft.app(target=main)

#Aplicacion Web desde navegador
#ft.app(target=main, view=ft.WEB_BROWSER)


#Aplicacion Web desde una ventana como tkinter
#ft.app(port=8550,target=main)