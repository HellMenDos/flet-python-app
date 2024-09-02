import flet as ft

def add_topic_modal(page: ft.Page): 
    return ft.AlertDialog(
        title=ft.Text("Добавьте тему для чата"),
        content=ft.Column(
            [
                ft.TextField(label="Название"),
                ft.TextField(label="Описание"),
                ft.ElevatedButton(
                    text="Добавить",
                ),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        on_dismiss=lambda e: page.add(ft.Text("Non-modal dialog dismissed")),
    )