import flet as ft
from comp.card import card_comp

def index(page: ft.Page):
    title = ft.TextField(label="Название")
    desc = ft.TextField(label="Описание")
    
    async def create_topic(e):
        chat.controls.append(card_comp(page, title.value, desc.value))

        title.value = ''
        desc.value = ''
        dlg.open = False
        await e.control.page.update_async()
    
    async def open_dlg(e):
        e.control.page.dialog = dlg
        dlg.open = True
        await e.control.page.update_async()
                    
    dlg = ft.AlertDialog(
        title=ft.Text("Добавьте тему для чата"),
        content=ft.Column(
            [
                title,
                desc,
                ft.ElevatedButton(text="Добавить", on_click=create_topic),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        on_dismiss=lambda e: page.add(ft.Text("Non-modal dialog dismissed")),
    )

    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )
        
    return (ft.View(
        "/",
        [
            ft.AppBar(
                title=ft.Text("Мессенджер"), 
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.ElevatedButton("Создать тему", on_click=open_dlg),
                    ]
                )]),
            chat
        ],
    ))