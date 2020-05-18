from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
import random


Config.set('graphics','resizable','0')
Config.set('graphics','width','400')
Config.set('graphics','height','650')



def calc3(a, b, c, d, y):
    def fit(x):
        global result
        delta = [abs(a * x[i][0] + b * x[i][1] + c * x[i][2] + d * x[i][3] - y) for i in range(len(x))]
        k = 0
        for i in range(len(delta)):
            try:
                k += 1 / delta[i]
            except:
                result = x[i]
                return 0
        return [round((1 / n) / k * 100) for n in delta]

    def nextpopulation(p, f):
        x = []
        for i in range(len(p)):
            x.extend([p[i]] * f[i])
        parents = [random.sample(x, 2) for i in range(len(p))]
        nextp = []
        for n in parents:
            part = random.randint(1, 3)
            mp = random.randint(0, 1)
            nextp.append(n[mp][:part] + n[1 - mp][part:])
        return nextp
    def mutation(p):
        for n in p:
            n[random.randint(0,3)]=random.randint(1,y)
        return p

    population = [[random.randint(1, y - 3) for i in range(4)] for i in range(10)]
    while True:
        fitness = fit(population)
        if fitness == 0:
            return result
            break
        population1 = nextpopulation(population, fitness)
        if population == population1:
            population=mutation(population)
        else:
            population=population1

    return 0





class MyApp(App):
    def build(self):
        f1 = FloatLayout()


        self.input1 = TextInput(font_size = 20,
                                background_normal='',
                                size_hint=(0.5, 0.05),
                                pos=(400 * 0.25, 650 * 0.7)
                                )
        self.input2 = TextInput(font_size=20,
                                background_normal='',
                                size_hint=(0.5, 0.05),
                                pos=(400 * 0.25, 650 * 0.64)
                                )
        self.input3 = TextInput(font_size = 20,
                                background_normal='',
                                size_hint=(0.5, 0.05),
                                pos=(400 * 0.25, 650 * 0.58)
                                )
        self.input4 = TextInput(font_size=20,
                                background_normal='',
                                size_hint=(0.5, 0.05),
                                pos=(400 * 0.25, 650 * 0.52)
                                )
        self.input5 = TextInput(font_size=20,
                                background_normal='',
                                size_hint=(0.5, 0.05),
                                pos=(400 * 0.25, 650 * 0.46)
                                )

        f1.add_widget(self.input1)
        f1.add_widget(self.input2)
        f1.add_widget(self.input3)
        f1.add_widget(self.input4)
        f1.add_widget(self.input5)

        f1.add_widget(Button(text='Calculate',
                            font_size = 30,
                            on_press=self.calculate,
                            background_normal = '',
                            background_color = [1,0,0,1],
                            size_hint = (0.35,0.1),
                            pos = (400*0.34,650*0.35)))

        bl = BoxLayout(orientation='vertical',
                        size_hint = (0.5,0.25),
                            pos = (400*0.25,650*0.15))
        self.result = Label(text='', bold=True)

        self.message_out = Label(text='', bold=True)


        bl.add_widget(self.result)

        bl.add_widget(self.message_out)
        f1.add_widget(bl)

        return f1


    def calculate(self, instance):
        try:
            a,b,c,d,y = int(self.input1.text),int(self.input2.text),int(self.input3.text),int(self.input4.text),int(self.input5.text)
            result = calc3(a,b,c,d,y)


            if (result):
                self.result.text, self.message_out.text = f'Result: {result}', 'SUCCESSFULLY'

            else:
                self.message_out.text = f''
                self.first_num.text, self.second_num.text = '',''
        except:
            self.message_out.text = 'Incorrect input'
            self.result.text = ''



if __name__ == '__main__':
    MyApp().run()