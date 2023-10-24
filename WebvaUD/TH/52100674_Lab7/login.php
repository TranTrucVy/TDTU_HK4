<?php
    session_start();

    $homePage = 'home.php';
    if (isset($_SESSION['user']) && isset($_SESSION['pass'])) {
        header("Location: $homePage");
        exit();
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
<?php
    $trueUser = "admin";
    $truePass = "123456";

    $displayErr = "display: none";
    $errorMess = "";

    if (isset($_COOKIE['user']) && isset($_COOKIE['pass'])) {
        $previousUser = $_COOKIE['user'];
        $previousPass = $_COOKIE['pass'];
    } else { 
        $previousUser = "";
        $previousPass = "";
    }

    if (isset($_POST['user']) && isset($_POST['pass'])) {
        $user = $_POST['user'];
        $pass = $_POST['pass'];
        $previousUser = $user;
        $previousPass = $pass;
        if (empty($user)) {
            $errorMess = "Bạn chưa nhập username";
            $displayErr = "";
        } else if (empty($pass)) {
            $errorMess = "Bạn chưa nhập password";
            $displayErr = "";
        } else if ($user!=$trueUser || $pass!=$truePass) {
            $errorMess = "Sai tên username hoặc password";
            $displayErr = "";
        } else {
            $displayErr = "display: none";
            if (isset($_POST['remember'])) {
                setcookie('user', $user, time() + 3600 * 24); //1 ngay
                setcookie('pass', $pass, time() + 3600 * 24); //1 ngay
            }
            $_SESSION['user'] = $user;
            $_SESSION['pass'] = $pass;

            header("Location: $homePage");
            exit();
        }
    } else {

    }
?>

<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6 col-lg-5">
            <h3 class="text-center text-secondary mt-5 mb-3">User Login</h3>
            <form action="login.php" method="POST" class="border rounded w-100 mb-5 mx-auto px-3 pt-3 bg-light">
                <div class="form-group">
                    <label for="username">Username</label>
                    <input name="user" value="<?=$previousUser?>" id="username" type="text" class="form-control" placeholder="Username">
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input name="pass" value="<?=$previousPass?>" id="password" type="password" class="form-control" placeholder="Password">
                </div>
                <div class="form-group custom-control custom-checkbox">
                    <input name="remember" type="checkbox" class="custom-control-input" id="remember">
                    <label class="custom-control-label" for="remember">Remember login</label>
                </div>
                <div class="form-group">
                    <div class="alert alert-danger" style="<?= $displayErr ?>"><?= $errorMess ?></div>
                    <button type="submit" class="btn btn-success px-5">Login</button>
                </div>
                <div class="form-group">
                    <p>Forgot password? <a href="#">Click here</a></p>
                </div>
            </form>

        </div>
    </div>
</div>

</body>
</html>