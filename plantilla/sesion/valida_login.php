<?php include $_SERVER['DOCUMENT_ROOT'].'/db_config.php'; ?>

<?php 
//Se inicia una sesión.
session_start();
//Se verifica que se hayan ingresado el correo y la contraseña.
if( isset($_POST['email']) && isset($_POST['pwd'])) {
    //Se definen las variables proporcionadas a través del método POST.
    $email = $_POST['email'];
    $password = $_POST['pwd'];

    //Se busca al usuario que tenga el correo proporcionado en el inicio de sesión.
    $consulta = "SELECT * FROM usuario WHERE correo = '$email'";

    $resultado = pg_query($dbconn, $consulta);

    //$result_consulta guarda los datos obtenidos gracias a la consulta anterior.
    $result_consulta = pg_fetch_assoc($resultado);

    //Se hashea la contraseña obtenida desde la base de datos para que no sea visible.
    $pwd_hash = password_hash($result_consulta['contraseña'], PASSWORD_DEFAULT);

    //Se guarda la cantidad de filas obtenidas en la consulta del correo.
    //Si $filas>0, es porque el correo está registrado.
    //Si $filas==0, es porque el correo no está registrado.
    $filas = pg_num_rows($resultado);

    //Se verifica que el correo esté registrado. De ser así, se sigue con la verificación de la contraseña.
    if($filas>0){
    //Se verifica que la contraseña entregada en el inicio de sesión coincida con la almacenada en la base de datos.
        if(password_verify($password, $pwd_hash)){
        //En caso afirmativo, se fijan las variables super globales $_SESSION['user'] y $_SESSION['admin'] con lo obtenido desde la base de datos.

            $_SESSION['user'] = $email;

            $_SESSION['admin'] = $result_consulta['admin'];
            //Y se redirige a la página principal.
            header("location:../index.html");
        }
        //Si la contraseña no coincida, se le indica a través de un mensaje y se devuelve a la página de inicio de sesión.
        else{
            echo '<script type="text/javascript">'; 
            echo 'alert("Correo o contraseña inválida. Intente nuevamente.");'; 
            echo 'window.location.href = "/sesion/log-in.html";';
            echo '</script>';
        }
    }
    //En el caso de no estar registrado el correo, se informa a través de una alerta y se devuelve a la página de inicio de sesión.
    else{
        echo '<script type="text/javascript">'; 
        echo 'alert("Correo o contraseña inválida. Intente nuevamente.");'; 
        echo 'window.location.href = "/sesion/log-in.html";';
        echo '</script>';
    }
    pg_free_result($resultado);

    pg_close($dbconn);
}

?>