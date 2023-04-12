import turtle

def dibujar_figura(figura):
    t = turtle.Turtle()
    if figura == 'cuadrado':
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(100)
    elif figura == 'rectangulo':
        t.forward(200)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(200)
        t.right(90)
        t.forward(100)
    elif figura == 'triangulo':
        t.forward(100)
        t.right(120)
        t.forward(100)
        t.right(120)
        t.forward(100)
    elif figura == 'circulo':
        t.circle(50)
    else:
        print(f"No puedo dibujar la figura '{figura}'.")
        return
    
    turtle.mainloop()

print("Las figuras disponibles son: cuadrado, rectangulo, triangulo, circulo")
figura = input("Escriba el nombre de la figura que desea dibujar: ")
dibujar_figura(figura.lower())
