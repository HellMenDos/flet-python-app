import flet as ft

def list_widget(): 
    return (ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    ))