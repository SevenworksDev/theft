<?php
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    if (filter_var($_GET['url'], FILTER_VALIDATE_URL) === false || !strpos($_GET['url'], 'catbox.moe')) { exit; }
    $file = 'links.txt';
    file_put_contents($file, $_GET['url'] . PHP_EOL, FILE_APPEND);
} else {
    exit;
}
?>