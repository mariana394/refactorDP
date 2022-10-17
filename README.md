# Building project locally
Install VirtualEnvironment (one time)

    >python -m pip install virtualenv

Create virtual environment

    >virtualenv virtual_project

1. This will create a virtual environment project folder and install python there.
2. This step can be skipped if you already have the folder locally.

Open virtual environment (Unix type OS)

    >source virtual_project/bin/activate

1. This will activate the virtual environment.  Yous should see `(virtual_project)` to the left of the terminal prompt.
2. This step will be needed each time.

Install requirements
    
    >python -m pip install -r requirements.txt

Install local src/ folder

    >python -m pip install -e src 

# Building Docker image
At the root of the project run

    >docker image build -t YOUR_NAME .

This will create a docker image using the `Dockerfile` with the image name `YOUR_NAME`

Run container

    >docker run YOUR_NAME

# IDENTIFICACIÓN DE PRINCIPIOS SOLID

1. Single Responsability Principle
    El primer principio SOLID identificado es el de "The single responsability principle". Este lo encontramos en el modulo
    de reportes porque es un modulo exclusivo para generacion de reportes y dentro de el mismo se encuentran las variaciones por formato. Sin embargo, el modulo se encarga unica y exclusivamente de los reportes por lo que podemos 
    confirmar que se esta haciendo uso del principio. Cada clase dentor del modulo esta exclusivamente enfocada en el formato para la que ha sido diseñada.

    Archivo: print_report.py

        Clase: TxtReport -> Es encargada del reporte en txt
        LOF: 4-54
        
        Clase: HTMLReport -> Es encargada del reporte en html
        LOF: 56-115

2. The Open Close Principle
    El segundo principio SOLID identificado es el de "The Open Close Principle". Este lo encontramos en el modulo de reporteo ya que este al no estar encapsulando los formatos de los reportes en una sola clase permite que se puedan tener otras clases que esten definidas para otros formatos, estando abierot a la extension, pero se sigue manteniendo la funcionalidad de generar reportes sin modificacion alguna. 
    
    Archivo: print_report.py

        Clase: TxtReport -> Es encargada del reporte en txt
        LOF: 4-54
        
        Clase: HTMLReport -> Es encargada del reporte en html
        LOF: 56-115

3. The Dependency Inversion Principle (DIP)
    El tercer principio SOLID identificado es el de "The Dependency Inversion Principle (DIP)". Este al ser un principio en donde los modulos de alto nivel no dependen de los modulos de bajo nivel sino que dependen de las abstracciones lo vemos implementado en el archivo command.py. En este caso el modulo de alto nivel es el comando, la abstraccion es el tipo de reporte (HTML, Txt) que el usuario desea obtener y los modulos de bajo nivel son cada una de las clases que permite que el reporte sea exportado en el formato deseado.

    Archivo: command.py

        Clase: createOneCommand
        LOF: 13-22

        Clase: createTwoCommand
        LOF: 24-38