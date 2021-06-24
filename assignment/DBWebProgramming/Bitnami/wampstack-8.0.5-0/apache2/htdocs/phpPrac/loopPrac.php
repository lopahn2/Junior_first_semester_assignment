<?php
for($x=1; $x<=10; $x++){
    if($x<10){
        echo "$x-";
    }else{
        echo "$x";
    }
}
echo "<br>";
?>
<?php
$n = 5;
for($x=1; $x<=$n; $x++){
    for($j=1; $j<=$x; $j++){
        echo " * ";
    }
    echo "<br>";
}
for($x=$n; $x>=1; $x--){
    for($j=1; $j<=$x; $j++){
        echo " * ";
    }
    echo "<br>";
}
?>