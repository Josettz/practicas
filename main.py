import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class OmniStoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OmniStore - Gestión de Inventario")
        self.root.geometry("600x650")
        self.root.config(bg="#f0f0f0")

        self.label_titulo = tk.Label(self.root, text="SISTEMA DE INVENTARIO", 
                                     font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#333")
        self.label_titulo.pack(pady=10)

        frame = tk.LabelFrame(self.root, text=" Registro de Producto ", font=("Arial", 10, "bold"), padx=20, pady=20)
        frame.pack(pady=10, padx=20, fill="x")

        tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_nombre = tk.Entry(frame, width=30)
        self.entry_nombre.grid(row=0, column=1, pady=5)
        self.entry_nombre.focus() 

        tk.Label(frame, text="Precio ($):").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_precio = tk.Entry(frame, width=30)
        self.entry_precio.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Stock:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_stock = tk.Entry(frame, width=30)
        self.entry_stock.grid(row=2, column=1, pady=5)

        self.btn_guardar = tk.Button(frame, text="GUARDAR PRODUCTO", command=self.agregar_producto,
                                     bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), cursor="hand2")
        self.btn_guardar.grid(row=3, columnspan=2, sticky="we", pady=15)

        self.tabla = ttk.Treeview(self.root, columns=("Precio", "Stock"), height=10)
        self.tabla.pack(pady=10, padx=20, fill="x")

        self.tabla.heading("#0", text="Nombre del Producto", anchor="center")
        self.tabla.heading("Precio", text="Precio Unitario", anchor="center")
        self.tabla.heading("Stock", text="Cant. Disponible", anchor="center")

        botonera = tk.Frame(self.root, bg="#f0f0f0")
        botonera.pack(pady=10)

        self.btn_eliminar = tk.Button(botonera, text="ELIMINAR SELECCIONADO", command=self.eliminar_producto,
                                      bg="#f44336", fg="white", font=("Arial", 9, "bold"), width=25)
        self.btn_eliminar.grid(row=0, column=0, padx=5)

        self.btn_limpiar = tk.Button(botonera, text="LIMPIAR TABLA", command=self.limpiar_tabla,
                                     bg="#2196F3", fg="white", font=("Arial", 9, "bold"), width=25)
        self.btn_limpiar.grid(row=0, column=1, padx=5)


    def validar_formulario(self):
        """Verifica que los datos sean correctos antes de procesar"""
        if len(self.entry_nombre.get()) == 0:
            messagebox.showwarning("Faltan datos", "El nombre del producto es obligatorio")
            return False
        try:
            float(self.entry_precio.get())
            int(self.entry_stock.get())
            return True
        except ValueError:
            messagebox.showerror("Error de Formato", "Precio debe ser número y Stock debe ser entero")
            return False

    def agregar_producto(self):
        if self.validar_formulario():
            nombre = self.entry_nombre.get()
            precio = self.entry_precio.get()
            stock = self.entry_stock.get()
            
            self.tabla.insert("", "end", text=nombre, values=(f"${precio}", stock))
            
            self.entry_nombre.delete(0, tk.END)
            self.entry_precio.delete(0, tk.END)
            self.entry_stock.delete(0, tk.END)
            self.entry_nombre.focus()
            messagebox.showinfo("Éxito", f"'{nombre}' ha sido registrado")

    def eliminar_producto(self):
        seleccion = self.tabla.selection()
        if seleccion:
            item_nombre = self.tabla.item(seleccion)['text']
            confirmar = messagebox.askyesno("Confirmar", f"¿Seguro que quieres eliminar '{item_nombre}'?")
            if confirmar:
                self.tabla.delete(seleccion)
        else:
            messagebox.showwarning("Atención", "Selecciona un producto de la tabla primero")

    def limpiar_tabla(self):
        if messagebox.askyesnocancel("Limpiar todo", "¿Deseas borrar TODOS los productos de la lista?"):
            for item in self.tabla.get_children():
                self.tabla.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = OmniStoreApp(root)
    root.mainloop()