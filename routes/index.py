import flet as ft
from widgets import add_topic 

def index(page: ft.Page):
    dlg = add_topic.add_topic_modal(page)

    async def open_dlg(e):
        e.control.page.dialog = dlg
        dlg.open = True
        await e.control.page.update_async()
            
    
    return (ft.View(
        "/",
        [
            ft.AppBar(
                title=ft.Text("Мессенджер"), 
                bgcolor=ft.colors.SURFACE_VARIANT,
                actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.ElevatedButton("Open dialog", on_click=open_dlg),
                    ]
                )]),
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                title=ft.Text("The Enchanted Nightingale"),
                                subtitle=ft.Text(
                                    "Music by Julie Gable. Lyrics by Sidney Stein."
                                ),
                            ),
                        ]
                    ),
                    width='100%',
                    padding=10,
                    on_click=lambda _: page.go("/mess/The Enchanted Nightingale")
                )
            ),
        ],
    ))