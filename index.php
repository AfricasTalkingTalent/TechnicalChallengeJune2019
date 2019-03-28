<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Home | Site</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <?php include 'assets/php/_css.php' ?>
</head>
<body>
    <div class="container body-content">
        <input class="form-control search" type="search" id="search" name="search" placeholder="Type here to search...">
        <table role='table' class='table table-borderless table-hover'>
            <tr>
                <th>Name</th>
                <th>Size</th>
            </tr>
            <?php
                // Scan and display all files in /documents directory.
                $dir = "documents/";
                $files = scandir($dir);
                $exclude = array(".", ".."); // Directories to exclude
                if (sizeof(array_diff($files, $exclude)) > 0) foreach ($files as $file){
                    if (in_array($file, $exclude)) continue; // skip "." and ".." directories
                    $path = $dir.$file; // filepath
                    $filesize = filesize($path); // filesize
                    echo 
                    "<tr>
                        <td>$file</td>
                        <td>$filesize bytes</td>
                    </tr>";
                } else echo "<tr><td colspan='2' class='text-center'>Nothing to display</td></tr>";
            ?>
        </table>
    </div>
    <?php include 'assets/php/_js.php'?>
</body>
</html>