from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import pyrebase as pb


config= {
    'apiKey': "AIzaSyDQwmJyhiCQMhzJ8FZGhll5IlrtlqyO0Fk",
    'authDomain': "ee4953-a55aa.firebaseapp.com",
    'databaseURL': "https://ee4953-a55aa.firebaseio.com",
    'projectId': "ee4953-a55aa",
    'storageBucket': "ee4953-a55aa.appspot.com",
    'messagingSenderId': "574908749831",
    'appId': "1:574908749831:web:04f5f14daa0a0c57d632a2",
    'measurementId': "G-ZR9G23P5NQ"
}
firebase= pb.initialize_app(config)
storage= firebase.storage()
pathOnCloud= 'images/pic.jpg'


class Widgets(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.upload = Button(text='Upload', size_hint= (1, 0.2))
        self.upload.bind(on_release= self.Pressed)
        self.add_widget(self.upload)


    def Selected(self, filename):
        try:
            self.ids.image.source = filename[0]
            self.address= filename[0]
        except:
            pass
 

    def Pressed(self, instance):

        storage.child(pathOnCloud).put(self.address)
    

class ImagePicker(App):
    def build(self):
      return Widgets()


if __name__ == "__main__":
    window = ImagePicker()
    window.run()