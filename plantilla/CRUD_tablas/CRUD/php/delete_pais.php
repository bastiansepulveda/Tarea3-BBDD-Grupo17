<?php include $_SERVER['DOCUMENT_ROOT'].'/callAPI.php'; ?>

<?php

$id_update = $_GET['id'];

$result = callAPI('DELETE', 'http://127.0.0.1:5000/api/v1/pais/'.$id_update, false);


echo '<script type="text/javascript">'; 
echo 'alert("Datos Borrados Correctamente");'; 
echo 'window.location.href = "/CRUD_tablas/pais.html";';
echo '</script>';

?>