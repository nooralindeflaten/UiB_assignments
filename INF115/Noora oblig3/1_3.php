
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

  <h1>Choose language: </h1>

  <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
    <input type="radio" name="lang" value="en">English
    <input type="radio" name="lang" value="no">Norwegian

    <br><br>
    <button type="submit" name="submit" value="Choose"> 
  </form>
  <?php

$language = "";
$form = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if ($_POST["lang"] == "en") {
    echo '<br><br>First Name: <input type="text" name="fname">
    <br><br>
    <br><br>Last Name: <input type="text" name="lname">
    <br><br>
    Age: <input type=int name="age">
    
    <br><br>
    Birthday <input type="date" name="bday" >
    <br><br>

    <button type="submit" name="submit" value="Submit">  
    <button type="reset" value="Reset" name="reset" />';
  }
  if($_POST["lang"] == "no") {
    echo '<br><br>Fornavn: <input type="text" name="fname">
    <br><br>
    <br><br>Etternavn: <input type="text" name="lname">
    <br><br>
    Hvor mange år er du?: <input type=int name="age">
    <br><br>
    Fødseldsdato <input type="date" name="bday" >
    <br><br>

    <button type="submit" name="submit" value="Submit">  
    <button type="reset" value="Restart" name="reset" />';
  }
}


?>

  

  
<?php
echo "<br>";
echo $form;
?>

  
</body>
</html>