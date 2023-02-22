import flet   
from flet import IconButton, Page, Row, TextField, icons

def main(page:Page):
    page.title = "Flet prueba"
    page.vertical_alignment="center"

    txt_number = TextField(value="0", text_align="right", width=100)


    def minus_click(event):
        txt_number.value=int(txt_number.value) - 1
        page.update()
        
    def plus_click(event):
        txt_number.value=int(txt_number.value) + 1
        page.update()
        
    page.add(
        Row(
        [
        IconButton(icons.REMOVE, on_click=minus_click),
        txt_number,
        IconButton(icons.ADD, on_click=plus_click),
        ],
        alignment="center",
        )
    )


#Aplicacion de escritorio
#flet.app(target=main)

#Aplicacion Web desde navegador
#flet.app(target=main, view=flet.WEB_BROWSER)


#Aplicacion Web desde una ventana como tkinter
flet.app(port=8550,target=main)