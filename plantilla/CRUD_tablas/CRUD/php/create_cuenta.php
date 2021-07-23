<?php include $_SERVER['DOCUMENT_ROOT'].'/callAPI.php'; ?>

<?php

if($_SERVER['REQUEST_METHOD']=='POST'){
    $id_usuario = $_POST['id'];
    $balance = $_POST['balance'];
    $create_cuenta = array(
        'id_usuario' => $id_usuario,
        'balance' => $balance,
    );
    $result = callAPI('POST', 'http://127.0.0.1:5000/api/v1/cuenta_bancaria', json_encode($create_cuenta));
}

echo '<script type="text/javascript">'; 
echo 'alert("Datos Ingresados Correctamente");'; 
echo 'window.location.href = "/CRUD_tablas/cuenta_bancaria.html";';
echo '</script>';

?>