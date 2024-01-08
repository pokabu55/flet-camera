import flet as ft


class ImageViewer:
    def __init__(self, image_files):
        self.image_files = image_files
        self.current_index = 0

    def get_image(self):
        with open(self.image_files[self.current_index], "rb") as img_file:
            return ft.Image(src_base64=img_file.read())

    def next_image(self):
        if self.current_index < len(self.image_files) - 1:
            self.current_index += 1

    def prev_image(self):
        if self.current_index > 0:
            self.current_index -= 1


def main(page: ft.Page):
    # 画像ファイルのリストを定義します。ここでは仮のパスを使用しています。
    image_files = ["./images/01.jpg", "./images/02.jpg", "./images/03.jpg"]
    viewer = ImageViewer(image_files)

    image = viewer.get_image()
    next_button = ft.TextButton("Next", on_click=viewer.next_image)
    prev_button = ft.TextButton("Prev", on_click=viewer.prev_image)
    row = ft.Row(spacing=0, controls=[prev_button, next_button])

    page.add(image)
    page.add(row)

    while True:
        image.src_base64 = viewer.get_image().src_base64
        page.update()


ft.app(target=main)
