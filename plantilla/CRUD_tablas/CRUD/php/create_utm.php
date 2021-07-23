<?php include $_SERVER['DOCUMENT_ROOT'].'/callAPI.php'; ?>

<?php

if($_SERVER['REQUEST_METHOD']=='POST'){
    $id_usuario = $_POST['id_usuario'];
    $id_moneda = $_POST['id_moneda'];
    $balance = $_POST['balance'];
    $create_utm = array(
        'id_usuario' => $id_usuario,
        'id_moneda' => $id_moneda,
        'balance' => $balance,
    );
    $result = callAPI('POST', 'http://127.0.0.1:5000/api/v1/utm', json_encode($create_utm));
}

echo '<script type="text/javascript">'; 
echo 'alert("Datos Ingresados Correctamente");'; 
echo 'window.location.href = "/CRUD_tablas/utm.html";';
echo '</script>';

?>