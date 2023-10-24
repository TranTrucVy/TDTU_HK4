<?php
    require 'connect.php';
    session_start();

    if(!isset($_SESSION['login'])){
        header("location: login.php");
    }
    else{
        function createID($old_id){
            $num_id = (int) $old_id + 1;
            return $num_id;
        }
    
        $check = mysqli_query($con,"SELECT * FROM `cart`");
        if(mysqli_num_rows($check) != 0){
            $recent_id = mysqli_query($con,"SELECT * FROM `cart` ORDER BY `stt` DESC LIMIT 1");
            while($row = mysqli_fetch_assoc($recent_id)){
                $last = $row["stt"];
            }
            $id = createID($last);
        }
        else{
            $id = createID("0");
        }
    
        $id_check = $_GET['id'];
        $sql_cart = "SELECT * FROM `product` WHERE `id` = '$id_check'";
        $sql_cart_run = mysqli_query($con,$sql_cart);
        while($row = $sql_cart_run->fetch_array(MYSQLI_ASSOC)){
            $name = $row['name'];
            $price = $row['price'];
            $image = $row['image'];
        }
    
        $sql = "INSERT INTO `cart` VALUES(?,?,?,?)";
        $stm = $con -> prepare($sql);
        $stm -> bind_param("ssss",$id,$image,$name,$price);
        if(!$stm->execute()){
            die($stm->error);
        }
        else{
            header("location:cart.php");
        }
    }

    
?>