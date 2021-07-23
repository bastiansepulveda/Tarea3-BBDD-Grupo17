<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php
//Obtenemos el id del usuario entregada en la url a trav�s del m�todo GET.
$id = htmlspecialchars($_GET['id']);
//Obtenemos los datos a trav�s de una consulta, utilizando el id recibido en la l�nea anterior.
$consult = 
"SELECT usuario.id, usuario.nombre, usuario.apellido, usuario.correo, usuario.fecha_registro, pais.nombre_pais AS pais
FROM usuario
INNER JOIN pais 
ON pais.cod_pais = usuario.pais
WHERE id = $id ";
$result = pg_query($dbconn, $consult);

$datos = pg_fetch_assoc($result);
?>