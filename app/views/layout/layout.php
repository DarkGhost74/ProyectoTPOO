<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= $titulo ?? 'Proyecto TPOO' ?></title>
    <link rel="stylesheet" href="../../../public/css/layout.css">
    <link rel="icon" href="../../../public/images/logo-icon.png" type="image/png">
</head>

<body>
    <nav>
        <img src="../../../public/images/logo.jpg" alt="logo">
        <ul>
            <li>
                <a class="primero" href="">Pólizas</a>
            </li>
            <li>
                <a href="">Clientes</a>
            </li>
            <li>
                <a href="">Agentes</a>
            </li>
            <li>
                <a href="">Aseguradoras</a>
            </li>
            <li>
                <a href="">Reportes</a>
            </li>
        </ul>
    </nav>
    <div id="superior">
        <ul>
            <li>
                <img src="../../../public/images/profile-default.png" alt="Foto de perfil">
            </li>
            <li>
                <P>Nombre</P>
            </li>
        </ul>
    </div>
</body>

</html>