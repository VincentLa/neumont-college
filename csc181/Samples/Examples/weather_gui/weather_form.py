from tkinter import *
import weather
from datetime import datetime

def weather_update():

    weather_form = Tk()
    weather_form.title("Weather Update")
    weather_form.geometry("300x200")

    def update_data():

        title = Label(weather_form, text=f'Weather Update: {datetime.now().strftime("%m/%d/%Y %H:%M:%S")}', height=2)
        title.grid(row=0, column=0)

        # Scrape the Weather
        weather_list = weather.get_weather()
        # print(weather_list)

        # Show weather on form
        for counter, item in enumerate(weather_list):
            Label(weather_form, text=item).grid(row=counter+1, column=0, sticky=W, padx=5)


    def loop():
        update_data()
        weather_form.after(5000, loop)
        
    weather_form.after(0, loop)
    weather_form.mainloop()


if __name__ == '__main__':
    weather_update()
