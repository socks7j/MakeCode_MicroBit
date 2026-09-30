#PRACTICA 8

nota = 0

def on_button_pressed_a():
    global nota
    nota = randint(0, 100)
    basic.show_number(nota)
    basic.pause(1000)
    
    if nota < 51:
        basic.show_icon(IconNames.NO)
        basic.show_string("REPROBADO")
    else:
        basic.show_icon(IconNames.YES)
        basic.show_string("APROBADO")
    
    basic.pause(500)
    basic.clear_screen()

input.on_button_pressed(Button.A, on_button_pressed_a)
