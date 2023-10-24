<?php
    require 'connect.php';
    session_start();
    
    if (isset($_POST['login'])) {
        $check_user = $_POST['username'];
        $check_password = $_POST['password'];

        $check_user = mysqli_real_escape_string($con, $check_user);
        $check_password = mysqli_real_escape_string($con, $check_password);

        $sql_login = "SELECT * FROM `customer` WHERE `username` LIKE '$check_user' AND `password` LIKE '$check_password'";
        $sql_run = mysqli_query($con, $sql_login);
        $num = mysqli_num_rows($sql_run);
        if ($num==0) {
            header("location:login.php?error=" . urlencode("Unknown User"));

        } else {
            $_SESSION['login'] = true;
            header('location: index.php');
        }
    }
?>