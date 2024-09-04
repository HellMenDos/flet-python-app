import flet as ft
from widgets import card, list
from typing import TypedDict


class Message(TypedDict):
    title: str
    desc: str
    
def index(page: ft.Page):
    title = ft.TextField(label="Название")
    desc = ft.TextField(label="Описание")
    
    def on_message(message: Message):
        topics = page.session.get("topics") if page.session.get("topics") else []
        topic = card.card_widget(page, message.get('title'), message.get('desc'))
        
        page.session.set("topics", [*topics, topic])
        topic_list.controls.append(topic)
        page.update()

    page.pubsub.subscribe(on_message)
    def create_topic(e):
        page.pubsub.send_all(Message(title=title.value,desc=desc.value)),
        
        title.value = ''
        desc.value = ''
        dlg.open = False
    
    async def open_dlg(e):
        e.control.page.dialog = dlg
        dlg.open = True
        await e.control.page.update_async()

    topic_list = list.list_widget()
    if page.session.get("topics"):
        topic_list.controls = [ *page.session.get("topics") ]          
          
    dlg = ft.AlertDialog(
        title=ft.Text("Добавьте тему для чата"),
        content=ft.Column(
            [ title, desc, ft.ElevatedButton(text="Добавить", on_click=create_topic) ],
            spacing=40,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        on_dismiss=lambda e: page.add(ft.Text("Non-modal dialog dismissed")),
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
            topic_list
        ],
    ))