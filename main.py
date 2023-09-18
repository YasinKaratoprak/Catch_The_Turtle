import turtle
import time
import random

game_board = turtle.Screen()
game_board.bgcolor("#9aefd8")
game_board.title("Catch The Turtle!!!")
game_board.register_shape("turtle3.gif")

t = turtle.Turtle()
t.shape("turtle3.gif")

sayac_degeri = 0


def guncelle_sayac():
    turtle.penup()
    turtle.goto(0, 200)
    turtle.hideturtle()
    turtle.clear()
    turtle.write(f"Sayaç Değeri: {sayac_degeri}", align="center", font=("Arial", 24, "normal"))


def dokunma(x, y):
    global sayac_degeri
    turtle_x, turtle_y = t.position()
    tıklama_x, tıklama_y = turtle_x - x, turtle_y - y
    mesafe = ((tıklama_x ** 2) + (tıklama_y ** 2)) ** 0.5
    if mesafe < 30:
        sayac_degeri += 1
        guncelle_sayac()
    else:
        print("Olmadı")

timer_time = 20

def timer():
    global timer_time
    baslangic_zamani = time.time()
    while timer_time > 0:
        # Rastgele konuma git
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        t.penup()
        t.goto(x, y)
        t.pendown()

        # Geri sayım metni
        turtle.clear()
        turtle.penup()
        turtle.goto(0, 150)
        turtle.hideturtle()
        turtle.write(f"Kalan Süre: {timer_time} saniye\nToplam Sayım: {sayac_degeri}", align="center",
                     font=("Arial", 24, "normal"))

        time.sleep(0.1)  # 1 saniye bekle
        timer_time -= 1

    # Geri sayım tamamlandığında metni temizle
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 100)
    turtle.hideturtle()
    turtle.write(f"Süre Doldu! Toplam Sayım: {sayac_degeri}", align="center", font=("Arial", 24, "normal"))


# Dokunma işlevini etkinleştirin
turtle.onscreenclick(dokunma)

# Geri sayımı başlatın
timer()

if timer_time==0:
    if sayac_degeri >= 10:
        print("Kazandın")
        game_board.textinput("Kazandın","Kazandın")
        turtle.done()

    else:
        print("Kaybettin")
        game_board.textinput("Kaybettin","Kaybettin")
        turtle.done()

# Turtle ekranını kapatmak için bekleyin
turtle.done()
