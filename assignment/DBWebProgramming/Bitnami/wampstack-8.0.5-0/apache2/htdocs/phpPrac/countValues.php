<?php
function count_array_values($my_array, $match){
    $count = 0;
    foreach ($my_array as $key => $value){
        if($value == $match){
            $count++;
        }
    }
    return $count;
}

$colors = array("c1"=>"Red", "c2"=>"Green", "c3"=>"Yellow","c4"=>"Red");

echo "red color appears ".count_array_values($colors,"Red")." times";