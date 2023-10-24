<?php
    session_start();

    $loginPage = 'login.php';
    if (!isset($_SESSION['user'])) {
        header("Location: $loginPage");
        exit();
    }

    session_destroy();
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" />
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>

<body>
    <?php $timeset = 10 ?>
    <script>
        function backToLogin(){
            window.location.href = "<?= $loginPage ?>";
        }
    </script>

    <div class="container">
        <div class="row">
            <div class="col-md-6 mt-5 mx-auto p-3 border rounded">
                <h4>Đăng xuất thành công</h4>
                <p>Tài khoản của bạn đã được đăng xuất khỏi hệ thống.</p>
                <p>Nhấn <a href="<?= $loginPage ?>">vào đây</a> để trở về trang đăng nhập,
                    hoặc trang web sẽ tự động chuyển hướng sau
                    <span id="countDown" class="text-danger"><?= $timeset ?></span> giây nữa.
                </p>
                <button onclick="backToLogin()" class="btn btn-success px-5">Đăng nhập</button>
            </div>
        </div>
    </div>

    <script>
        let countDown = document.getElementById('countDown');

        let timeSet = <?= $timeset ?>;
        let count = 0;

        let intervalID = setInterval(() => {
            count++;
            let remaintime = timeSet - count;
            if (remaintime >= 0) {
                countDown.innerHTML = remaintime;
            } else {
                clearInterval(intervalID);
                backToLogin();
            }
        }, 1000)
    </script>
</body>

</html>