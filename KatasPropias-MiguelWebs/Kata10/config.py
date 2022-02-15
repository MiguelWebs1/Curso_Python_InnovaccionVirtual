def main():
    try:
        configuration = open('config.txt','r')
    except FileNotFoundError:
        print("No puedo encontrar el archivo config.txt")
    except IsADirectoryError:
        print("Encontre config.txt pero es un directorio, no puedo leerlo")
    except (BlockingIOError, TimeoutError):
        print("No tengo permisos para leer el archivo config.txt")

if __name__ == '__main__':
    main()
    


