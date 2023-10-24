<?php
  require "connect.php";
  session_start();
?>

<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Shop Homepage</title>

    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/shop-homepage.css" rel="stylesheet">

  </head>
  <style>
    footer{
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 2.5rem;   
    }

  </style>

  <body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <a class="navbar-brand" href="index.php">Smart Station</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <a class="nav-link" href="index.php">Home
                <span class="sr-only">(current)</span>
              </a>
            </li>
              <li class="nav-item">
                  <?php
                    if(isset($_SESSION['login'])){
                      echo '<a class="nav-link" href="logout.php">Log out</a>';
                    }
                    else{
                      echo '<a class="nav-link" href="login.php">Username</a>';
                    }
                  ?>
                  
              </li>
            <li class="nav-item">
                <?php
                    $sql_cart = "SELECT * FROM `cart`";
                    $sql_cart_run = mysqli_query($con, $sql_cart);
                    $count = mysqli_num_rows($sql_cart_run);

                    if(isset($_SESSION['login'])){
                      echo '<a class="nav-link" href="cart.php">Cart ('.$count.' items)</a>';
                    }
                  ?>
              
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Page Content -->
      <div class="container">

        <div class="row" style="padding-top:70px">
        <?php
            $id = $_GET['id'];
            $sql_detail = "SELECT * FROM `product` WHERE `id` = '$id'";
            $sql_detail_run = mysqli_query($con, $sql_detail);
            while($row = $sql_detail_run->fetch_array(MYSQLI_ASSOC)){
                $id = $row['id'];
                $name = $row['name'];
                $price = $row['price'];
                $des = $row['description'];
                $vote = $row['vote'];
                $image = $row['image'];
            }

            if($vote == "1"){
                $vote = "&#9733; &#9734; &#9734; &#9734; &#9734;";
              }
              else if($vote == "2"){
                $vote = "&#9733; &#9733; &#9734; &#9734; &#9734;";
              }
              else if($vote == "3"){
                $vote = "&#9733; &#9733; &#9733; &#9734; &#9734;";
              }
              else if($vote == "4"){
                $vote = "&#9733; &#9733; &#9733; &#9733; &#9734;";
              }
              else if($vote == "5"){
                $vote = "&#9733; &#9733; &#9733; &#9733; &#9733;";
            }

            echo '
                <div class="col-lg-5" style="text-align: center">
                    <img style="width:300px" class="card-img-top" src="'.$image.'" alt="">
                </div>

                <div class="col-lg-7">
                    <h1>'.$name.'</h1>
                    <small class="text-muted" style="font-size:30px">'.$vote.'</small>
                    <h3>'.number_format($price,0,',','.').' VND</h3>
                    <h6>'.$des.'</h6>
                    <a href="C_Cart.php?id='.$id.'" style="color: white; " class="btn btn-primary">Add to cart</a>
                </div>
            ';
        ?>

          

        </div>
<!-- /.row -->
        
    </div>
    
    
    <!-- /.container -->
<!-- Footer -->
<footer class="py-5 bg-dark">
      <div class="container">
        <p class="m-0 text-center text-white">Copyright &copy; Your Website 2017</p>
      </div>
      <!-- /.container -->
    </footer>
    

    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
    <script>
      // $(document).ready(function(){
      //       $(".btn btn-primary").click(function(){
      //           var id = $(this).attr("id");
      //           var url = "cart_test.php" + "?id=" + id;
      //           window.location.href = url;
      //       });
      //   });
    </script>
  </body>

</html>
