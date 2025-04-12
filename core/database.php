<?php

$host = "localhost";
$user = "root";
$password = "0407";
$database = "proyectotpoo";

$connection = mysqli_connect($host,$user,$password,$database);
if(!$connection){
    echo "Hubo un error al conectar a la base de datos";
    exit;
}