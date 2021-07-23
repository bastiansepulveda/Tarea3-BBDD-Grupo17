<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
//Obtenemos el id del usuario entregada en la url a través del método GET.
$id_delete = htmlspecialchars($_GET['id']);
//Realizamos la consulta para la eliminación del usuario.
$sql_delete = "DELETE FROM usuario WHERE id = $1";
$sql_delete2 = "DELETE FROM usuario_tiene_moneda WHERE id_usuario = $1";
$sql_delete3 = "DELETE FROM cuenta_bancaria WHERE id_usuario = $1";
//En el caso de eliminarse, se informa al usuario y se redirige a la pestaña Usuarios.
if(pg_query_params($dbconn, $sql_delete3, array($id_delete)) && pg_query_params($dbconn, $sql_delete2, array($id_delete)) && pg_query_params($dbconn, $sql_delete, array($id_delete))){
     echo '<script type="text/javascript">'; 
     echo 'alert("Eliminación Exitosa");'; 
     echo 'window.location.href = "/admin/users/all.html";';
     echo '</script>';
}
//En caso contrario, se muestra un mensaje indicando que no se pudo eliminar, y se devuelve a la pestaña Usuarios.
else{
     echo '<script type="text/javascript">'; 
     echo 'alert("Error al Eliminar");'; 
     echo 'window.location.href = "/admin/users/all.html";';
     echo '</script>';
}
?>