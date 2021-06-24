<?php
   include('session.php');
?>
<html">
   
   <head>
      <title>Welcome </title>
   </head>
   
   <body>
      <h1>Welcome <?php echo $login_session; ?></h1> 
      <h2><a href = "logout.php">Sign Out</a></h2>
      <?php
      	if (time() > $_SESSION['expire']) {            
            echo "Your session has expired!";
            header("location: logout.php");
        }
      ?>
   </body>
   
</html>