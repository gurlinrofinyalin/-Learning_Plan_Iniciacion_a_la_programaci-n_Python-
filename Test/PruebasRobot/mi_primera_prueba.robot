***Settings***
Library    OperatingSystem

***Test Cases***
Mi Primer Caso de Prueba
    Log To Console    Hola, Robot Framework!
    Create File    saludo.txt    Este es un archivo de prueba.
    File Should Exist    saludo.txt
    Remove File    saludo.txt
    File Should Not Exist    saludo.txt