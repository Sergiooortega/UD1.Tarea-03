from operaciones import sumar, restar, multiplicar, dividir
def mostrar_menu():
 print("\n=== CALCULADORA BÁSICA ===")
 print("1. Sumar")
 print("2. Restar")
 print("3. Multiplicar")
 print("4. Dividir")
 print("5. Salir")
def pedir_numero(mensaje):
 while True:
 try:
 return float(input(mensaje))
 except ValueError:
 print("Error: debes introducir un número válido.")
def main():
 while True:
 mostrar_menu()
 opcion = input("Elige una opción: ")
 if opcion == "1":
 a = pedir_numero("Introduce el primer número: ")
 b = pedir_numero("Introduce el segundo número: ")
 print(f"Resultado: {sumar(a, b)}")
 elif opcion == "2":
 a = pedir_numero("Introduce el primer número: ")
 b = pedir_numero("Introduce el segundo número: ")
 print(f"Resultado: {restar(a, b)}")
 elif opcion == "3":
 a = pedir_numero("Introduce el primer número: ")
 b = pedir_numero("Introduce el segundo número: ")
 print(f"Resultado: {multiplicar(a, b)}")
 elif opcion == "4":
 a = pedir_numero("Introduce el primer número: ")
 b = pedir_numero("Introduce el segundo número: ")
 try:
 print(f"Resultado: {dividir(a, b)}")
 except ValueError as e:
 print(f"Error: {e}")
 elif opcion == "5":
 print("Saliendo del programa...")
 break
 else:
 print("Opción no válida. Inténtalo de nuevo.")
if __name__ == "__main__":
 main()
