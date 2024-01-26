import flet as ft


def on_dialog_result(e: ft.FilePickerResultEvent):
    print("Selected files:", e.files)
    print("Selected file or directory:", e.path)


def main(page: ft.Page):
    # 全体レイアウト
    page.window_max_width = 640
    page.window_max_height = 480
    page.title = "Image Viewer"

    file_picker = ft.FilePicker(on_result=on_dialog_result)
    print(file_picker)

    pass


# desktop
ft.app(target=main)
