<?php include $_SERVER['DOCUMENT_ROOT'].'/callAPI.php'; ?>

<?php

$id_update = $_GET['id'];
$id_update[10] = ': ';

$result = callAPI('DELETE', 'http://127.0.0.1:5000/api/v1/precio/'.$id_update, false);


echo '<script type="text/javascript">'; 
echo 'alert("Datos Borrados Correctamente");'; 
echo 'window.location.href = "/CRUD_tablas/precio_moneda.html";';
echo '</script>';

?>