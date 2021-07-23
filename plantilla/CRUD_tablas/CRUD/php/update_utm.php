<?php include $_SERVER['DOCUMENT_ROOT'].'/callAPI.php'; ?>

<?php

$id_usuario_update = $_GET['id_usuario'];
$id_moneda_update = $_GET['id_moneda'];

if($_SERVER['REQUEST_METHOD']=='POST'){
    $balance = $_POST['balance'];
    $update_utm = array(
        'balance' => $balance,
    );
    $result = callAPI('PUT', 'http://127.0.0.1:5000/api/v1/utm/'.$id_usuario_update.'&'.$id_moneda_update, json_encode($update_utm));
}

echo '<script type="text/javascript">'; 
echo 'alert("Datos Ingresados Correctamente");'; 
echo 'window.location.href = "/CRUD_tablas/utm.html";';
echo '</script>';

?>