<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php

//Obtenemos la id del último usuario ingresado, que será la id más alta, 
//para crear al nuevo usuario con el sucesor de esta id.

$obt_id = 
"SELECT id
FROM usuario
ORDER BY id DESC
LIMIT 1";
$result = pg_query($dbconn, $obt_id);

$last_id = pg_fetch_assoc($result)['id'];

//Fijamos la zona horaria con la hora local.
$zona = date_default_timezone_set('America/Santiago');

if($_SERVER['REQUEST_METHOD']=='POST'){
    //Obtenemos todos los datos recibidos a través del método POST.
    $nombre = $_POST['name'];
    $apellido = $_POST['surname'];
    $correo = $_POST['email'];
    $contraseña = $_POST['pwd'];
    $id_pais = $_POST['country'];
    $fecha = date('Y-m-d h:i:s');
    //Consultamos por el correo ingresado, para verificar si ya existe algún usuario con este email.
    $get_correo = "SELECT correo FROM usuario WHERE correo = '$correo'";
    $sql = 'INSERT INTO usuario (id, nombre, apellido, correo, contraseña, pais, fecha_registro, admin) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)';
    //Verificamos si existe algún usuario con el correo ingresado. En caso afirmativo, se señala que ya existe y se devuelve a la página de creación.
    if(pg_num_rows(pg_query($get_correo))>0){
         echo '<script type="text/javascript">'; 
         echo 'alert("El correo ya existe. Intente con otro.");'; 
         echo 'window.location.href = "/admin/users/create.html";';
         echo '</script>';}
     //De no existir el correo, se procede con la creación del usuario.   
    else{
    //Se crea el usuario.
    if(pg_query_params($dbconn, $sql, array($last_id+1, $nombre, $apellido, $correo, $contraseña, $id_pais, $fecha, 'false'))){
         echo '<script type="text/javascript">'; 
         echo 'alert("Usuario Creado Correctamente");'; 
         echo 'window.location.href = "/admin/users/all.html";';
         echo '</script>';
    }
    //En el caso de ingresar algún dato de manera errónea, se le señala al usuario y se devuelve a la página de creación.
    else{
       echo '<script type="text/javascript">'; 
       echo 'alert("Error al ingresar los datos.");'; 
       echo 'window.location.href = "/admin/users/create.html";';
       echo '</script>';
    }

  
    }
}

?>