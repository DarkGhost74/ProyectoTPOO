<?php
$titulo = "Clientes";
$paginaActual = "clientes";

ob_start();
?>
<h1>Clientes</h1>
<p>Aqui va lo de clientes</p>
<?php
$contenido = ob_get_clean();

include('layout/layout.php');
?>