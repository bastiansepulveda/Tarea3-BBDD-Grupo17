<?php include $_SERVER['DOCUMENT_ROOT'].'/callAPI.php'; ?>

<?php

$id_update = $_GET['id'];

if($_SERVER['REQUEST_METHOD']=='POST'){
    $nombre = $_POST['name'];
    $apellido = $_POST['surname'];
    $correo = $_POST['email'];
    $pais = $_POST['pais'];

    $update_usuario = array(
        'nombre' => $nombre,
        'apellido' => $apellido,
        'correo' => $correo,
        'pais' => $pais,
    );
    $result = callAPI('PUT', 'http://127.0.0.1:5000/api/v1/usuario/'.$id_update, json_encode($update_usuario));
}

echo '<script type="text/javascript">'; 
echo 'alert("Datos Ingresados Correctamente");'; 
echo 'window.location.href = "/CRUD_tablas/usuario.html";';
echo '</script>';

?>