<?php include $_SERVER['DOCUMENT_ROOT'].'/callAPI.php'; ?>

<?php

if($_SERVER['REQUEST_METHOD']=='POST'){
    $id_moneda = $_POST['id'];
    $valor = $_POST['valor'];
    $create_precio = array(
        'id_moneda' => $id_moneda,
        'valor' => $valor,
    );
    $result = callAPI('POST', 'http://127.0.0.1:5000/api/v1/precio', json_encode($create_precio));
}

echo '<script type="text/javascript">'; 
echo 'alert("Datos Ingresados Correctamente");'; 
echo 'window.location.href = "/CRUD_tablas/precio_moneda.html";';
echo '</script>';

?>