import flet as ft
from routes import index, mess
def main(page: ft.Page):
    page.title = "Messanger"

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


ft.app(main)