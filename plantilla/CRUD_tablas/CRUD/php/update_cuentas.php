<?php include $_SERVER['DOCUMENT_ROOT'].'/callAPI.php'; ?>

<?php

$id_update = $_GET['id'];

if($_SERVER['REQUEST_METHOD']=='POST'){
    $balance = $_POST['balance'];
    $update_cuenta = array(
        'balance' => $balance,
    );
    $result = callAPI('PUT', 'http://127.0.0.1:5000/api/v1/cuenta_bancaria/'.$id_update, json_encode($update_cuenta));
}

echo '<script type="text/javascript">'; 
echo 'alert("Datos Ingresados Correctamente");'; 
echo 'window.location.href = "/CRUD_tablas/cuenta_bancaria.html";';
echo '</script>';

?>