from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

quiz_data = [
    {
        "question": "Bir jisim 10 m/s² tizlik bilen tizlenýär. \n Eger jisimiň massasy 2 kg bolsa, \n oňa täsir edýän güýç näçedir?",
        "options": ["12 N", "5 N", "8 N", "20 N"],
        "answer": 3
    },
    {
        "question": "Bir jisim 5 sekundda 20 m/s tizlige \n ýetýär. Tizlenmesi näçedir?",
        "options": ["2 m/s²", "5 m/s²", "10 m/s²", "4 m/s²"],
        "answer": 3
    },
    # goşmaça soraglar girizip bolýar
]

class ColoredBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        with self.canvas.before:
            Color(0.95, 0.95, 1, 1)  # Açyk gök fon
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class QuizWidget(ColoredBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.clear_widgets()
        q = quiz_data[self.index]

        self.add_widget(Label(
            text=q["question"],
            font_size='22sp',
            color=(0.2, 0.2, 0.5, 1),  # Gök ýazgy
            halign='center',
            size_hint_y=None,
            height=1000
        ))

        for i, option in enumerate(q["options"]):
            btn = Button(
                text=option,
                font_size='20sp',
                background_normal='',
                background_color=(0.3, 0.6, 0.9, 1),  # Açyk gök düwme
                color=(1, 1, 1, 1),  # Ak ýazgy
                size_hint_y=None,
                height=60
            )
            btn.bind(on_press=lambda instance, i=i: self.check_answer(i))
            self.add_widget(btn)

    def check_answer(self, selected):
        correct = quiz_data[self.index]["answer"]
        if selected == correct:
            self.score += 1
        self.index += 1
        if self.index < len(quiz_data):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.clear_widgets()
        self.add_widget(Label(
            text=f"Netije: {self.score} / {len(quiz_data)}",
            font_size='26sp',
            color=(0, 0.5, 0, 1),  # Ýaşyl ýazgy
            halign='center',
            size_hint_y=None,
            height=2000
        ))

class QuizApp(App):
    def build(self):
        return QuizWidget()

if __name__ == '__main__':
    QuizApp().run()