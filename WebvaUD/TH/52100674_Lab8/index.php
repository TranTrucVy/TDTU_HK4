<?php require 'connect.php';?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

<style>
    body{
        padding-top: 50px;
    }
    table{

        text-align: center;
    }
    td{
        padding: 10px;
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


<script>
    $(document).ready(function () {


        $(".delete").click(function () {

            $('#myModal').modal({
                backdrop: 'static',
                keyboard: false
            });

        });


    });
</script>


<table cellpadding="10" cellspacing="10" border="0" style="border-collapse: collapse; margin: auto">

    <tr class="control" style="text-align: left; font-weight: bold; font-size: 20px">
        <td colspan="5">
            <a href="add.php">Thêm sản phẩm</a>
        </td>
    </tr>
    <tr class="header">
        <td>Image</td>
        <td>Name</td>
        <td>Price</td>
        <td>Description</td>
        <td>Action</td>
    </tr>
   
    <?php
    $sql = "SELECT * from product";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) { ?>
        <?php while ($row = $result->fetch_assoc()) { ?>
            <tr class="item">
                <td>
                    <img src="<?= $row['image'] ?>" alt="" style="max-height: 80px">
                </td>
                <td><?= $row['name'] ?></td>
                <td><?= $row['price'] ?></td>
                <td><?= $row['description'] ?></td>
                <td>
                <a href="update.php?id=<?= $row['id'] ?>">Edit</a> | <a href="#" class="delete" onclick="getId('<?= $row['id'] ?>')">Delete</a></td>

            </tr>
    <?php }
    } else {
        echo "<script>alert('Bảng chưa có dữ liệu')</script>";
    } ?>

    <tr class="control" style="text-align: right; font-weight: bold; font-size: 17px">
        <td colspan="5">
            <p>Số lượng sản phẩm: 
                <?php 
                    $sql = "SELECT * from product";
                    $result = $conn->query($sql);
                    $i = 0;
                    while ($row = $result->fetch_assoc()) {
                        $i++;
                    }
                    echo $i;
                ?>
        </p>
        </td>
    </tr>
</table>


<!-- Delete Confirm Modal -->
<div id="myModal" class="modal fade" role="dialog">
    <div class="modal-dialog">

        <!-- Modal content-->
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">&times;</button>
                <h4 class="modal-title">Modal Header</h4>
            </div>
            <div class="modal-body">
                <p>Some text in the modal.</p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                <a href="#" type="button" class="btn btn-danger" name="delete" data-dismiss="modal" onclick="deleteData()">Delete</a>
            </div>
            
        </div>

    </div>
</div>

<script>

function getId(id) {
  localStorage.setItem("id", id);
}

function deleteData() {
  var id = localStorage.getItem("id");
  $.ajax({
    type: "POST",
    url: "action_page.php",
    data: {
        action: 'delete',
        id: id
    },
    success: function (response) {
        window.location.href = 'index.php';
    },
  });
}

</script>
</body>
</html>