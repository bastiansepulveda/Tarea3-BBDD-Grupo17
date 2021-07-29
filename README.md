# Tarea3-BBDD-Grupo17

## Consideraciones.

1.- Seguimos las ideas presentadas en el Gitbook, tanto en el main como en models. \
2.- En las funciones update dejamos la posibilidad de actualizar uno o más atributos. \
3.- En la clase Usuario agregamos el atributo admin para que la interfaz sea coherente con la Tarea 2. El código asociado a esta inclusión es mostrado en [InformeTarea2](https://www.overleaf.com/read/kwpzfprrbtkd). \
4.- Se utilizó una función auxiliar en cada clase con clave primaria tipo *id* llamada **Last_id**. Esta función se encarga de obtener la última id registrada. Esto se realizó debido a que tuvimos problemas al insertar nuevos elementos en las tablas ya pobladas (como la BD de la Tarea 1). Por ende, explicitamos al momento de insertar que las id's tengan la forma *id = last_id + 1*. \
5.- Al momento de editar un usuario, no es posible cambiar la contraseña de la cuenta asociada. \
6.- Para las consultas 2, 4 y 5 tuvimos problemas con el Output del Postman, ya que los atributos flotantes no estan asociados a JSON. Por lo que cambiamos la propiedad tipo **Numeric** a **Double precision** de la columna *balance* en las tablas *Precio Moneda*, *Usuario Tiene Moneda* y *Cuenta Bancaria*. \
7.- La opción **VER** solo se encuentra en la tabla *USUARIO* dado que posee una gran cantidad de atributos. Para las otras tablas se muestran todos sus atributos de manera inmediata. \
8.- Modificamos el cambio de formato de el atributo *fecha* en la tabla Precio Moneda. En el método *json* que se define en la clase correspondiente se  agrega en el return **'fecha': self.fecha.strftime('%Y-%m-%d %H:%M:%S.%f')**. Esta modificación viene del hecho que cuando hacemos uso de la función *callAPI* se retorna, posteriormente, un formato no accesible para la obtención de los elementos de dicha tabla. \
9.- Queremos explicitar nuestros agredecimientos a este [blog](https://www.overleaf.com/read/kwpzfprrbtkd), ya que sin esa ayuda aún estaríamos en el barro. Por otro lado, se le agregó a la función **callAPI** el caso *DELETE*, para que la eliminación funcione correctamente. \ 
10.- Para encriptar la contraseña, añadimos la función **hash** con el método *ripemd160*, el cual tiene un tamaño de 40 caracteres. 

