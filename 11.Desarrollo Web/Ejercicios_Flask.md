                              EJERCICIOS DE FLASK

1.-Implementa una vista que reciba parámetros por URL
    La vista deberá recibir dos números a través de la URL y devolver la suma de ambos, formateado a string
    ejemplo: usando /sumar/100/200, la respuesta debería ser: "La suma de 100 y 200 es: 300"

2.-Implementa una vista que construya nombres de usuario
    En este caso, tendrás que implementar una vista que reciba el nombre y el apellido del usuario, y cree su nombre de usuario en minúsculas utilizando la primera letra del nombre, concatenada con el apellido (recuerda validar que los parámetros de entrada sean un string)
    ejemplo: usando /usuario/Maria/Martin devolverá mmartin

3.-Implementa una vista que reciba parámetros por GET
    Para este ejercicio, tendrás que implementar una vista que reciba un parámetro de consulta ?texto= en la URL y devuelva la cantidad de usuarios en la lista de usuarios dada (créate tú mismo un array con nombres ficticios), que contengan esa cadena de texto en sus nombres.
    ejemplo: /buscar_usuario?texto=ma devolverá “Se encontraron 2 usuarios que coinciden con la búsqueda: ma”