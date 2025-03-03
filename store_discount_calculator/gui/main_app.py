from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Calculadora():
    def __init__(self):
        self.root = Tk()
        self.setup_ui()
        
    def setup_ui(self):
        # Se definen las variables que almacenaran los datos de la compra
        self.client_id = StringVar()
        self.client_name = StringVar()
        self.client_id_last_digit = IntVar()
        self.item_code = StringVar()
        self.item_price = DoubleVar()
        self.bill_total_discount = StringVar()
        self.bill_total = StringVar()
        
        # Se define el método para el llenado del ultimo dígito
        def fill_last_digit(event):
            if self.client_id.get():
                self.client_id_last_digit.set(self.client_id.get()[-1])
            else:
                self.client_id_last_digit.set("")
        
        # Se configura el titulo de la ventana
        self.root.title("Calculadora de descuento")
        
        #Se configura el area de Datos del cliente (Nombre, num de documento, ultimo dígito)
        labelframe1 = ttk.LabelFrame(self.root )
        labelframe1.config(text="Datos del cliente", padding="15 20")
        labelframe1.grid(row=0, column=0, padx=20, pady=20)
        
        ttk.Label(labelframe1, text="Número de Identificación*").grid(row=0, column=0, padx="20 5", pady="15")
        client_id_entry = ttk.Entry(labelframe1, textvariable=self.client_id)
        client_id_entry.grid(row=0, column=1)
        client_id_entry.bind("<FocusOut>", fill_last_digit)
        
        ttk.Label(labelframe1, text="Nombre*").grid(row=1, column=0, padx="20 5", pady="15")
        ttk.Entry(labelframe1, textvariable=self.client_name).grid(row=1, column=1)
        
        ttk.Label(labelframe1, text="Ultimo dígito").grid(row=0, column=2, padx="20 5")
        ttk.Entry(labelframe1, textvariable=self.client_id_last_digit, state=DISABLED).grid(row=0, column=3, padx="0 20")
        
        #Se configura el area de Datos de la compra (Código, descuento, valor a pagar)
        labelframe2 = ttk.LabelFrame(self.root, text="Datos de la compra", padding="20 20")
        labelframe2.grid(row=2, column=0, padx=20, pady=20)
        
        ttk.Label(labelframe2, text="Código de compra*").grid(row=1, column=0, padx="20 5", pady="15")
        ttk.Entry(labelframe2, textvariable=self.item_code).grid(row=1, column=1)
        
        ttk.Label(labelframe2, text="Valor de la compra*").grid(row=2, column=0, padx="20 5", pady="15")
        item_price_field = ttk.Entry(labelframe2, textvariable=self.item_price)
        item_price_field.grid(row=2, column=1)
        item_price_field.bind("<FocusOut>", self.calcular_descuento)
        
        ttk.Label(labelframe2, text="Total descuento").grid(row=3, column=0, padx="20 5", pady="15")
        bill_total_discount_field = ttk.Entry(labelframe2, textvariable=self.bill_total_discount, state=DISABLED)
        self.bill_total_discount.set("$0")
        bill_total_discount_field.grid(row=3, column=1)
        
        ttk.Label(labelframe2, text="Total a pagar").grid(row=4, column=0, padx="20 5", pady="15")
        bill_total_field = ttk.Entry(labelframe2, textvariable=self.bill_total, state=DISABLED)
        self.bill_total.set("$0")
        bill_total_field.grid(row=4, column=1)
        
        # Boton para registrar la compra
        ttk.Button(labelframe2, text="Registrar calculo", command=self.validate_fields).grid(row=2, column=2, padx="80 80")
        
    def show(self):
        self.root.mainloop()
        
    def calcular_descuento(self, event=None):
        
        last_digit = self.client_id_last_digit.get()
        original_price = self.item_price.get()
    
        if last_digit and original_price:
            
            discount_percentage = 0
            
            if last_digit >= 0 and last_digit < 2:
                discount_percentage = 0.2
            elif last_digit >= 2 and last_digit < 5:
                discount_percentage = 0.3
            elif last_digit >= 5 and last_digit < 7:
                discount_percentage = 0.45
            elif last_digit >= 7 and last_digit <= 8:
                discount_percentage = 0.6
            elif last_digit == 9:
                discount_percentage = 0
            
            discount = original_price*discount_percentage
            total = original_price-discount
            
            # Se actualiza el valor de los campos Total descuento y Total a pagar
            self.bill_total_discount.set(f"${discount}")
            self.bill_total.set(f"${total}")
        else:
            # Se actualiza el valor de los campos Total descuento y Total a pagar
            self.bill_total_discount.set(f"${0}")
            self.bill_total.set(f"${0}")

    def validate_fields(self):
        if self.client_id.get() and self.client_name.get() and self.item_code.get() and self.item_price.get():
            self.calcular_descuento()
            self.save_bill()
            messagebox.showinfo("ÉXITO", "El registro fue guardado exitosamente!.")
        else:
            messagebox.showerror("ERROR", "Debe llenar todos los campos marcados con asterisco.")
    
    def save_bill(self, path='sells_log.txt'):
        with open(path, 'a') as file:
            file.write(f'{self.client_id.get()} {self.client_name.get()} {self.item_code.get()} {self.item_price.get()} {self.client_id_last_digit.get()} {self.bill_total_discount.get()} {self.bill_total.get()} \n')
    
    def imprimir_totales(total_discounted, total_sold):
        print(f"El total de dinero descontado por almacén es: ${total_discounted}")
        print(f"El total de dinero recibido por ventas es: ${total_sold}")

def main():
    # Se inicializa la interfaz gráfica
    calculadora = Calculadora()
    calculadora.show()
    
if __name__ == "__main__":
    main()