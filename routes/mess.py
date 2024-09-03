    
import flet as ft

def mess(page: ft.Page):
    title = page.route.split('/')[2]
    
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    
    new_message = ft.TextField(
        hint_text="Напиши свое сообщение...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
    )

    async def add_message(e):
        user_name = page.session.get("user_name")
        chat.controls.append(ft.Text('{}: {}'.format(user_name,new_message.value)))
        await e.control.page.update_async()

    return (ft.View(
        "/mess",
        [
            ft.AppBar(title=ft.Text(title), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Container(
                content=chat,
                border=ft.border.all(1, ft.colors.OUTLINE),
                border_radius=5,
                padding=10,
                expand=True,
            ),
            ft.Row(
                [
                    new_message,
                    ft.IconButton(
                        icon=ft.icons.SEND_ROUNDED,
                        tooltip="Send message",
                        on_click=add_message
                    ),
                ]
            ),    
        ])
    )