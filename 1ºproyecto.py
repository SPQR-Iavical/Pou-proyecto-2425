A = int(input("Nivel de Fuerza: "))
B = input("Clase 1,2 Ó 3: ")
Primaria = "primaria"
Secundaria = "secundaria"
Tercera = "tercera"


if (A >= 1 and A <= 5):

    if (A == "1"): 
         print("es un objeto")
        
    elif(A == "2"):
        print("es debil")

    elif(A == "3"):
        print("fuerte")

    elif(A == "4"):
         print("bastante fuerte")
    if (B  == 1):
         print("es el SCP-5372")
    elif(B == 2):
        print("es el SCP-4967")
    elif(B == 3):
        print("el SCP-650-KO")

elif(A <= 6):
    print("muy alto, vuelve a intentarlo")

elif(A >= 0):
    print("muy bajo vuelve a intentarlo")