<?php
$target_dir = "./UploadFiles/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));

if (file_exists($target_file)) {
  echo "Sorry, file already exists.";
} else if ($_FILES["fileToUpload"]["size"] > 5242880) {
  echo "Sorry, your file is too large.";
} else if ($imageFileType != "jpg" && $imageFileType != "mp3" && $imageFileType != "mp4") {
  echo "Sorry, only JPG, JPEG, MP3 & MP4 files are allowed.";
} else if ($uploadOk == 0) {
  echo "Sorry, your file was not uploaded.";
} else if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
  echo "The file " . htmlspecialchars(basename($_FILES["fileToUpload"]["name"])) . " has been uploaded.";
} else {
  echo "Sorry, there was an error uploading your file.";
}
