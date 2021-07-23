<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
//Realizamos la consulta con los datos que se deben mostrar en pantalla, 
//y los ordenamos por el id de forma ascendente.

$consult = 
"SELECT id, nombre, apellido, correo
FROM usuario
ORDER BY id ASC";
$result = pg_query($dbconn, $consult);

$datos = pg_fetch_assoc($result);
?>