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

    <title>Apple Shop</title>

    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/shop-homepage.css" rel="stylesheet">

  </head>
  <style>
    .list-group{
      border: 1px solid black;
      border-radius: 6px;
    }
  </style>

  <body>

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <a class="navbar-brand" href="index.php">Start bootstrap</a>
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

        <div class="row">

          <div class="col-lg-3">

            <h1 class="my-4">Apple</h1>
            <div class="list-group">
              <a href="apple_shop.php" class="list-group-item">Apple</a>
              <a href="samsung_shop.php" class="list-group-item">Samsung</a>
              <a href="oppo_shop.php" class="list-group-item">Oppo</a>
              <a href="google_shop.php" class="list-group-item">Google</a>
              <a href="nokia_shop.php" class="list-group-item">Nokia</a>

            </div>

          </div>
          <!-- /.col-lg-3 -->

          <div class="col-lg-9">

            <div id="carouselExampleIndicators" class="carousel slide my-4" data-ride="carousel">
              <ol class="carousel-indicators">
                <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
              </ol>
              <div class="carousel-inner" role="listbox">
                <div class="carousel-item active">
                  <img class="d-block img-fluid" src="images/ava1.png" alt="First slide">
                </div>
                <div class="carousel-item">
                  <img class="d-block img-fluid" src="images/ava2.png" alt="Second slide">
                </div>
                <div class="carousel-item">
                <img class="d-block img-fluid" src="images/ava3.png" alt="Third slide">
                </div>
              </div>
              <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
              </a>
              <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
              </a>
            </div>
            <div class="row">
            <?php
              $sql_phone = "SELECT * FROM `product` WHERE `name` LIKE '%iPhone%'";
              $run = mysqli_query($con, $sql_phone);
              while($row = $run->fetch_array(MYSQLI_ASSOC)){
                $id = $row['id'];
                $name = $row['name'];
                $price = $row['price'];
                $des = $row['description'];
                $vote = $row['vote'];
                $image = $row['image'];

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
                <div class="col-lg-4 col-md-6 mb-4">
                  <div class="card h-100" >
                    <a href=""><img style="padding:10px" class="card-img-top" src="'.$image.'" alt=""></a>
                    <div class="card-body">
                      <h4 class="card-title">
                        <a href="">'.$name.'</a>
                      </h4>
                      <h5 style="color: #f47442">'.$price.' VND</h5>
                      <p class="card-text">'.$des.'</p>
                      <small class="text-muted">'.$vote.'</small>
                    </div>
                    <div class="card-footer">
                      <a href="C_cart.php?id='.$id.'" style="color: white;" class="btn btn-primary">Add to cart</a>
                    </div>
                  </div>
                </div>
                ';
              }
            ?>
            </div>
          </div>
          <!-- /.col-lg-9 -->

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
