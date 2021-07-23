<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
//Obtenemos el id del usuario entregada en la url a través del método GET.
$id_update = htmlspecialchars($_GET['id']); 

if($_SERVER['REQUEST_METHOD']=='POST'){
    //Obtenemos todos los datos recibidos a través del método POST.
    $nombre = $_POST['name'];
    $apellido = $_POST['surname'];
    $correo = $_POST['email'];
    $contraseña = $_POST['pwd'];
    $id_pais = $_POST['country'];
    $fecha = date('a, Y-m-d h:i:s');
    //Realizamos la consulta para modificar los datos del respectivo usuario.
    $sql_update =
    "UPDATE usuario
    SET nombre=$1, apellido=$2, correo=$3, contraseña=$4, pais=$5
    WHERE id = $6";
    //Verificamos si existe algún usuario, distinto de aquel que se está editando, que posea el mismo correo.
    $get_correo = "SELECT correo FROM usuario WHERE correo = '$correo' and id <> $id_update";
    //En caso de existir, se informa que el correo ya existe y se solicita volver a intentarlo.
     if(pg_num_rows(pg_query($get_correo))>0){
         echo '<script type="text/javascript">'; 
         echo 'alert("El correo ya existe. Intente con otro.");'; 
         echo 'window.location.href = "/admin/users/update.html?id='.$id_update.'"';
         echo '</script>';
     }
     //En caso de no existir, se procede con la edición del usuario.
    else{
    //Si se ejecuta la edición de manera satisfactoria, se informa a través de un mensaje y se redirige a la pestaña Usuarios.
    if(pg_query_params($dbconn, $sql_update, array($nombre, $apellido, $correo, $contraseña, $id_pais,$id_update))){    
             echo '<script type="text/javascript">'; 
             echo 'alert("Datos Ingresados Correctamente");'; 
             echo 'window.location.href = "/admin/users/all.html";';
             echo '</script>';
    }
    //Si existe algún error al editar, se informa y se redirige a la pestaña de edición.
    else{
         echo '<script type="text/javascript">'; 
         echo 'alert("Error al Ingresar Datos");'; 
         echo 'window.location.href = "/admin/users/update.html?id='.$id_update.'"';
         echo '</script>';
    }
    
    }
}

?>