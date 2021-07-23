# Tarea3-BBDD-Grupo17

## Consideraciones.

1.- Seguimos las ideas presentadas en el Gitbook, tanto en el main como en models. \
2.- En las funciones update dejamos la posibilidad de actualizar uno o más atributos. \
3.- En la clase Usuario agregamos el atributo admin para que la interfaz sea coherente con la Tarea 2. El código asociado a esta inclusión es mostrado en [InformeTarea2](https://www.overleaf.com/read/kwpzfprrbtkd). \
4.- Se utilizó una función auxiliar en cada clase con clave primaria tipo *id* llamada **Last_id**. Esta función se encarga de obtener la última id registrada. Esto se realizó debido a que tuvimos problemas al insertar nuevos elementos en las tablas ya pobladas (como la BD de la Tarea 1). Por ende, explicitamos al momento de insertar que las id's tengan la forma *id = last_id + 1*.

