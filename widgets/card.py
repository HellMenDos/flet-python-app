import flet as ft

def card_widget(page: ft.Page, title: str, desc: str):
    return (ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                title=ft.Text(title),
                                subtitle=ft.Text(
                                    desc
                                ),
                            ),
                        ]
                    ),
                    width='100%',
                    padding=10,
                    on_click=lambda _: page.go("/mess/" + title)
                )
        ))