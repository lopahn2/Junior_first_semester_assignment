<?php
session_start();
$inactive = 10;

if(isset($_SESSION["timeout"])){
    $sesstionTTL = time() - $_SESSION["timeout"];
    if($sesstionTTL> $inactive){
        session_destroy();
        echo "Time is up...";
    }else{
        echo "We have time to timeout". $sesstionTTL. " seconds are passed";
    }
}else{
    $_SESSION["timeout"] = time();
    echo "Timeout is set with current time.";
}
?>