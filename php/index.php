<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>php</title>
</head>
<body>
    <h1>text-to-html</h1>
    resultado:
    <?php
    $input = "input.txt";
    $file = fread(fopen($input, "r"),filesize($input));
    $output = str_replace("\n", "<br>", $file );
    echo $output;
    ?>
</body>
</html>