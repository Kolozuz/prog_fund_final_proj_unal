# from store_discount_calculator.discount_utils import *
from store_discount_calculator.gui import main_app

main_app.main()

# Programa principal
# n_clients = int(input())
    
# if n_clients == 0:
#     print("Se debe ingresar por lo menos un cliente")
# else:
#     total_discounted = 0
#     total_sold = 0
#     for client in range(n_clients):
#         T = float(input()) # Total comprado por el cliente
#         D = int(input()) # Ultimo digito del id del cliente
#         C = int(input()) # Codigo del producto comprado
#         client_bill = calcularDineroRecibido(T,D,C)
#         total_discounted += client_bill[1]
#         total_sold += client_bill[2]

#     imprimirTotales(total_discounted, total_sold)
