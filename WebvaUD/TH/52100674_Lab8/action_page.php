<?php
    require 'connect.php';

    $target_dir = "images/";
    if (isset($_POST['add'])) {
        $id = $_POST['id'];
        $name = $_POST['name'];
        $price = $_POST['price'];
        $image = basename($_FILES["image"]["name"]);//$_POST['image'];
        $description = $_POST['description'];

        $target_file = $target_dir . basename($_FILES["image"]["name"]);
        $uploadOk = 1;
        if (file_exists($target_file)) {
            echo "Sorry, file already exists.";
            $uploadOk = 0;
        }

        if ($uploadOk == 0) {
            echo "Sorry, your file was not uploaded.";
        } else {
            if (move_uploaded_file($_FILES["image"]["tmp_name"], $target_file)) {
                echo "The file ". htmlspecialchars( basename( $_FILES["image"]["name"])). " has been uploaded.";
            } else {
                echo "Sorry, there was an error uploading your file.";
            }
        }

        $sql = "INSERT INTO `product` (`id`, `name`, `price`, `image`, `description`) VALUES ('$id', '$name', '$price', 'images/$image', '$description')";

        mysqli_query($conn,$sql);
        header('location: index.php');
    }

    if (isset($_POST['action'])) {
        if ($_POST['action'] == 'delete') {
            $id = $_POST['id'];
            $sql = "DELETE FROM `product` WHERE `product`.`id` = '$id'";
    
            mysqli_query($conn,$sql);
            
        }
    }

    if (isset($_POST['update'])) {
        $id = $_POST['id'];
        $name = $_POST['name'];
        $price = $_POST['price'];
        $image = basename($_FILES["newImage"]["name"]);//$_POST['image'];
        $description = $_POST['description'];

        $target_file = $target_dir . basename($_FILES["newImage"]["name"]);
        $uploadOk = 1;
        if (file_exists($target_file)) {
            echo "Sorry, file already exists.";
            $uploadOk = 0;
        }

        if ($uploadOk == 0) {
            echo "Sorry, your file was not uploaded.";
        } else {
            if (move_uploaded_file($_FILES["image"]["tmp_name"], $target_file)) {
                echo "The file ". htmlspecialchars( basename( $_FILES["newImage"]["name"])). " has been uploaded.";
            } else {
                echo "Sorry, there was an error uploading your file.";
            }
        }
        // $image = 'images/'. $_POST['newImage'];
        // if ($image == 'images/') {
        //     $image = $_POST['oldImage'];
        // } 
        $description = $_POST['description'];

        $sql = "UPDATE `product` 
        SET
        `name` = '$name', 
        `price` = '$price', 
        `image` = 'images/$image', 
        `description` = '$description' 
        WHERE 
        `product`.`id` = '$id'";

        mysqli_query($conn,$sql);
        header('location: index.php');
    }
?>