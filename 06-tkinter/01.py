import tkinter

canvas = tkinter.Canvas()   # vytvorenie plátna a jeho priradenie do premennej canvas
canvas.pack()   # umiestnenie plátna do okna

canvas.create_text(100, 75, text='Ahoj')
# vypíše text 'Ahoj' na pozícii x=100, y=100
# súradnice zadaávame vždy v poradí x,y
# x rastie smerom doprava
# y rastie smerom dole

canvas.create_rectangle(50, 50, 150, 100)
# vykreslenie štvorca (obdĺžnika)
# prvé dve čísla určujú pozíciu začiatočného bodu
# dalšie dve určujú pozíciu koncového bodu

canvas.create_oval(50, 50, 150, 100)
# vykreslenie kruhu (oválu)
# prvé dve čísla určujú pozíciu začiatočného bodu
# dalšie dve určujú pozíciu koncového bodu

tkinter.mainloop() # aby zostalo okno otvorené, aby sa nezavrelo