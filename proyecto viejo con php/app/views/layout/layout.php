<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= $titulo ?? 'Proyecto TPOO' ?></title>
    <!-- Bootstrap icons -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <!-- CSS general -->
    <link rel="stylesheet" href="../../../public/css/layout.css">
    <!-- Icono de prestaña del navegador -->
    <link rel="icon" href="../../../public/images/logo-icon.png" type="image/png">
</head>

<body>
    <!-- SideBar -->
    <nav>
        <img src="../../../public/images/logo.jpg" alt="logo">
        <ul>
            <li>
                <a class="primero <?= ($paginaActual === 'polizas') ? 'activo' : '' ?>" href="polizas.php">Pólizas</a>
            </li>
            <li>
                <a class="<?= ($paginaActual === 'clientes') ? 'activo' : '' ?>" href="clientes.php">Clientes</a>
            </li>
            <li>
                <a <?= ($paginaActual === 'agentes') ? 'activo' : '' ?> href="">Agentes</a>
            </li>
            <li>
                <a <?= ($paginaActual === 'aseguradoras') ? 'activo' : '' ?> href="">Aseguradoras</a>
            </li>
            <li>
                <a <?= ($paginaActual === 'reportes') ? 'activo' : '' ?> href="">Reportes</a>
            </li>
        </ul>
    </nav>
    <!-- NavBar -->
    <div id="superior">
        <a href="">
            <img src="../../../public/images/profile-default.png" alt="Foto de perfil">
            Nombre
        </a>
    </div>
    <div id="principal">
        <!-- Contenido -->
        <div id="contenedor">
            <?= $contenido ?? 'No hay contenido' ?>
        </div>
        <!-- Footer -->
        <footer>
            <div>
                <h1>Ruja CRM</h1>
                <p id="subtitulo">Simplificando gestiones desde 2025</p>
            </div>
            <div id="segundo">
                <p>Proyecto hecha con mucho esfuezo y dedicación, haciendo uso de todos los conocimientos que se han adquirido durante el semestre.</p>
            </div>
            <div>
                <a href="https://github.com/DarkGhost74/ProyectoTPOO">
                    <i class="bi bi-github"></i>
                    Repositorio
                </a>
            </div>
        </footer>
    </div>
</body>

</html>