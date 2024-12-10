#Se declaran todas las variables en inglés para generalizar el programa

name = str(input("Ingrese su nombre: \n"))
age = int(input("Ingrese su edad: \n"))
title = str(input("Ingrese su cargo: \n")).lower()
exp_years = int(input("Ingrese sus años de experiencia: \n"))
base_salary = float(input("Ingrese su salario base: \n"))

if age < 18 or age > 65:
    print("No es elegible para bonificaciones")

elif title == "gerente":
    if exp_years > 5:
        bonification = base_salary * 0.20
    elif exp_years >= 3 and exp_years <= 5:
        bonification = base_salary * 0.15
    else:
        bonification = base_salary * 0.10

elif title == "analista":
    if exp_years > 5:
        bonification = base_salary * 0.15
    elif exp_years >= 3 and exp_years <= 5:
        bonification = base_salary * 0.10
    else:
        bonification = base_salary * 0.05

elif title == "asistente":
    if exp_years > 5:
        bonification = base_salary * 0.10
    elif exp_years >= 3 and exp_years <= 5:
        bonification = base_salary * 0.05
    else:
        bonification = base_salary * 0.02

else:
    print("No es elegible para bonificaciones")


print("Nombre del empleado: ", name)
print("Cargo: ", title)
print("Anhos de experiencia: ", exp_years)
print("Salario base: ", base_salary)
print("Bonificación: ", bonification)
print("Monto final con impuestos: ", base_salary + bonification)




