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
    <title>PHP Exercises</title>
    <style>
        h5 {
            font-weight: bold;
        }
    </style>
</head>
<body>
<?php
    $titleClass = "row ml-5 mt-3 text-secondary";
    $valueClass = "row ml-5 text-success";

    function wbName($value) {
        if ($value=='chrome') {
            return 'Google Chrome';
        }
        if ($value=='ff') {
            return 'Fire fox';
        }
        if ($value=='safari') {
            return 'Safari';
        }
        if ($value=='edge') {
            return 'Edge';
        }
    }
    function osName($value) {
        if ($value=='win10') {
            return 'Windows 10';
        }
        if ($value=='mac') {
            return 'macOS';
        }
        if ($value=='linux') {
            return 'Linux';
        }
    }

    if (!empty($_POST['name'])) {
        $name = $_POST['name'];
    } else {
        $name = '';
    }
    if (!empty($_POST['email'])) {
        $email = $_POST['email'];
    } else {
        $email = '';
    }
    if (!empty($_POST['gender'])) {
        $gender = ucfirst($_POST['gender']);
    } else {
        $gender = '';
    }
    if (!empty($_POST['favWeb'])) {
        $webVal = $_POST['favWeb'];
        $favWeb = array_map('wbName', $webVal);
    } else {
        $favWeb = '';
    }
    if (!empty($_POST['favOS'])) {
        $favOS = osName($_POST['favOS']);
    } else {
        $favOS = '';
    }
?>
    <div class="container mt-3">
    <div class="col-md-8 col-lg-5 my-5 mx-2 mx-sm-auto border rounded px-3 py-3">
        <div class="row">
            <h5 class="mx-auto mt-2 text-success">Confirm Information</h5>
        </div>
        <!--Name-->
        <div class="row">
            <div class="<?=$titleClass?>"><h6>Your name</h6></div>
        </div>
        <div class="row">
            <div class="<?=$valueClass?>"><h5><?=$name?></h5></div>
        </div>
        <!--Email-->
        <div class="row">
            <div class="<?=$titleClass?>"><h6>Your email</h6></div>
        </div>
        <div class="row">
            <div class="<?=$valueClass?>"><h5><?=$email?></h5></div>
        </div>
        <!--Gender-->
        <div class="row">
            <div class="<?=$titleClass?>"><h6>Gender</h6></div>
        </div>
        <div class="row">
            <div class="<?=$valueClass?>"><h5><?=$gender?></h5></div>
        </div>
        <!--Favorite web browser-->
        <div class="row">
            <div class="<?=$titleClass?>"><h6>Favorite web browser</h6></div>
        </div>
        <div class="row">
            <div class="<?=$valueClass?>">
                <ul>
                    <?php
                        if ($favWeb!='') {
                            foreach ($favWeb as $c) {
                                echo "<li><h5>$c</h5></li>";
                            }
                        }
                    ?>
                </ul>
            </div>
        </div>
        <!--Prefered OP-->
        <div class="row">
            <div class="<?=$titleClass?>"><h6>Prefered Operating System</h6></div>
        </div>
        <div class="row">
            <div class="<?=$valueClass?>"><h5><?=$favOS?></h5></div>
        </div>
        <div class="row">
            <button type="button" onclick="save()" class="col-xs-4 ml-5 mb-3 mt-2 btn btn-success px-5 mr-2">Save</button>
            <button type="button" onclick="back()" class="col-xs-4 mb-3 mt-2 btn btn-outline-success px-5">Back</button>
        </div>
    </div>

    <script>
        function save() {
            alert("Saved successfully");
            back();
        }

        function back() {
            window.history.back();
        }
    </script>
</body>
</html>