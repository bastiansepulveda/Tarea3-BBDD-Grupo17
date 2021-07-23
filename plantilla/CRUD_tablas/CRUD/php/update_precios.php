<?php include $_SERVER['DOCUMENT_ROOT'].'/callAPI.php'; ?>

<?php

$id_update = $_GET['id'];

if($_SERVER['REQUEST_METHOD']=='POST'){
    $id_moneda = $_POST['id'];
    $valor = $_POST['valor'];

    $update_precios = array(
        'id_moneda' => $id_moneda,
        'valor' => $valor,
    );
    $result = callAPI('PUT', 'http://127.0.0.1:5000/api/v1/precio/'.$id_update, json_encode($update_precios));
}

echo '<script type="text/javascript">'; 
echo 'alert("Datos Ingresados Correctamente");'; 
echo 'window.location.href = "/CRUD_tablas/precio_moneda.html";';
echo '</script>';

?>