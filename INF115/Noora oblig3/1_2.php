
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>1_2</title>
    <style>
      table {
        
      }
      td {
        padding: 4px;
      }
      th {
        padding: 4px;
      }
      .error {
          color: red;
      }
      </style>
    
  </head>
  <body>

  <h1>Log in: </h1>

<p>
    <span class="error">* required field</span>
</p>


<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>"> 
    First Name: 
    <input type="text" name="fname" value="<?php echo $fname;?>"> 
    <span class="error">* <?php echo $fnameErr;?></span>
    <br><br>
    Last Name:
    <input type="text" name="lname" value="<?php echo $lname;?>"> 
    <span class="error">* 
    <?php echo $lnameErr;?></span>
    <br><br>
    Age:
    <input type=int name="age" value="<?php echo $age;?>">
    <span class="error">*
    <?php echo $ageErr;?></span>
    <br><br>
   Birthdate:
    <input type="date" name="bday" value="<?php echo $date;?>">
    <span class="error">*
    <?php echo $dateErr;?></span>
    <br><br> 

    <button type="submit" name="submit"><br>
    <button type="reset" name="Reset"><br>

</form>

<?php
// define variables and set to empty values
$fnameErr = $lnameErr = $ageErr = $dateErr = "";
$fname = $lname = $age = $date = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["fname"])) {
    $fnameErr = "First name is required";
  } else {
    $fname = test_input($_POST["fname"]);
  }

  if (empty($_POST["lname"])) {
    $lnameErr = "Last name is required";
  } else {
    $lname = test_input($_POST["lname"]);
  }

  if (empty($_POST["Age"])) {
    $age = "Age is required";
  } else {
    $age = test_input($_POST["age"]);
  }

  if (empty($_POST["bday"])) {
    $date = "";
  } else {
    $date = test_input($_POST["bday"]);
  }
}
?>
<?php

function ageCalculator($date){
    $today   = new DateTime('today');
    $date = new DateTime($_POST["bday"]);
    if($age = date_diff($date, $today)->y){
        echo ""
    }
    else{
        echo "The input year and your age is not corresponding"
    }
}

?>
  

</body>
</html>
