
## Modulos

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import db.dbedit as dbe

# Ventana principal

root = Tk()
root.title("Cotizaciones")
root.geometry("900x1000+0+0")

# Disposición de ventana

# Definición de estilos

# style1 = ttk.Style()
# style1.configure("style1.TFrame", background="blue" )

# Definición de frames
titleFrame = ttk.Frame(root)
titleFrame.pack(padx=5, pady=5)

resultsFrame = ttk.Frame(root)
resultsFrame.pack(padx=5, pady=5)

dinResultsFrame = ttk.Frame(resultsFrame)

guideFrame = ttk.Frame(root)
guideFrame.pack(padx=10)

commandFrame = ttk.Frame(root)
commandFrame.pack(padx=5, pady=5)

# Widgets

titleLabel = ttk.Label(titleFrame, text = "Cotizaciones v1.0")
titleResults = ttk.Label(resultsFrame, text = "Resultados")
label = ttk.Label(resultsFrame, text="This is a ttk.Frame!")

resultsNotebook = ttk.Notebook(dinResultsFrame)


# View

titleLabel.pack()
titleResults.pack()
dinResultsFrame.pack(expand = True)
label.pack(pady=10)

# Main event loop para mostrar la ventana
root.mainloop()