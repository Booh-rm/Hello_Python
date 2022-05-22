

#Booh!



print("\n")
print("===========================================================================================")
print("                                 Dr. Dolittle - Pharmacy")
print("===========================================================================================")
print("\n")

list = []
list2 = []
list3 = []
cont = 1;

while True:
  print("Ingrese la opción deseada:\n1. Create prescription\n2. Print prescrition\n0. Exit")
  opcion = input("Ingrese la opción deseada: ")
  
  if opcion == "1":
    Patient = input("Patient name: ")

    while True:
        print("\n[T]ablet, [L]iquid, [I]njection:, e[X]it ")

        opcion=input()
        if opcion == "T":
            Medicine_Name = input("Medicine name: ")
            Weight = input("Weight (mg): ")
            Amount_tables = input("Amount of tables: ")
            Dosage = input("Dosage: ")

            list.append(["Tablet: "+ Medicine_Name, Weight + "mg", Amount_tables + " pills", Dosage])


        elif opcion == "L":
            Medicine_Name = input("Medicine name: ")
            suspention = input("Is suspention: Y/N ")
            if suspention == "Y":
                suspentionL="(suspention)"
            elif suspention == "N":
                suspentionL=""
            Amount = input("Amount (ml): ")
            Dosage = input("Dosage: ")

            list2.append(["Liquid: " + Medicine_Name, suspentionL, Amount + "ml", Dosage])

        elif opcion == "I":
            typet=0
            Medicine_Name = input("Medicine name: ")
            type = input("Type (0:Intravenous 1:Intramuscular): ")
            if type == "0":
                typet="(Intravenous)"
            elif type == "1":
                typet="(Intramuscular)"
            Amount_of_vials = input("Amount of vials: ")
            Dosage = input("Dosage: ")

            list3.append(["Injection; " + Medicine_Name, typet, Amount_of_vials, Dosage])

        elif opcion =="X":
            break


  elif opcion == "2":
    print("\n")
    print("===========================================================================================")
    print("                  Dr. Dolittle - Prescription")
    print("===========================================================================================")
    print("Patient: " + Patient)
    print("-------------------------------------------------------------------------------------------")
    for nombre in list:
        print(cont, nombre)
        cont += 1
    for nombre2 in list2:
        print(cont, nombre2)
        cont += 1
    for nombre3 in list3:
        print(cont, nombre3)
        cont += 1
    print("===========================================================================================")

    print("\n")

  elif opcion == "0":
    print("Gracias por visitar nuestra farmacia. ¡Vuelve pronto!\n")
    break

