import tkinter as tk
from tkinter import ttk, messagebox
from funciones import NUM_ALUMNOS, ASIGNATURAS, ASPECTOS, procesar_encuestas

class EncuestaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Evaluación de Asignaturas")
        self.root.geometry("900x700")
        
        # Variables
        self.encuestas = {asig: [] for asig in ASIGNATURAS}
        self.asignatura_actual = tk.StringVar(value=ASIGNATURAS[0])
        
        # Estilo
        style = ttk.Style()
        style.configure('TFrame', background='#f5f5f5')
        style.configure('TLabel', background='#f5f5f5')
        style.configure('Title.TLabel', font=('Arial', 11, 'bold'))
        
        # Contenedor principal
        main_frame = ttk.Frame(root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Panel superior
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(top_frame, text="Asignatura:", style='Title.TLabel').pack(side=tk.LEFT)
        ttk.Combobox(top_frame, textvariable=self.asignatura_actual, 
                    values=ASIGNATURAS, state="readonly", width=25).pack(side=tk.LEFT, padx=10)
        
        self.contador = ttk.Label(top_frame, text=f"Encuestas: 0/{NUM_ALUMNOS}", style='Title.TLabel')
        self.contador.pack(side=tk.LEFT)
        
        # Panel de entrada
        input_frame = ttk.LabelFrame(main_frame, text=" Ingresar Calificaciones (1-10) ", padding=15)
        input_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 15))
        
        self.entradas = []
        for aspecto in ASPECTOS:
            frame = ttk.Frame(input_frame)
            frame.pack(fill=tk.X, pady=5)
            ttk.Label(frame, text=aspecto, width=20).pack(side=tk.LEFT)
            entrada = ttk.Spinbox(frame, from_=1, to=10, width=5)
            entrada.pack(side=tk.RIGHT)
            self.entradas.append(entrada)
        
        ttk.Button(input_frame, text="Agregar", command=self.agregar_encuesta).pack(pady=(15, 5))
        
        # Panel de resultados
        self.result_frame = ttk.Frame(main_frame)
        self.result_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Botón de resultados
        ttk.Button(main_frame, text="Generar Reporte", 
                  command=self.mostrar_resultados).pack(pady=(15, 0))
    
    def agregar_encuesta(self):
        """Agrega una nueva evaluación"""
        asignatura = self.asignatura_actual.get()
        encuestas_asig = self.encuestas[asignatura]
        
        if len(encuestas_asig) >= NUM_ALUMNOS:
            messagebox.showinfo("Info", f"Máximo {NUM_ALUMNOS} encuestas por asignatura")
            return
        
        try:
            valores = [int(e.get()) for e in self.entradas]
            if any(not 1 <= v <= 10 for v in valores):
                raise ValueError("Las calificaciones deben ser entre 1 y 10")
            
            encuestas_asig.append(valores)
            self.contador.config(text=f"Encuestas ({asignatura}): {len(encuestas_asig)}/{NUM_ALUMNOS}")
            [e.set('') for e in self.entradas]
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def mostrar_resultados(self):
        """Muestra los resultados organizados"""
        if not any(len(e) > 0 for e in self.encuestas.values()):
            messagebox.showwarning("Advertencia", "No hay datos para mostrar")
            return
        
        # Limpiar frame de resultados
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        
        resultados = procesar_encuestas(self.encuestas)
        notebook = ttk.Notebook(self.result_frame)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        for asignatura in ASIGNATURAS:
            if not self.encuestas[asignatura]:
                continue
                
            tab = ttk.Frame(notebook, padding=10)
            notebook.add(tab, text=asignatura)
            
            # Mostrar total de la asignatura
            total_frame = ttk.Frame(tab)
            total_frame.pack(fill=tk.X, pady=(0, 10))
            ttk.Label(total_frame, 
                     text=f"TOTAL DE LA ASIGNATURA: {resultados[asignatura]['total_asignatura']} puntos",
                     font=('Arial', 10, 'bold')).pack()
            
            # Mostrar resultados por aspecto
            for aspecto in resultados[asignatura]['resultados']:
                frame = ttk.Frame(tab)
                frame.pack(fill=tk.X, pady=3)
                
                ttk.Label(frame, text=f"{aspecto['aspecto']}:", width=25, anchor='w').pack(side=tk.LEFT)
                ttk.Label(frame, 
                         text=f"Promedio: {aspecto['promedio']} | "
                              f"Excelentes: {aspecto['excelentes']} | "
                              f"Notas: {aspecto['notas']}").pack(side=tk.LEFT)

if __name__ == "__main__":
    root = tk.Tk()
    app = EncuestaApp(root)
    root.mainloop()