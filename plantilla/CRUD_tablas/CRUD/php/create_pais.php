<?php include $_SERVER['DOCUMENT_ROOT'].'/callAPI.php'; ?>

<?php

if($_SERVER['REQUEST_METHOD']=='POST'){
    $nombre = $_POST['name'];
    $update_nombre = array(
        'nombre' => $nombre,
    );
    $result = callAPI('POST', 'http://127.0.0.1:5000/api/v1/pais', json_encode($update_nombre));
}

echo '<script type="text/javascript">'; 
echo 'alert("Datos Ingresados Correctamente");'; 
echo 'window.location.href = "/CRUD_tablas/pais.html";';
echo '</script>';

?>