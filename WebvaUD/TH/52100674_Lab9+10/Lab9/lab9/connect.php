<?php
    $con = new mysqli("localhost","root","","online_marketing_db");
    if($con -> connect_error){
        die("Connection failed" .$con->connect_error);
    }

?>