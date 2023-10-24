<?php
    require 'connect.php';

    function createID($old_id){
        $char = substr($old_id, 0, 2);
        $num_id = (int) substr($old_id,2) + 1;
        $new_id = '';
        for($i = 0; $i < (4-strlen((string) $num_id)); $i++){
            $new_id = $new_id . "0";
        }
        return $char . $new_id . $num_id;

    }
    
    if (isset($_POST['register'])) {

        $check = mysqli_query($con,"SELECT * FROM `customer`");
        if(mysqli_num_rows($check) != 0){
            $recent_id = mysqli_query($con,"SELECT * FROM `customer` ORDER BY `cust_id` DESC LIMIT 1");
            while($row = mysqli_fetch_assoc($recent_id)){
                $last = $row["cust_id"];
            }
            $id = createID($last);
        }
        else{
            $id = createID("KH0000");
        }

        $add_user = $_POST['username'];
        $add_password = $_POST['password'];
        $add_email = $_POST['email'];

        $check_user = mysqli_query($con,"SELECT * FROM `customer` WHERE `username` = '$add_user'");
        if(mysqli_num_rows($check_user)>0){
            header("location: login.php?exist=" . urlencode("Exist"));
        }
        else{
            $sql = "INSERT INTO `customer` VALUES(?,?,?,?)";
            $stm = $con -> prepare($sql);
            $stm -> bind_param("ssss",$id,$add_user,$add_password,$add_email);
            if(!$stm->execute()){
                die($stm->error);
            }
            else{
                header("location:login.php?signup=" . urlencode("Success"));
            }
        }
    }
?>