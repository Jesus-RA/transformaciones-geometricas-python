from tkinter import *
from transformaciones import *

class main:
    def __init__(self, master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.totalPoints = 0
        self.points = { 'x': [], 'y': [] }
        self.currentTransformationWidgets = {}
        self.penwidth = 3
        self.addMenu()
        self.setInitialButtons()

    def clear(self):
        self.c.delete(ALL)

    def drawCanvas(self):
        self.c = Canvas(self.master, width=400, height=300, bg=self.color_bg, highlightthickness=1, highlightbackground="black")
        self.c.grid(row = 4, column = 3)
    
    def hideCanvas(self):
        self.c.grid_forget()

    def draw(self, x0, y0, x1, y1):
        self.c.create_line(x0, y0, x1, y1, width=self.penwidth, fill=self.color_fg, smooth=True)

    def addMenu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Options',menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas',command=self.clear)
        optionmenu.add_command(label='Exit',command=self.master.destroy)

    def drawTransformationButtons(self):

        self.transformationButtons = {
            'traslation_button': Button(self.master, text = "Traslacion", command = self.traslation),
            'rotation_button': Button(self.master, text = "Rotacion", command = self.rotation),
            'scaling_button': Button(self.master, text = "Escalamiento", command = self.scaling),
            'rotation_with_arbitrary_pivot_button': Button(self.master, text = "Rotacion con punto arbitrario", command = self.rotation_with_arbitrary_pivot),
            'fixed_point_scaling_button': Button(self.master, text = "Escalamiento con punto fijo", command = self.fixed_point_scaling),
            'new_figure_button': Button(self.master, text = "Nueva figura", command = self.newFigure)
        }

        self.transformationButtons["traslation_button"].grid(row = 2, column = 0)
        self.transformationButtons["rotation_button"].grid(row = 2, column = 1)
        self.transformationButtons["scaling_button"].grid(row = 2, column = 2)
        self.transformationButtons["rotation_with_arbitrary_pivot_button"].grid(row = 3, column = 0)
        self.transformationButtons["fixed_point_scaling_button"].grid(row = 3, column = 1)
        self.transformationButtons["new_figure_button"].grid(row = 3, column = 2)

    def hideTransformationButtons(self):
        for widget in self.transformationButtons.values():
            widget.grid_forget()

    def newFigure(self):
        self.clearEarlierTransformationWidgets()
        self.hideCanvas()
        self.hideTransformationButtons()
        self.setInitialButtons()

    def traslation(self):
        self.clearEarlierTransformationWidgets()
        self.currentTransformationWidgets = {
            'tx_label': Label(self.master, text = "tx"),
            'tx_input': Entry(self.master, width = 10),
            'ty_label': Label(self.master, text = "ty"),
            'ty_input': Entry(self.master, width = 10)
        }
         
        self.currentTransformationWidgets['tx_label'].grid(row = 0, column = 0)
        self.currentTransformationWidgets['tx_input'].grid(row = 1, column = 0)

        self.currentTransformationWidgets['ty_label'].grid(row = 0, column = 1)
        self.currentTransformationWidgets['ty_input'].grid(row = 1, column = 1)

        def applyTransformation():
            tx = int(self.currentTransformationWidgets['tx_input'].get())
            ty = int(self.currentTransformationWidgets['ty_input'].get())
            
            for i in range(self.totalPoints):
                x = self.points['x'][i]
                y = self.points['y'][i]
                [xt, yt] = traslation([x, y], [tx, ty])
                self.points['x'][i] = xt
                self.points['y'][i] = yt

            self.drawFigure()

        self.currentTransformationWidgets['apply'] = Button(self.master, text = "Aplicar transformacion", command = applyTransformation)
        self.currentTransformationWidgets['apply'].grid(row = 1, column = 2)

    def rotation(self):
        self.clearEarlierTransformationWidgets()

        self.currentTransformationWidgets = {
            'label': Label(self.master, text = "Angulo de rotacion"),
            'angle_input': Entry(self.master, width = 10)
        }

        self.currentTransformationWidgets['label'].grid(row = 1, column = 0)
        self.currentTransformationWidgets['angle_input'].grid(row = 1, column = 1)

        def applyTransformation():
            angle = int(self.currentTransformationWidgets['angle_input'].get())
            for i in range(self.totalPoints):
                x = self.points['x'][i]
                y = self.points['y'][i]
                [rx, ry] = rotation([x, y], angle)
                self.points['x'][i] = rx
                self.points['y'][i] = ry

            self.drawFigure()

        self.currentTransformationWidgets['apply'] = Button(self.master, text = "Aplicar transformacion", command = applyTransformation)
        self.currentTransformationWidgets['apply'].grid(row = 1, column = 2)

    def scaling(self):
        self.clearEarlierTransformationWidgets()
        self.currentTransformationWidgets = {
            'sx_label': Label(self.master, text = "sx"),
            'sx_input': Entry(self.master, width = 10),
            'sy_label': Label(self.master, text = "sy"),
            'sy_input': Entry(self.master, width = 10)
        }
         
        self.currentTransformationWidgets['sx_label'].grid(row = 0, column = 0)
        self.currentTransformationWidgets['sx_input'].grid(row = 1, column = 0)

        self.currentTransformationWidgets['sy_label'].grid(row = 0, column = 1)
        self.currentTransformationWidgets['sy_input'].grid(row = 1, column = 1)

        def applyTransformation():
            sx = int(self.currentTransformationWidgets['sx_input'].get())
            sy = int(self.currentTransformationWidgets['sy_input'].get())
            
            for i in range(self.totalPoints):
                x = self.points['x'][i]
                y = self.points['y'][i]
                [xs, ys] = scaling([x, y], [sx, sy])
                self.points['x'][i] = xs
                self.points['y'][i] = ys

            self.drawFigure()

        self.currentTransformationWidgets['apply'] = Button(self.master, text = "Aplicar transformacion", command = applyTransformation)
        self.currentTransformationWidgets['apply'].grid(row = 1, column = 2)

    def rotation_with_arbitrary_pivot(self):
        self.clearEarlierTransformationWidgets()

        self.currentTransformationWidgets = {
            'xr_label': Label(self.master, text = "xr"),
            'xr_input': Entry(self.master, width = 10),
            'yr_label': Label(self.master, text = "yr"),
            'yr_input': Entry(self.master, width = 10),
            'angle_label': Label(self.master, text = "Angulo de rotacion"),
            'angle_input': Entry(self.master, width = 10),
        }
         
        self.currentTransformationWidgets['xr_label'].grid(row = 0, column = 0)
        self.currentTransformationWidgets['xr_input'].grid(row = 1, column = 0)

        self.currentTransformationWidgets['yr_label'].grid(row = 0, column = 1)
        self.currentTransformationWidgets['yr_input'].grid(row = 1, column = 1)

        self.currentTransformationWidgets['angle_label'].grid(row = 0, column = 2)
        self.currentTransformationWidgets['angle_input'].grid(row = 1, column = 2)

        def applyTransformation():
            xr = int(self.currentTransformationWidgets['xr_input'].get())
            yr = int(self.currentTransformationWidgets['yr_input'].get())
            angle = int(self.currentTransformationWidgets['angle_input'].get())
            
            for i in range(self.totalPoints):
                x = self.points['x'][i]
                y = self.points['y'][i]
                [rx, ry] = rotation_with_arbitrary_pivot([x, y], angle, [xr, yr])
                self.points['x'][i] = rx
                self.points['y'][i] = ry

            self.drawFigure()

        self.currentTransformationWidgets['apply'] = Button(self.master, text = "Aplicar transformacion", command = applyTransformation)
        self.currentTransformationWidgets['apply'].grid(row = 0, column = 3)

    def fixed_point_scaling(self):
        self.clearEarlierTransformationWidgets()
        self.currentTransformationWidgets = {
            'sx_label': Label(self.master, text = "sx"),
            'sx_input': Entry(self.master, width = 10),
            'sy_label': Label(self.master, text = "sy"),
            'sy_input': Entry(self.master, width = 10),
            'px_label': Label(self.master, text = "px"),
            'px_input': Entry(self.master, width = 10),
            'py_label': Label(self.master, text = "py"),
            'py_input': Entry(self.master, width = 10),
        }
         
        self.currentTransformationWidgets['sx_label'].grid(row = 0, column = 0)
        self.currentTransformationWidgets['sx_input'].grid(row = 1, column = 0)

        self.currentTransformationWidgets['sy_label'].grid(row = 0, column = 1)
        self.currentTransformationWidgets['sy_input'].grid(row = 1, column = 1)

        self.currentTransformationWidgets['px_label'].grid(row = 0, column = 2)
        self.currentTransformationWidgets['px_input'].grid(row = 1, column = 2)

        self.currentTransformationWidgets['py_label'].grid(row = 0, column = 3)
        self.currentTransformationWidgets['py_input'].grid(row = 1, column = 3)

        def applyTransformation():
            sx = int(self.currentTransformationWidgets['sx_input'].get())
            sy = int(self.currentTransformationWidgets['sy_input'].get())
            px = int(self.currentTransformationWidgets['px_input'].get())
            py = int(self.currentTransformationWidgets['py_input'].get())
            
            for i in range(self.totalPoints):
                x = self.points['x'][i]
                y = self.points['y'][i]
                [xs, ys] = fixed_point_scaling([x, y], [sx, sy], [px, py])
                self.points['x'][i] = xs
                self.points['y'][i] = ys

            self.drawFigure()

        self.currentTransformationWidgets['apply'] = Button(self.master, text = "Aplicar transformacion", command = applyTransformation)
        self.currentTransformationWidgets['apply'].grid(row = 2, column = 3)

    def clearEarlierTransformationWidgets(self):
        for widget in self.currentTransformationWidgets.values():
            widget.grid_forget()

    def setInitialButtons(self):

        self.initialButtons = {
            'points_label': Label(self.master, text = "Cuantos puntos tiene tu figura?"),
            'points_input': Entry(self.master, width = 10)            
        }

        def getFigureSize():
            self.totalPoints = int(self.initialButtons['points_input'].get())
            self.hideInitialButtons()
            self.requestPoints()

        self.initialButtons['accept_button'] = Button(self.master, text = "Aceptar", command = getFigureSize)
        
        self.initialButtons['points_label'].grid(row = 0, column = 0)
        self.initialButtons['points_input'].grid(row = 0, column = 1)
        self.initialButtons['accept_button'].grid(row = 0, column = 2)

    def hideInitialButtons(self):
        for widget in self.initialButtons.values():
            widget.grid_forget()

    def requestPoints(self):
        x = [None] * self.totalPoints
        y = [None] * self.totalPoints
        labels = [None] * self.totalPoints

        x_label = Label(self.master, text = "x")
        y_label = Label(self.master, text = "y")
        x_label.grid(row = 0, column = 1)
        y_label.grid(row = 0, column = 2)
        
        for point in range(self.totalPoints):
            x[point] = Entry(self.master, width = 10)
            y[point] = Entry(self.master, width = 10)
            labels[point] = Label(self.master, text = str(point))
            labels[point].grid(row = point + 1, column = 0)
            x[point].grid(row = point + 1, column = 1)
            y[point].grid(row = point + 1, column = 2)
        
        def setPoints():
            self.points['x'] = []
            self.points['y'] = []
            for point_x in x:
                self.points['x'].append(int(point_x.get()))
                point_x.grid_forget()

            for point_y in y:
                self.points['y'].append(int(point_y.get()))
                point_y.grid_forget()

            for label in labels:
                label.grid_forget()

            x_label.grid_forget()
            y_label.grid_forget()
            
            self.drawTransformationButtons()
            self.drawCanvas()
            self.drawFigure()
            graficar.grid_forget()

        graficar = Button(self.master, text = "Graficar", command = setPoints)
        graficar.grid(row = 1, column = 3)
    
    def drawFigure(self):
        x_points = self.points['x']
        y_points = self.points['y']
        for i in range(self.totalPoints - 1):
            self.draw(x_points[i], y_points[i], x_points[i+1], y_points[i+1])
        

if __name__ == '__main__':
    window = Tk()
    m = main(window)
    window.title('Transformaciones geometricas')
    window.geometry("1000x500")

    window.mainloop()