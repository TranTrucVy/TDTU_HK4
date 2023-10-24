<?php
    require 'connect.php';
    session_start();

    error_reporting(E_ERROR | E_PARSE);

    if(!isset($_SESSION['login'])){
        header("location: login.php");
    }

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Cart</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

<style>
    body{
        background-color: white;
    }


</style>

<div class="container">
    <h2>Giỏ hàng</h2>

    <table class="table table-striped">
        <thead>
        <tr>
            <form action = "index.php">
                <td colspan="7">
                    <button type="submit" class="btn btn-primary">Tiếp tục mua hàng</button>
                </td>
            </form>
            
        </tr>
        <tr>
            <th>Ảnh</th>
            <th>STT</th>
            <th>Tên sản phẩm</th>
            <th>Số lượng</th>
            <th>Giá</th>
            <th>Thành tiền</th>
            <th>Xóa</th>
        </tr>
        </thead>
        <tbody>
        <form action = "" method="post">
            <?php
            
                $sql = "SELECT * FROM `cart`";
                $sql_run = mysqli_query($con,$sql);
                while($row = $sql_run->fetch_array(MYSQLI_ASSOC)){
                    $stt = $row['stt'];
                    $name = $row['pro_name'];
                    $price = $row['price'];
                    $image = $row['image'];

                    $number = $_POST['count'.$stt.''];
                    $total = (int) $price * $number;

                    echo '
                    <tr>
                        <td ><img src="'.$image.'" style="max-height: 50px"></td>
                        <td class="pro_id">'.$stt.'</td>
                        <td>'.$name.'</td>
                        <td><input type="number" value="1" min="1" name="count'.$stt.'" onchange="saveValue(this)" id="count'.$stt.'"></td>
                        <td><p>'.number_format($price,0,',','.').' VND</p></td>
                        <td>'.number_format($total,0,',','.').' VND</td>
                        <td><button style="background-color:#D9534F; color: white; border-radius: 5px; padding: 8px; border: none" class="delete_btn">Xóa</button></td>
                    </tr>
                    ';

                    if(isset($number)){
                        $check = "SELECT * FROM `bill` WHERE `stt` LIKE '$stt'";
                        $check_run = mysqli_query($con,$check);
                        if(mysqli_num_rows($check_run)>0){
                            $update = "UPDATE `bill` SET `pro_name` = '$name', `quantity` = '$number', `price` = '$price', `total` = '$total' WHERE `stt` = '$stt'";
                            mysqli_query($con,$update);

                        }
                        else{
                            $sql = "INSERT INTO `bill` VALUES(?,?,?,?,?)";
                            $stm = $con -> prepare($sql);
                            $stm -> bind_param("sssss",$stt,$name,$number,$price,$total);
                            if(!$stm->execute()){
                                die($stm->error);
                            }
                        }
                        
                    }
                
                    


                }

                
            ?>
            
            <tr>
                <td colspan="7" style="text-align: right">
                    <p><i>(Note: Click "Cập nhật giỏ hàng" to reload the total for payment!)</i></p>
                    <button type="submit" class="btn btn-success">Cập nhật giỏ hàng</button>
                    <button type="button" class="btn btn-danger" onclick="paySuccess()">Thanh toán</button>
                </td>
            </tr>
        </form>
        
        </tbody>
    </table>
</div>
<!-- Delete Confirm Modal -->
<div id="myModal" class="modal fade" role="dialog">
    <div class="modal-dialog">

        <!-- Modal content-->
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">&times;</button>
                <h4 class="modal-title">Delete Product</h4>
            </div>
            <form action="C_Delete.php" method="POST">
                <div class="modal-body">
                    <input type="hidden" name="id" id="delete_id" >
                    <h5>Are you sure you want to delete this product?</h5>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                    <button type="submit" class="btn btn-danger" name="delete_pro" value="delete">Delete</button>
                </div>
            </form>

        </div>

    </div>
</div>
</body>
<script>

    $(document).ready(function(){
        $('.delete_btn').click(function(e){
            e.preventDefault();
            var id = $(this).closest('tr').find('.pro_id').text();
            
            $('#delete_id').val(id);
            $('#myModal').modal('show');
            
        })
    })

    function paySuccess(){
        alert("Payment Successful!");
        window.location.href = "C_Payment.php";
    }

    for (i = 1; i < 100; i++)     
    {
        let num = i;
        var id_char = "count";
        let result = id_char.concat(num);
        document.getElementById(result).value = getSavedValue(result); 
    }

    //Save the value function - save it to localStorage as (ID, VALUE)
    function saveValue(e){
        var id = e.id;  // get the sender's id to save it . 
        var val = e.value; // get the value. 
        localStorage.setItem(id, val);// Every time user writing something, the localStorage's value will override . 
    }

    //get the saved value function - return the value of "v" from localStorage. 
    function getSavedValue  (v){
        if (!localStorage.getItem(v)) {
            return "1";// You can change this to your defualt value. 
        }
        return localStorage.getItem(v);
    }

    
</script>
</html>