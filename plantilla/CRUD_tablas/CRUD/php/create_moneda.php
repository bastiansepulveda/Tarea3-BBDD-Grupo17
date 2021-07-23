<?php include $_SERVER['DOCUMENT_ROOT'].'/callAPI.php'; ?>

<?php

if($_SERVER['REQUEST_METHOD']=='POST'){
    $sigla = $_POST['sigla'];
    $nombre = $_POST['nombre'];
    $create_moneda = array(
        'sigla' => $sigla,
        'nombre' => $nombre,
    );
    $result = callAPI('POST', 'http://127.0.0.1:5000/api/v1/moneda', json_encode($create_moneda));
}

echo '<script type="text/javascript">'; 
echo 'alert("Datos Ingresados Correctamente");'; 
echo 'window.location.href = "/CRUD_tablas/moneda.html";';
echo '</script>';

?>