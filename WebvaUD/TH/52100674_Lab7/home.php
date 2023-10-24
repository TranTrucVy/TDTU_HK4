<?php
   session_start();

   $loginPage = 'login.php';
   $logoutPage = 'logout.php';
   if (!isset($_SESSION['user'])) {
      header("Location: $loginPage");
      exit();
   }

   //Đọc thư mục gốc
   $root = './user/' . $_SESSION['user'];
   if (!file_exists($root)) {
      mkdir($root);
   }

   //print_r($_POST);
   //Hàm đệ quy xóa thư mục
   function recDeleteFolder($currentDir) {
      $filesInFolder = scandir($currentDir);
      $numFiles = count($filesInFolder);
      
      for ($i=0; $i<$numFiles; $i++) {
         if ($filesInFolder[$i]=='.' || $filesInFolder[$i]=='..') {
            unset($filesInFolder[$i]);
         }
      }

      for ($i=2; $i<$numFiles; $i++) {
         $currFile = $filesInFolder[$i];
         $deleteFilePath = "$currentDir/$currFile";

         if (is_file($deleteFilePath)) {
            if (file_exists($deleteFilePath)) {
               if (is_file($deleteFilePath)) {
                  unlink($deleteFilePath);
               }
            }
         } else {
            recDeleteFolder($deleteFilePath);
         }
      }
      rmdir($currentDir);
   }

   /* Tạo folder/file, sửa tên folder/file, xóa folder/file */
   if (isset($_POST['action'])) {
      $action = $_POST['action'];
      if ($action=='create-folder') {
         if (isset($_POST['path']) && isset($_POST['folder-name'])) {
            $path = $_POST['path'];
            $name = $_POST['folder-name'];
            $newFolder = "$root/$path/$name";
            mkdir($newFolder);
         }
      } else if ($action=='create-text-file') {
         if (isset($_POST['path']) && isset($_POST['new-file-name'])) {
            $path = $_POST['path'];
            $name = $_POST['new-file-name'];
            $content = $_POST['new-file-content'];
            $createFilePath = "$root$path";
            
            if (file_exists($createFilePath)) {
               file_put_contents("$createFilePath/$name.txt", $content);
            }
         }
      } else if ($action=='rename-file') {
         //print_r($_POST);
         if (isset($_POST['path']) && isset($_POST['old-file-name']) && isset($_POST['new-file-name'])) {
            $path = $_POST['path'];
            $oldName = $_POST['old-file-name'];
            $newName = $_POST['new-file-name'];

            $oldNameFilePath = "$root$path/$oldName";
            $newNameFilePath = "$root$path/$newName";

            if (file_exists($oldNameFilePath)) {
               if (is_file($oldNameFilePath)) {
                  $file_extension = pathinfo($oldNameFilePath, PATHINFO_EXTENSION);
                  rename("$oldNameFilePath", "$newNameFilePath.$file_extension");
               } else {
                  rename("$oldNameFilePath", "$newNameFilePath");
               }
            }
         }
      } else if ($action=='delete-file-folder') {
         if (isset($_POST['path']) && isset($_POST['file-name'])) {
            $path = $_POST['path'];
            $name = $_POST['file-name'];
            $deleteFilePath = "$root$path/$name";

            if (file_exists($deleteFilePath)) {
               if (is_file($deleteFilePath)) {
                  unlink($deleteFilePath);
               } else {
                  recDeleteFolder($deleteFilePath);
               }
            }
         }
      } else if ($action=='download-file') {
         if (isset($_POST['path']) && isset($_POST['download-file-name'])) {
            $path = $_POST['path'];
            $name = $_POST['download-file-name'];
            $downloadFilePath = "$root$path/$name";

            if (file_exists($downloadFilePath)) {
               if (is_file($downloadFilePath)) {
                  header('Content-Description: File Transfer');
                  header('Content-Type: application/octet-stream');
                  header('Content-Disposition: attachment; filename="'.basename($downloadFilePath).'"');
                  header('Expires: 0');
                  //header('Cache-Control: must-revalidate');
                  //header('Pragma: public');
                  header('Content-Length: ' . filesize($downloadFilePath));
                  readfile($downloadFilePath);
                  exit;
               } else {
                  $zipname = "$name.zip";
                  $filesInFolder = scandir($downloadFilePath);
                  $numFiles = count($filesInFolder);
                  for ($i=0; $i<$numFiles; $i++) {
                     if ($filesInFolder[$i]=='.' || $filesInFolder[$i]=='..') {
                        unset($filesInFolder[$i]);
                     }
                  }

                  $zip = new ZipArchive();
                  if ($zip->open($zipname)===TRUE) {
                     foreach ($filesInFolder as $file)
                     {
                        $zip->addFile("$downloadFilePath/$file", $file);
                     }
                     $zip->close();
                  }
                  header("Content-type: application/zip"); 
                  header("Content-Disposition: attachment; filename=$zipname");
                  header("Content-length: " . filesize($zipname));
                  header("Pragma: no-cache"); 
                  header("Expires: 0"); 
                  readfile("$zipname");
               }
            }
         }
      } else if ($action=='upload-file') {
         if ($_FILES["fileupload"]['error'] != 0)
         {
            die("Đã xảy ra lỗi với dữ liệu upload");
         }

         if (isset($_POST['path']) && isset($_FILES["fileupload"])) {
            
            $path = $_POST['path'];
            $name = basename($_FILES["fileupload"]["name"]);
            $downloadFilePath = "$root$path/$name";

            if ($_FILES["fileupload"]['error'] == 0)
            {
               $uploadFileType = pathinfo($downloadFilePath, PATHINFO_EXTENSION);
               $fileNotAllow = array('exe', 'msi', 'sh');
               $maxfilesize   = 20971520; #20 MB = 20971520 Bytes
               
               if (file_exists($downloadFilePath)) {
                  die('File đã tồn tại file trong thư mục');
               } else if ($_FILES["fileupload"]['size']>$maxfilesize) {
                  die('Không thể upload file lớn hơn 20 MB');
               } else if (in_array($uploadFileType, $fileNotAllow)) {
                  die('Các tập tin thực thi (*.exe, *.msi, *.sh) không được phép upload');
               }

               move_uploaded_file($_FILES["fileupload"]["tmp_name"], $downloadFilePath);
            }
         }
      }
   }

   //Đọc thư mục con, nếu kg có thì đọc thư mục hiện tại
   if (isset($_GET['dir'])) {
      $dir = $_GET['dir'];
      $path = "$root/$dir";
      if (!file_exists($path) || !is_dir($path)) {
         die("Không tồn tại thư mục");
      }
   } else {
      $dir = '';
      $path = $root;
   }
   $fileList = scandir($path);
?>


<!DOCTYPE html>
<html lang="en">
<head>
   <title>Lab 8 - Web Programming</title>
   <meta charset="utf-8">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
   <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
   <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
   <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
   <style>
      var {
         font-style: normal;
      }

      .fa,
      .fas {
         color: #858585;
      }

      .fa-folder {
         color: rgb(74, 158, 255);
      }

      i.fa,
      table i.fas {
         font-size: 16px;
         margin-right: 6px;
      }

      i.action {
         cursor: pointer;
      }

      a {
         color: black;
      }
   </style>
</head>
<?php
   $iconTypes = [
      'zip' => '<i class="fas fa-file-archive"></i>',
      'rar' => '<i class="fas fa-file-archive"></i>',
      'jpg' => '<i class="fas fa-file-image"></i>',
      'jpeg' => '<i class="fas fa-file-image"></i>',
      'png' => '<i class="fas fa-file-image"></i>',
      'bmp' => '<i class="fas fa-file-image"></i>',
      'mp3' => '<i class="fas fa-file-audio"></i>',
      'doc' => '<i class="fas fa-file-word"></i>',
      'docx' => '<i class="fas fa-file-word"></i>',
      'pdf' => '<i class="fas fa-file-pdf"></i>',
      'mp4' => '<i class="fas fa-file-video"></i>',
      'mkv' => '<i class="fas fa-file-video"></i>',
      'mov' => '<i class="fas fa-file-video"></i>',
      'html' => '<i class="fas fa-file-code"></i>',
      'css' => '<i class="fas fa-file-code"></i>',
      'php' => '<i class="fas fa-file-code"></i>'
   ];
   $fileTypes = [
      'txt' => 'Text',
      'zip' => 'Compressed File',
      'rar' => 'Compressed File',
      'jpg' => 'Image',
      'jpeg' => 'Image',
      'png' => 'Image',
      'bmp' => 'Image',
      'mp3' => 'Audio',
      'doc' => 'Microsoft Word 2003',
      'docx' => 'Microsoft Word 2010',
      'pdf' => 'PDF Document',
      'mp4' => 'Video',
      'mkv' => 'Video',
      'mov' => 'Video',
      'html' => 'HTML Document',
      'css' => 'CSS Document',
      'php' => 'PHP Document'
   ];

   function byteTransform($bytes) {
      $units = array('Bytes', 'KB', 'MB', 'GB', 'TB'); 
      $newSize = $bytes;
      $count = 0;
      while ($newSize>=1024) {
         $newSize = round($newSize/1024, 1);
         $count += 1;
      }
      return strval($newSize) . " " . $units[$count];
  } 

   function sortFiles($listcontent, $path) {
      $folders = [];
      $files = [];

      foreach ($listcontent as $content) {
         if ($content!='.' && $content!='..') {
            $f = "$path/$content";
            if (is_dir($f)) {
               $folders[] = $content;
            } else {
               $files[] = $content;
            }
         }
      }
      natcasesort($files);
      return array_merge($folders, $files);
   }
?>

<!---------------- SUPPORT JAVASCRIPT FUNCTIONS ---------------->
<script>
   function changeDeleteFileName(filename) {
      let label = document.getElementById("file-delete");
      let param = document.getElementById("file-delete-input");
      
      label.innerHTML = filename;
      param.value = filename;

      let tmp = document.getElementById("folder-or-file");
      let check = filename.split(".");
      if (check.length===1) {
         tmp.innerHTML = "thư mục";
      } else {
         tmp.innerHTML = "tập tin";
      }
   }

   function changeFileName(filename) {
      let label = document.getElementById("old-name-display");
      let param = document.getElementById("old-name-input");

      label.innerHTML = filename;
      param.value = filename;
   }

   function downloadFile(filename) {
      let label = document.getElementById("download-file-display");
      let param = document.getElementById("download-file-input");

      label.innerHTML = filename;
      param.value = filename;
   }

   function changeUploadName(inputBox) {
      let val = inputBox.value;
      let filename = val.split("\\").at(-1);

      let displayUpload = document.getElementById("display-file-upload");
      displayUpload.innerHTML = filename;
   }
</script>

<?php $fileList = sortFiles($fileList, $path); ?>

<body>
   <!------------------ CONTENT OF PAGE ------------------>
   <div class="container">
      <!--Tiêu đề-->
      <div class="row align-items-center py-5">
         <div class="col-6">
            <h3>
               File Manager</h2>
         </div>
         <div class="col-6">
            <h5 class="text-right">Xin chào <?=$_SESSION['user']?>, <a class="text-primary" href="<?= $logoutPage ?>">Logout</a></h5>
         </div>
      </div>

      <!--Thanh hiển thị đường dẫn thư mục hiện tại-->
      <ol class="breadcrumb">
         <li class="breadcrumb-item"><a href="/">Home</a></li>
         <?php
            $dirSequences = explode('/', $dir);
            $dirURL = "?dir=";
            for ($i=0; $i<count($dirSequences); $i++) {
               $dirName = $dirSequences[$i];
               if (empty($dirName)) {
                  continue;
               }
               if ($i==0) {
                  $dirURL = "$dirURL";
               } else {
                  $dirURL = "$dirURL/$dirName";
               }

               if ($i==count($dirSequences)-1) {
                  $activeState = 'active';
               } else {
                  $activeState = '';
               }
               echo "<li class='breadcrumb-item $activeState'><a href='$dirURL'>$dirName</a></li>";
            }
         ?>
      </ol>

      <!--Thanh tìm kiếm-->
      <div class="input-group mb-3">
         <div class="input-group-prepend">
            <span class="input-group-text">
               <span class="fa fa-search"></span>
            </span>
         </div>
         <input type="text" class="form-control" placeholder="Search">
      </div>

      <!--Nút tạo folder/text file mới-->
      <div class="btn-group my-3">
         <button type="button" class="btn btn-light border" data-toggle="modal" data-target="#new-folder-dialog">
            <i class="fas fa-folder-plus"></i> New folder
         </button>
         <button type="button" class="btn btn-light border" data-toggle="modal" data-target="#new-file-dialog">
            <i class="fas fa-file"></i> Create text file
         </button>
      </div>

      <!--Hiển thị danh sách file-->
      <table class="table table-hover border">
         <thead>
            <tr>
               <th>Name</th>
               <th>Type</th>
               <th>Size</th>
               <th>Last modified</th>
               <th>Actions</th>
            </tr>
         </thead>
         <tbody>
            <?php
               foreach ($fileList as $fname) {
                  $filepath = "$path/$fname";
                  if (is_dir($filepath)) {
                     $icon = '<i class="fa fa-folder"></i>';
                     $type = 'Folder';
                     $fpath = "?dir=" . $dir . "/" . $fname;
                     $size = "-";
                  } else {
                     $fileExtension = pathinfo($fname, PATHINFO_EXTENSION);

                     if (array_key_exists($fileExtension, $iconTypes)) {
                        $icon = $iconTypes[$fileExtension];
                     } else {
                        $icon = '<i class="fas fa-file"></i>';
                     }

                     if (array_key_exists($fileExtension, $fileTypes)) {
                        $type = $fileTypes[$fileExtension];
                     } else {
                        $type = 'File';
                     }
                     
                     $fpath = $filepath;
                     $size = byteTransform(filesize($filepath));
                  }
                  $modify = date("d-m-Y", filemtime($filepath));
                  ?>
                     <tr>
                        <td>
                           <?=$icon?>
                           <a href="<?=$fpath?>"><?=$fname?></a>
                        </td>
                        <td><?=$type?></td>
                        <td><?=$size?></td>
                        <td><?=$modify?></td>
                        <td>
                           <i onclick="downloadFile('<?=$fname?>')" 
                              class="fa fa-download action" data-toggle="modal"
                              data-target="#confirm-download"></i>
                           <i onclick = "changeFileName('<?=$fname?>')"
                              class="fa fa-edit action" data-toggle="modal"
                              data-target="#confirm-rename"></i>
                           <i onclick="changeDeleteFileName('<?=$fname?>')" 
                              class="fa fa-trash action" data-toggle="modal"
                              data-target="#confirm-delete"></i>
                        </td>
                     </tr>
                  <?php
               }
            ?>
         </tbody>
      </table>

      <!--Tùy chọn upload file-->
      <div class="border rounded mb-3 mt-5 p-3">
         <h4>File upload</h4>
         <form method="POST" enctype="multipart/form-data">
            <div class="form-group">
               <div class="custom-file">
                  <!--value="fileupload"-->
                  <input onchange="changeUploadName(this)" type="file" name="fileupload" class="custom-file-input" id="customFile">
                  <label id="display-file-upload" class="custom-file-label" for="customFile">Choose file</label>
               </div>
            </div>
            <p>Người dùng chỉ được upload tập tin có kích thước tối đa là 20 MB.</p>
            <p>Các tập tin thực thi (*.exe, *.msi, *.sh) không được phép upload.</p>
            <p><strong>Yêu cầu nâng cao</strong>: hiển thị progress bar trong quá trình upload.</p>
            <input type="hidden" name="action" value="upload-file">
            <input type="hidden" name="path" value="<?=$dir?>">
            <button type="submit" class="btn btn-success px-5">Upload</button>
         </form>
      </div>
      
      <!--Ví dụ về sử dụng modals - một số dialog mẫu-->
      <div class="modal-example my-5">
         <h4>Một số dialog mẫu</h4>
         <p>Nhấn vào để xem kết quả</p>
         <ul>
            <li><a href="#" data-toggle="modal" data-target="#confirm-delete">Confirm delete</a></li>
            <li><a href="#" data-toggle="modal" data-target="#confirm-rename">Confirm rename</a></li>
            <li><a href="#" data-toggle="modal" data-target="#new-file-dialog">New file dialog</a></li>
            <li><a href="#" data-toggle="modal" data-target="#message-dialog">Message Dialog</a></li>
            <li><a href="#" data-toggle="modal" data-target="#new-folder-dialog">New folder Dialog</a></li>
         </ul>
      </div>

   </div>
   

   <!------------------ DIALOGS ------------------>
   <!-- Tao folder dialog -->
   <div class="modal fade" id="new-folder-dialog">
      <div class="modal-dialog">
         <div class="modal-content">
            <form method="POST">

               <div class="modal-header">
                  <h4 class="modal-title">Tạo thư mục</h4>
                  <button type="button" class="close" data-dismiss="modal">&times;</button>
               </div>

               <div class="modal-body">
                  <!--<p>Bạn không được cấp quyền để xóa tập tin/thư mục này</p>-->
                  <div class="form-group">
                     <label for="name">Folder name</label>
                     <input name="folder-name" type="text" placeholder="File name" class="form-control">
                  </div>
               </div>

               <div class="modal-footer">
                  <input type="hidden" name="action" value="create-folder">
                  <input type="hidden" name="path" value="<?=$dir?>">
                  <button type="submit" class="btn btn-success">Lưu</button>
               </div>
            </form>
         </div>
      </div>
   </div>

   <!-- Delete dialog -->
   <div class="modal fade" id="confirm-delete">
      <div class="modal-dialog">
         <div class="modal-content">
            <form method="POST">
               <div class="modal-header">
                  <h4 class="modal-title">Xóa tập tin</h4>
                  <button type="button" class="close" data-dismiss="modal">&times;</button>
               </div>

               <div id="delete-question" class="modal-body">
                  Bạn có chắc rằng muốn xóa <var id="folder-or-file">tập tin</var> <strong id="file-delete">image.jpg</strong>
               </div>

               <div class="modal-footer">
                  <input type="hidden" name="action" value="delete-file-folder">
                  <input type="hidden" name="path" value="<?=$dir?>">
                  <input type="hidden" name="file-name" id="file-delete-input" value="">
                  <button type="submit" class="btn btn-danger">Xóa</button>
                  <button type="button" class="btn btn-secondary" data-dismiss="modal">Không</button>
               </div>
            </form>
         </div>
      </div>
   </div>

   <!-- New file dialog -->
   <div class="modal fade" id="new-file-dialog">
      <div class="modal-dialog">
         <div class="modal-content">
            <form method="POST">
               <div class="modal-header">
                  <h4 class="modal-title">Tạo tập tin mới</h4>
                  <button type="button" class="close" data-dismiss="modal">&times;</button>
               </div>

               <div class="modal-body">
                  <div class="form-group">
                     <label for="new-file-name">File Name</label>
                     <input name="new-file-name" type="text" placeholder="File name" class="form-control" id="new-file-name" />
                  </div>
                  <div class="form-group">
                     <label for="new-file-content">Nội dung</label>
                     <textarea name="new-file-content" rows="10" id="new-file-content" class="form-control" placeholder="Nội dung"></textarea>

                  </div>
               </div>

               <div class="modal-footer">
                  <input type="hidden" name="action" value="create-text-file">
                  <input type="hidden" name="path" value="<?=$dir?>">
                  <button type="submit" class="btn btn-success">Lưu</button>
               </div>
            </form>
            
         </div>
      </div>
   </div>

   <!-- Rename dialog -->
   <div class="modal fade" id="confirm-rename">
      <div class="modal-dialog">
         <div class="modal-content">
            <form method="POST">
               <div class="modal-header">
                  <h4 class="modal-title">Đổi tên</h4>
                  <button type="button" class="close" data-dismiss="modal">&times;</button>
               </div>

               <div class="modal-body">
                  <p>Nhập tên mới cho tập tin <strong id="old-name-display">Document.txt</strong></p>
                  <input name="new-file-name" type="text" placeholder="Nhập tên mới" class="form-control"/>
               </div>

               <div class="modal-footer">
                  <input type="hidden" name="action" value="rename-file">
                  <input type="hidden" name="path" value="<?=$dir?>">
                  <input type="hidden" name="old-file-name" id="old-name-input" value="">
                  <button type="submit" class="btn btn-primary">Lưu</button>
               </div>
            </form>
         </div>
      </div>
   </div>

   <!-- Download dialog -->
   <div class="modal fade" id="confirm-download">
      <div class="modal-dialog">
         <div class="modal-content">
            <form method="POST">
               <div class="modal-header">
                  <h4 class="modal-title">Download file</h4>
                  <button type="button" class="close" data-dismiss="modal">&times;</button>
               </div>

               <div class="modal-body">
                  <p>Xác nhận tải file <strong id="download-file-display">Document.txt</strong>?</p>
               </div>

               <div class="modal-footer">
                  <input type="hidden" name="action" value="download-file">
                  <input type="hidden" name="path" value="<?=$dir?>">
                  <input type="hidden" name="download-file-name" id="download-file-input" value="">
                  <button type="submit" class="btn btn-primary">Lưu</button>
               </div>
            </form>
         </div>
      </div>
   </div>


   <!-- message dialog 
   <div class="modal fade" id="message-dialog">
      <div class="modal-dialog">
         <div class="modal-content">

            <div class="modal-header">
               <h4 class="modal-title">Xóa file</h4>
               <button type="button" class="close" data-dismiss="modal">&times;</button>
            </div>

            <div class="modal-body">
               <p>Bạn không được cấp quyền để xóa tập tin/thư mục này</p>
            </div>

            <div class="modal-footer">
               <button type="button" class="btn btn-info" data-dismiss="modal">Đóng</button>
            </div>
         </div>
      </div>
   </div>-->
</body>

</html>