<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php

/* Este archivo debe manejar la lógica para obtener la información del perfil */

//Se define el correo como aquel del usuario que ha iniciado sesión.
$email = $_SESSION['user'];
//Se realiza la consulta a la base de datos por los datos que se exhibirán en la página Billetera.
$consult = 
"SELECT moneda.sigla, moneda.nombre, tabla_id.balance, ultimo_valor.valor
FROM
	(SELECT usuario_tiene_moneda.id_moneda AS id_moneda, usuario_tiene_moneda.balance
	 FROM usuario INNER JOIN usuario_tiene_moneda ON usuario.id = usuario_tiene_moneda.id_usuario
	 WHERE usuario.correo = '$email'
	) AS tabla_id INNER JOIN
	 (SELECT precio_moneda.id_moneda AS id_moneda, precio_moneda.valor
	 	FROM (SELECT precio_moneda.id_moneda, MAX(precio_moneda.fecha) AS max_fecha
		  	  FROM precio_moneda
		      GROUP BY precio_moneda.id_moneda
		  ) AS tabla1 INNER JOIN precio_moneda
	  ON precio_moneda.id_moneda = tabla1.id_moneda AND precio_moneda.fecha = tabla1.max_fecha) AS ultimo_valor
	  ON tabla_id.id_moneda = ultimo_valor.id_moneda,
	  moneda
WHERE
	moneda.id = tabla_id.id_moneda";
$result2 = pg_query($dbconn, $consult);

//$datos2 = pg_fetch_assoc($result2);

?>