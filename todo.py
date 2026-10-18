import os
runProgram = True
todoList = []  # Lista para almacenar las tareas
#Función para mostrar todas las opciones del menú´
def showMenuOptions():
    print("")
    print("")
    print("Por favor, seleccione una opción:")
    print("")
    print("")
    print("1. Crear una nueva tarea")
    print("2. Marcar tarea como completada")
    print("3. Borrar tarea")
    print("4. Salir")
    
#Función para mostrar todas las tareas
def showTodoList():
    global todoList
    print("")
    print("")
    print("********************************")
    for todo in todoList:
        print(f"{todoList.index(todo) + 1}. {todo}")
    print("********************************")
    print("")
    print("")  

#Función para guardar las tareas en la variable todoList
def createTodo():
    os.system("cls") #Limpiar la pantalla
    global todoList
    print("Crear una nueva tarea")
    todo = input("Por favor, ingrese la descripción de la tarea: ") 
    todoList.append(todo)
    #Mostrar la lista de tareas.
    showTodoList()
   
#Función para marcar una tarea como realizada
def updateTodo():
    global todoList
    print("Actualizar una tarea")
    todoId = int(input("Por favor, ingrese el número de la tarea que desea actualizar: "))
    todoList[todoId - 1] = todoList[todoId - 1] + " (Completada)"
    showTodoList()

#Función para borrar una tarea
def deleteTodo():
    global todoList
    print("Borrar una tarea")
    todoId = int(input("Por favor, ingrese el número de la tarea que desea borrar: "))
    del todoList[todoId - 1]
    showTodoList()

#Función principal del programa
def main():
    global runProgram
    print("Bienvenido a la Aplicación de Tareas")
    flag = True

    while runProgram:
        while flag:
            showMenuOptions() #aquí invocamos la función para mostrar las opciones del menú
            option = int(input("Ingrese una opción (1-4): "))
            
            match option:
                case 1: 
                    createTodo()
                case 2:
                    updateTodo()
                case 3:
                    deleteTodo()
                case 4:
                    print("Saliendo de la aplicación...")
                    runProgram = False
                    flag = False
                case _:
                    print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()