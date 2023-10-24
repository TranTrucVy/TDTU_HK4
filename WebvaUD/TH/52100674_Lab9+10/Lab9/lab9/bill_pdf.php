<?php
    require('./fpdf183/fpdf.php');
    require('connect.php');
    session_start();

    $pdf = new FPDF();
    $pdf->AddPage();
    $pdf->SetFont('Arial','B',20);
    $pdf->Cell(0,10,"Invoice",0,0,'C');
    $pdf->Ln();
    $pdf->Ln();
    $pdf->SetFont('Arial','B',13);
    $pdf->Cell(20,10,"STT",1,0,'C');
    $pdf->Cell(70,10,"Product Name",1,0,'C');
    $pdf->Cell(20,10,"Quantity",1,0,'C');
    $pdf->Cell(40,10,"Price",1,0,'C');
    $pdf->Cell(40,10,"Total",1,1,'C');

    $sql = "SELECT * FROM `bill`";
    $sql_run = mysqli_query($con,$sql);
    while($row = $sql_run->fetch_array(MYSQLI_ASSOC)){
        $stt = $row['stt'];
        $name = $row['pro_name'];
        $quantity = $row['quantity'];
        $price = $row['price'];
        $total = $row['total'];

        $pdf->SetFont('Arial','',12);
        $pdf->Cell(20,10,$stt,1,0,'C');
        $pdf->Cell(70,10,$name,1,0);
        $pdf->Cell(20,10,$quantity,1,0,'C');
        $pdf->Cell(40,10,number_format($price,0,',','.')." VND",1,0,'C');
        $pdf->Cell(40,10,number_format($total,0,',','.')." VND",1,0,'C');
        $pdf->Ln();
    }

    $pdf->Output();

    $sql_bill = "DELETE FROM `bill`";
    $sql_run = mysqli_query($con,$sql_bill);
?>
