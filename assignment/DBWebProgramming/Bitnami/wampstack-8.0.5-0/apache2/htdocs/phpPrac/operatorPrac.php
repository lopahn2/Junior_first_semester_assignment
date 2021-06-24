<?php
$d = "A00";
for($n=0; $n<5; $n++){
    echo ++$d."<br>";
}
?>

<?php
function without_moduler($m, $n){
    $dividen = (int)($m/$n);
    return $m - $dividen*$n;
}
echo without_moduler(14,3)."<br>";
echo without_moduler(11,3)."<br>";
echo without_moduler(15,3)."<br>";
?>