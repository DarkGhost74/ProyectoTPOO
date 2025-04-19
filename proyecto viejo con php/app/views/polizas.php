<?php
$titulo = "Pólizas";
$paginaActual = "polizas";

ob_start();
?>
<h1>Pólizas</h1>
<p>Aqui va lo de polizas</p>
<?php
$contenido = ob_get_clean();

include('layout/layout.php');
?>