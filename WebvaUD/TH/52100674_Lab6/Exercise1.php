<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lab6 - Exercise1</title>
    <style>
        * {
            box-sizing: border-box;
        }

        table {
            border-collapse: collapse;
            margin: auto;
        }

        table th, td {
            border: 1px solid black;
        }

        th {
            background-color: #c9c9c9;
            padding: 5px;
        }

        td {
            text-align: center;
            padding: 5px;
        }
    </style>
</head>
<body>
    <table border="1">
        <th colspan="10">BẢNG CỬU CHƯƠNG</th>
        <?php
            for ($row=1; $row<=10; $row++) {
                echo "<tr>";
                for ($col=1; $col<=10; $col++) {
                    $c = $col*$row;
                    echo "<td>$col x $row = $c</td>";
                }
                echo "</tr>";
            }
        ?>
    </table>
</body>
</html>