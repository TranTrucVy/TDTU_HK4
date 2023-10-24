<?php
    require 'connect.php';
    session_start();

    $sql_pay = "DELETE FROM `cart`";
    $sql_run = mysqli_query($con,$sql_pay);
    header("location: bill_pdf.php");
?>