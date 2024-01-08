import flet as ft


class ImageViewer:
    def __init__(self):
        self.image_file = ""

    def set_image(self, image_path):
        self.image_file = image_path

    def get_image(self):
        with open(self.image_file, "rb") as img_file:
            return ft.Image(src_base64=img_file.read())


def main(page: ft.Page):
    viewer = ImageViewer()

    image_path_input = ft.TextControl(placeholder="Enter image file path")
    set_image_button = ft.TextButton(
        "Set Image", on_click=lambda: viewer.set_image(image_path_input.value)
    )

    image = viewer.get_image()
    page.add(image)
    page.add(image_path_input)
    page.add(set_image_button)

    while True:
        if viewer.image_file:
            image.src_base64 = viewer.get_image().src_base64
        page.update()


ft.app(target=main)
