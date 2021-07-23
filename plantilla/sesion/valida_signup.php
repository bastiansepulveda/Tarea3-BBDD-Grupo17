<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
//Se obtiene la id del último usuario registrado, para crear al nuevo usuario con el sucesor de esta id.
$obt_id = 
"SELECT id
FROM usuario
ORDER BY id DESC
LIMIT 1";
$result = pg_query($dbconn, $obt_id);

$last_id = pg_fetch_assoc($result)['id'];
//Se fija la zona horaria con la hora local.
$zona = date_default_timezone_set('America/Santiago');

if($_SERVER['REQUEST_METHOD']=='POST'){
    //Se definen las variables con los datos obtenidos a través del método POST.
    $nombre = $_POST['name'];
    $apellido = $_POST['surname'];
    $correo = $_POST['email'];
    $contraseña = $_POST['pwd'];
    $contraseña2 = $_POST['pwd2'];
    $id_pais = $_POST['country'];
    $fecha = date('Y-m-d h:i:s');
    //Se crea la consulta para añadir al nuevo usuario en la base de datos.
    $sql_insert = 'INSERT INTO usuario (id, nombre, apellido, correo, contraseña, pais, fecha_registro, admin) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)';
    //Se crea la consulta para verificar si el correo ya está registrado.
    $get_correo = "SELECT correo FROM usuario WHERE correo = '$correo'";
    //Se verifica si el correo ya está registrado. En el caso de estarlo, se le señala a través de un mensaje.
    if(pg_num_rows(pg_query($get_correo))>0){
        echo 'El correo ya existe. Intente con otro.';
    }
    //Si no existe, entonces se procede a añadir al usuario a la base de datos.
    else{
    //Se verifica que las contraseñas proporcionadas coincidan.
        if($contraseña==$contraseña2){
        //Si los datos ingresados son correctos, se añaden a la base de datos y se informa a través de un mensaje. Se redirige a la página de inicio de sesión.
            if(pg_query_params($dbconn, $sql_insert, array($last_id+1, $nombre, $apellido, $correo, $contraseña, $id_pais, $fecha, 'false'))){
             echo '<script type="text/javascript">'; 
             echo 'alert("Datos Ingresados Correctamente");'; 
             echo 'window.location.href = "/sesion/log-in.html";';
             echo '</script>';
            }
            //Si existe algún error, se le informa a través de un mensaje y se devuelve a la página de registro.
            else{
             echo '<script type="text/javascript">'; 
             echo 'alert("Error al ingresar datos.");'; 
             echo 'window.location.href = "/sesion/sign-up.html";';
             echo '</script>';
            }
        }
        //Si las contraseñas no coincide, se informa a través de una alerta y se devuelve a la página de registro.
        else{
             echo '<script type="text/javascript">'; 
             echo 'alert("Las contraseñas no coinciden.");'; 
             echo 'window.location.href = "/sesion/sign-up.html";';
             echo '</script>';
        }
    }
}

?>