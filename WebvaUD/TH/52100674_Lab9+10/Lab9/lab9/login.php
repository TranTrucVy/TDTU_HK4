<?php  
  require 'connect.php';

  $message = '';
  $flag = '';
  if(isset($_GET['error'])) {
    $flag = false;
    $message = 'User not found';
  }
  else if(isset($_GET['signup'])){
    $flag = true;
    $message = 'Sign up success';
  }
  else if(isset($_GET['exist'])){
    $message = 'Username is already existed! Please choose another username!';
  }
?>
<!DOCTYPE html>
<html >
<head>
  <meta charset="UTF-8">
  <title>Login Form</title>
  
  
  
      <link rel="stylesheet" href="css/style.css">

  
</head>

<body>
  <div class="login-page">
  <div class="form">
    <form class="register-form" action="C_Register.php" method="post">
      <input type="text" placeholder="username" name="username" required/>
      <input type="password" placeholder="password" name="password" required/>
      <input type="text" placeholder="email address" name="email" required/>
      <button name="register" value="register">create</button>
      <p class="message">Already registered? <a href="#">Sign In</a></p>
    </form>
    <form class="login-form" action="C_Login.php" method="post">
      <input type="text" placeholder="username" name="username" required/>
      <input type="password" placeholder="password" name="password" required/>
      <?php
      if($flag == true){
        echo '<p style = "color: green; font-weight: bold; margin-top:-5px;">'.$message.'</p>';
      }
      else if($flag == false){
        echo '<p style = "color: red; font-weight: bold; margin-top:-5px;">'.$message.'</p>';
      }
      else{
        echo '<p style = "color: red; font-weight: bold; margin-top:-5px;">'.$message.'</p>';
      }
       
      ?>
      <button name="login" value="login">login</button>
      <p class="message">Not registered? <a href="#">Create an account</a></p>

    </form>
  </div>
</div>
  <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

    <script  src="js/index.js"></script>

</body>
</html>
