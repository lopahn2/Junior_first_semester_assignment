<?php
function IsPrime($n){
    for($x=2; $x<$n; $x++){
        if($n % $x ==0){
            return 0;
        }

    }
    return 1;
}

for($i = 3; $i <= 10; $i++){
    $a = IsPrime($i);
    if($a ==0){
        echo "$i is not a prime..."."<br>";
    }else{
        echo "$i is  a prime..."."<br>";
    }
}
?>
<?php
function reverse_string($str){
    $n = strlen($str);
    if($n == 1){
        return $str;
    }else{
        $n--;
        return reverse_string(substr($str,1,$n)).substr($str,0,1);
    }
}

$reversed_string = reverse_string("abcdefg");
echo $reversed_string;
?>