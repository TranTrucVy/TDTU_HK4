<?php
    require('connect.php');
    
    if(isset($_POST['delete_pro'])){
        $id_pro = $_POST['id'];
        $sql = mysqli_query($con,"DELETE FROM `cart` WHERE `stt` = '$id_pro'");
        
        if($sql){
            header("Location: cart.php");
        }
        else{
            echo "Something went wrong";
        }

    }
?>