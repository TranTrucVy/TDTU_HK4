<?php require 'connect.php'?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    
</head>
<body>

<style>
    body{
        padding-top: 50px;
    }
    table{

        text-align: center;
    }
    tr.item{
        border-top: 1px solid #5e5e5e;
        border-bottom: 1px solid #5e5e5e;
    }

    tr.item:hover{
        background-color: #d9edf7;
    }

    tr.item td{
        min-width: 150px;
    }

    tr.header{
        font-weight: bold;
    }

    a{
        text-decoration: none;
    }
    a:hover{
        color: deeppink;
        font-weight: bold;
    }
</style>

<?php
    $sql = "SELECT * FROM `product` WHERE `id` LIKE '".$_GET['id']."' ";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) { 
        while ($row = $result->fetch_assoc()) {
            $list = $row;
        }
    }

?>
<div class="container" style="width: 600px">
    <h2>Cập nhật sản phẩm</h2>
    <form action="action_page.php" method="post" enctype="multipart/form-data">
        <div class="form-group">
            <label for="id">Id:</label>
            <input type="text" class="form-control" id="id" placeholder="Enter id" name="id" value="<?php echo $list['id'];?>" readonly>
        </div>
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" class="form-control" id="name" placeholder="Enter name" name="name" value="<?php echo $list['name'];?>">
        </div>
        <div class="form-group">
            <label for="price">Price:</label>
            <input type="text" class="form-control" id="price" placeholder="Enter price" name="price" value="<?php echo $list['price'];?>">
        </div>
        
        <div class="form-group">
            <input type="hidden" name="oldImage" value="<?php echo $list['image']?>">
        </div>

        <div class="form-group">
            <label for="img">Image:</label>
            <input type="file" class="form-control" id="img" name="newImage">
        </div>

        <div class="form-group">
            <label for="description">Description:</label>
            <input type="text" class="form-control" id="description" placeholder="Enter description" name="description" value="<?php echo $list['description'];?>">
        </div>
        
        <button type="submit" class="btn btn-primary" name="update">Update</button>
        <button type="reset" class="btn btn-default">Reset</button>
    </form>

    <br>
</div>
    
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</body>
</html>