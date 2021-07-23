<?php include $_SERVER['DOCUMENT_ROOT'].'/callAPI.php'; ?>

<?php

if($_SERVER['REQUEST_METHOD']=='POST'){
    $nombre = $_POST['name'];
    $apellido = $_POST['surname'];
    $correo = $_POST['email'];
    $contraseña = $_POST['pwd'];
    $pais = $_POST['pais'];

    $create_usuario = array(
        'nombre' => $nombre,
        'apellido' => $apellido,
        'correo' => $correo,
        'contraseña' => $contraseña,
        'pais' => $pais,
    );
    $result = callAPI('POST', 'http://127.0.0.1:5000/api/v1/usuario', json_encode($create_usuario));
}

echo '<script type="text/javascript">'; 
echo 'alert("Datos Ingresados Correctamente");'; 
echo 'window.location.href = "/CRUD_tablas/usuario.html";';
echo '</script>';

?>