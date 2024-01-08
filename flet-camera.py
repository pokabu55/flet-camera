import flet as ft
import cv2
import base64
from datetime import datetime


class Cam:
    """カメラを扱うクラス"""

    def __init__(self):
        # OpenCVのカメラオブジェクトを作成
        self.cap = cv2.VideoCapture(0)
        self._is_capture = True

    def get_image(self):
        # カメラから画像を取得
        _, self.frame = self.cap.read()
        img = self._cv_to_base64(self.frame)
        return img

    def start_cam(self, e):
        """画像取得開始時の処理"""
        self._is_capture = True

    def end_cam(self, e):
        """画像取得終了時の処理"""
        self._is_capture = False

    def save_image(self, e):
        """画像を保存する"""
        filename = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
        cv2.imwrite(f"{filename}.jpg", self.frame)

    @property
    def is_capture(self) -> bool:
        """画像取得を行うかのフラグ
        Returns:
            bool: 画像取得を行う場合True
        """
        return self._is_capture

    def _cv_to_base64(self, img):
        _, encoded = cv2.imencode(".jpg", img)
        img_str = base64.b64encode(encoded).decode("ascii")
        return img_str

    def __del__(self):
        # カメラを終了
        self.cap.release()


def main(page: ft.Page):
    # 全体レイアウト
    page.window_max_width = 500
    page.window_max_height = 450
    page.title = "Camera App"
    # カメラを扱うインスタンスの定義
    camera = Cam()
    # ページ内のレイアウト
    image = ft.Image(
        src_base64=camera.get_image(),
        width=480,
        height=320,
        fit=ft.ImageFit.CONTAIN,
    )
    start_button = ft.TextButton("start", on_click=camera.start_cam)
    stop_button = ft.TextButton("stop", on_click=camera.end_cam)
    save_button = ft.TextButton("save", on_click=camera.save_image)
    row = ft.Row(spacing=0, controls=[start_button, stop_button, save_button])
    page.add(image)
    page.add(row)
    # 描写のループ
    while True:
        if camera.is_capture:
            img = camera.get_image()
            image.src_base64 = img
            page.update()


ft.app(target=main)
# ウェブアプリの場合
# ft.app(target=main, view=ft.WEB_BROWSER)
