from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

from datetime import datetime


# ================= ANDROID SAFE MODE =================

arduino = None
connected = False


# ================= STATE =================

distance = "--"
alive = 2


# ================= APP =================

class FeederUI(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.padding = 20
        self.spacing = 10

        with self.canvas.before:
            Color(0.05, 0.07, 0.12, 1)
            self.bg = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_bg, pos=self._update_bg)


        # TITLE
        self.title = Label(
            text="SMART FISH FEEDER SYSTEM",
            font_size=22,
            bold=True
        )
        self.add_widget(self.title)


        # STATUS
        self.status = Label(
            text="STARTING...",
            font_size=18
        )
        self.add_widget(self.status)


        # CLOCK
        self.clock = Label(
            text="",
            font_size=18
        )
        self.add_widget(self.clock)


        # TIMER
        self.timer = Label(
            text="00:00:00",
            font_size=40,
            bold=True
        )
        self.add_widget(self.timer)


        # DISTANCE
        self.distance_lbl = Label(
            text="Distance: -- cm"
        )
        self.add_widget(self.distance_lbl)


        # FEED BUTTON
        self.feed_btn = Button(
            text="FEED NOW",
            font_size=20,
            background_color=(0,1,1,1)
        )

        self.feed_btn.bind(
            on_press=self.show_passcode
        )

        self.add_widget(self.feed_btn)


        Clock.schedule_interval(
            self.update_ui,
            1
        )


    def _update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos



    # ================= PASSWORD =================

    def show_passcode(self, instance):

        layout = BoxLayout(
            orientation="vertical"
        )


        self.pass_input = TextInput(
            password=True,
            hint_text="Enter passcode"
        )


        btn = Button(
            text="CONFIRM"
        )


        layout.add_widget(
            self.pass_input
        )

        layout.add_widget(
            btn
        )


        popup = Popup(
            title="Security Check",
            content=layout,
            size_hint=(0.7,0.4)
        )


        def check(instance):

            if self.pass_input.text == "9876":

                self.send_feed()

            else:

                self.status.text = "WRONG PASSCODE ❌"


            popup.dismiss()


        btn.bind(
            on_press=check
        )


        popup.open()



    # ================= FEED =================

    def send_feed(self):

        # Android safe simulation
        self.status.text = "FEED SENT ⚡"



    # ================= LOOP =================

    def update_ui(self, dt):

        now = datetime.now()


        self.clock.text = now.strftime(
            "%H:%M:%S | %Y-%m-%d"
        )


        # 12 hour countdown

        sec = (
            now.hour * 3600 +
            now.minute * 60 +
            now.second
        )


        feed_time = 12 * 3600


        if sec < feed_time:
            remaining = feed_time - sec
        else:
            remaining = (24*3600) - sec + feed_time



        h = remaining // 3600
        m = (remaining % 3600) // 60
        s = remaining % 60


        self.timer.text = (
            f"{h:02}:{m:02}:{s:02}"
        )


        self.distance_lbl.text = (
            f"Distance: {distance} cm"
        )


        self.status.text = (
            "OFFLINE MODE 🔌"
        )



class FeederApp(App):

    def build(self):
        return FeederUI()



FeederApp().run()