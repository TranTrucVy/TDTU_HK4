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


<div class="container" style="width: 600px">
    <h2>Thêm sản phẩm</h2>
    <form action="action_page.php" method="post" enctype="multipart/form-data">
        <div class="form-group">
            <label for="id">Id:</label>
            <input type="text" class="form-control" id="id" placeholder="Enter id" name="id">
        </div>
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" class="form-control" id="name" placeholder="Enter name" name="name">
        </div>
        <div class="form-group">
            <label for="price">Price:</label>
            <input type="text" class="form-control" id="price" placeholder="Enter price" name="price">
        </div>
        
        <div class="form-group">
            <label for="img">Image:</label>
            <input type="file" class="form-control" id="img" placeholder="Enter image" name="image">
        </div>

        <div class="form-group">
            <label for="description">Description:</label>
            <input type="text" class="form-control" id="description" placeholder="Enter description" name="description">
        </div>
        
        <button type="submit" class="btn btn-primary" name="add" id="add">Add</button>
        <button type="reset" class="btn btn-default">Reset</button>
    </form>

    <br>
    <div id="announce" style="display:none">
        <div class="alert alert-danger">
            <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
            Vui lòng nhập đầy đủ thông tin sản phẩm.
        </div>
    </div>
</div>
    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>    
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <!-- <script>
        $(document).ready(function () {
            $('#announce').hide();
            $('#add').click(function (e) { 
                if ($('#id').val() == '' ||
                    $('#name').val() == '' ||
                    $('#price').val() == '' ||
                    $('#image').val() == '' ||
                    $('#description').val() == ''
                ){
                    e.preventDefault();
                    $('#announce').show();
                    setTimeout(() => {
                        $('#announce').fadeOut();
                    }, 2000);
                } else {

                }

            });
        });
    </script> -->
</body>
</html>