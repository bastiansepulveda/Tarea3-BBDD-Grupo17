<?php include $_SERVER['DOCUMENT_ROOT'].'/callAPI.php'; ?>

<?php

$id_usuario_delete = $_GET['id_usuario'];
$id_moneda_delete = $_GET['id_moneda'];

$result = callAPI('DELETE', 'http://127.0.0.1:5000/api/v1/utm/'.$id_usuario_delete.'&'.$id_moneda_delete, false);


echo '<script type="text/javascript">'; 
echo 'alert("Datos Borrados Correctamente");'; 
echo 'window.location.href = "/CRUD_tablas/utm.html";';
echo '</script>';

?>