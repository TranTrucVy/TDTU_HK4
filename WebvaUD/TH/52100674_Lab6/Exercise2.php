<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <title>Lab6 - Exercise2</title>
</head>
<body>
    <?php
        $dispResult = 'display: none';
        $result = '';

        $dispAlert = '';
        $alertMess = 'Vui lòng nhập đầy đủ thông tin';

        if (isset($_GET['numA']) && isset($_GET['numB'])&& isset($_GET['operation'])) {
            $a = $_GET['numA'];
            $b = $_GET['numB'];
            $op = $_GET['operation'];
            if ($a == '') {
                $dispAlert = '';
                $alertMess = 'Vui lòng nhập số hạng 1';
            } else if ($b == '') {
                $dispAlert = '';
                $alertMess = 'Vui lòng nhập số hạng 2';
            } else if ($op=='add') {
                $c = $a + $b;
                $result = "$a + $b = $c";
                $dispResult = '';
                $dispAlert = 'display: none';
            } 
            else if ($op=='subtract') {
                $c = $a - $b;
                $result = "$a - $b = $c";
                $dispResult = '';
                $dispAlert = 'display: none';
            } else if ($op=='multiply') {
                $c = $a * $b;
                $result = "$a x $b = $c";
                $dispResult = '';
                $dispAlert = 'display: none';
            } else if ($b==0) {
                $dispAlert = '';
                $alertMess = 'Không thể chia cho 0';
            } else {
                $c = $a / $b;
                $result = "$a / $b = $c";
                $dispResult = '';
                $dispAlert = 'display: none';
            }
        }
    ?>
    <div class="container">

        <div class="row">
            <div class="col-md-6 my-5 mx-auto border rounded px-3 py-3">
                <h4 class="text-center">Tính toán cơ bản</h4>
                <form action="" method="get">
                    <div class="form-group">
                        <label for="num1">Số hạng 1</label>
                        <input type="text" class="form-control" id="num1" name="numA">
                    </div>
                    <div class="form-group">
                        <label for="num2">Số hạng 2</label>
                        <input type="text" class="form-control" id="num2" name="numB">
                    </div>
                    <div class="form-group">
                        <div class="custom-control custom-radio custom-control-inline">
                            <input name="operation" value="add" id="add" type="radio" class="custom-control-input">
                            <label for="add" type="radio" class="custom-control-label">Cộng</label>
                        </div>
                        <div class="custom-control custom-radio custom-control-inline">
                            <input name="operation" value="subtract" id="subtract" type="radio" class="custom-control-input">
                            <label for="subtract" type="radio" class="custom-control-label">Trừ</label>
                        </div>
                        <div class="custom-control custom-radio custom-control-inline">
                            <input name="operation" value="multiply" id="multiply" type="radio" class="custom-control-input">
                            <label for="multiply" type="radio" class="custom-control-label">Nhân</label>
                        </div>
                        <div class="custom-control custom-radio custom-control-inline">
                            <input name="operation" value="divide" id="divide" type="radio" class="custom-control-input">
                            <label for="divide" type="radio" class="custom-control-label">Chia</label>
                        </div>
                    </div>
                    <div class="alert alert-danger pt-2 pb-2" style="<?= $dispAlert ?>"><?= $alertMess ?></div>
                    <button class="btn btn-success">Xem kết quả</button>
                </form>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6 mx-auto px-3 py-3 text-center">
                <div class="alert alert-success" style="<?= $dispResult ?>"><?= $result ?></div>
            </div>
        </div>
    </div>
</body>
</html>