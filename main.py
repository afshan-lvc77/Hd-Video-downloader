from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import platform

# Android permissions mangne ke liye (Zaroori hai)
if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE, Permission.INTERNET])

class DownloaderScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical')
        
        # Top Bar
        self.toolbar = MDTopAppBar(title="SMV Downloader")
        self.toolbar.elevation = 4
        layout.add_widget(self.toolbar)
        
        # Content Layout
        content = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.label = MDLabel(
            text="Welcome to SMV Downloader",
            halign="center",
            theme_text_color="Secondary",
            font_style="H5"
        )
        content.add_widget(self.label)
        
        # URL Input
        self.url_input = MDTextField(
            hint_text="Paste Video URL Here",
            mode="rectangle",
            icon_right="link-variant"
        )
        content.add_widget(self.url_input)
        
        # Download Button
        self.btn = MDRaisedButton(
            text="DOWNLOAD NOW",
            pos_hint={"center_x": .5},
            on_release=self.start_download
        )
        content.add_widget(self.btn)
        
        layout.add_widget(content)
        self.add_widget(layout)

    def start_download(self, instance):
        url = self.url_input.text
        if url:
            self.label.text = "Starting Download..."
            # Yahan tum apna actual download logic (yt-dlp etc) baad mein add kar sakte ho
        else:
            self.label.text = "Please enter a valid URL!"

class SMVDownloader(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"  # App ka color theme
        self.theme_cls.theme_style = "Light"
        return DownloaderScreen()

if __name__ == "__main__":
    Hd video Downloader().run()

