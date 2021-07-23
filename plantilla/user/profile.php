<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php

/* Este archivo debe manejar la lógica para obtener la información del perfil */

//Se define el correo como aquel del usuario que ha iniciado sesión.
$email = $_SESSION['user'];
//Se realiza la consulta a la base de datos por los datos que se exhibirán en la página Perfil.
$consult = 
"SELECT usuario.nombre, usuario.apellido, usuario.correo, usuario.fecha_registro, pais.nombre_pais AS pais
FROM usuario
INNER JOIN pais 
ON pais.cod_pais = usuario.pais
WHERE correo = '$email'";
$result = pg_query($dbconn, $consult);

$datos = pg_fetch_assoc($result);

?>