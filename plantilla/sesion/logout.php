<?php
//Se inicia una sesión, para cerrarla en el caso de que no haya una sesión iniciada.
session_start();
//Se vacían las variables superglobales $_SESSION['user'] y $_SESSION['admin'].
unset($_SESSION['user']);
unset($_SESSION['admin']);
//Se redirige a la página principal.
header('location:../index.html')
?>