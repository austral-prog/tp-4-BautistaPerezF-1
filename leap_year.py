def leap_year():
    
     año = int(input("Ingrese un año: "))
     if (año % 4 == 0 and año % 100 != 0)  or (año % 400 == 0):
         return (f"El año {año} es biciesto")
     else:
         return (f"El año {año} no es biciesto")
