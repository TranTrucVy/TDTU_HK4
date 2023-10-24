<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lab5 - Exercise1</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <style>
        * {
            box-sizing: border-box;
        }
        .colorInfo {
            background-color: rgb(69, 69, 69);
            color: white;
            width: 300px;
            text-align: center;
            font-size: larger;
            border-radius: 16px;
            padding: 20px;
            margin: auto;
            margin-top: 30px;
            margin-bottom: 30px;
        }

        .colorPalette {
            width: 300px;
            height: 300px;
            margin: auto;
        }

        .colorRow {
            clear: both;
            float:left;
            height: 10%;
            width: 100%;
        }

        .colorCell {
            float: left;
            border: 1px solid black;
            width: 10%;
            height: 100%;
        }

        .noti {
            background-color: rgb(218, 241, 220);
            color: rgb(42, 82, 46);
            width: 500px;
            text-align: center;
            font-size: large;
            border-radius: 10px;
            padding: 16px;
            margin: auto;
            margin-top: 30px;
        }
    </style>
    
    <?php
        function randomColor() {
            $r = rand(0, 255);
            $g = rand(0, 255);
            $b = rand(0, 255);
            $color = 'rgb(' . strval($r) . ',' . strval($g) . ',' . strval($b) . ')';
            return $color;
        }
    ?>
</head>
<body>

<!--Ô hiển thị thông tin màu-->
<div class="colorInfo">Hover a cell</div>

<!--Tạo palette-->
<div class="colorPalette" id='colorPalette'>
    <?php
        for ($row=1; $row<=10; $row++) {
            echo "<div class='colorRow'>";
            for ($col=1; $col<=10; $col++) {
                $color = randomColor();
                $c = $col*$row;
                echo "<div class='colorCell' style='background-color: $color'>
                    </div>";
            }
            echo "</div>";
        }
    ?>
</div>

<!--Ô thông báo-->
<div class="noti" style="display: none"></div>

<script>
    let currentBgColor = 'rgb(255 , 255, 255)';

    $(".colorCell").on({
        mouseenter: function(){
            let bgColor = $(this).css("backgroundColor");
            
            $('body').css("background-color", bgColor);
            $('.colorInfo').html(bgColor);
        },
        mouseleave: function(){
            $('body').css("background-color", currentBgColor);
        },
        click: function(){
            currentBgColor = $(this).css("backgroundColor");

            $('.noti').html('Background color has been changed.');
            $('.noti').fadeIn("slow").delay(3000).fadeOut("slow");
        }
    });

    $(".colorInfo").css("cursor", "pointer");

    $(".colorInfo").click(function(){
        navigator.clipboard.writeText(this.innerHTML);
        $('.noti').html('Color has been copy to the clipboard.');
        $('.noti').fadeIn("slow").delay(3000).fadeOut("slow");
    })
</script>

</body>
</html>