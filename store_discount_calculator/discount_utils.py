def calcularDineroRecibido(T, D, C):
    discount_percentage = 0
    
    if D >= 0 and D < 2:
        discount_percentage = 0.2
    elif D >= 2 and D < 5:
        discount_percentage = 0.3
    elif D >= 5 and D < 7:
        discount_percentage = 0.45
    elif D >= 7 and D <= 8:
        discount_percentage = 0.6
    elif D == 9:
        discount_percentage = round(0)
    
    discount = T*discount_percentage
    total = T-discount
    bill = [C, 0 if discount_percentage == 0 else discount, total]
    print(*bill, sep=" ")
    return bill

def imprimirTotales(total_discounted, total_sold):
    print(f"El total de dinero descontado por almacén es: ${total_discounted}")
    print(f"El total de dinero recibido por ventas es: ${total_sold}")
