from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
import requests


def get_random_cat_url() -> str:
    json = requests.get("https://cataas.com/cat?json=true").json()
    cat_id: str = json["_id"]
    return f"https://cataas.com/cat/{cat_id}"


class MainView(BoxLayout):
    def get_new_image(self, _):
        self.cat_image.source = get_random_cat_url()

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.new_image_button: Button = Button(text="New Cat!", on_press=self.get_new_image)
        self.new_image_button.size_hint_y = 0.1
        self.new_image_button.

        self.cat_image: AsyncImage = AsyncImage()
        self.cat_image.source = get_random_cat_url()

        self.add_widget(self.new_image_button)
        self.add_widget(self.cat_image)


class Application(App):
    def build(self):
        return MainView()


if __name__ == '__main__':
    Application().run()