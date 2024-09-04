import flet as ft
from routes import index, mess

def main(page: ft.Page):
    page.title = "Мессанджер"
    user_name = ft.TextField(label="Название")

    async def join_chat_click(e):
        if not user_name.value:
            user_name.error_text = "Поле имени не может быть пустым"
            await e.control.page.update_async()
        else:
            page.session.set("user_name", user_name.value)
            page.dialog.open = False
            await e.control.page.update_async()

    page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Добро пожаловать !"),
        content=ft.Column([user_name], width=300, height=70, tight=True),
        actions=[ft.ElevatedButton(text="Войти в чат", on_click=join_chat_click)],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def route_change(e):
        page.views.clear()
        page.views.append(index.index(page))
        if "/mess" in page.route:
            page.views.append(mess.mess(page))
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


ft.app(main, view=ft.AppView.WEB_BROWSER)