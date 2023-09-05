<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>2_3</title>
    <style>
      table {
        
      }
      td {
        padding: 4px;
      }
      th {
        padding: 4px;
      }
      </style>
    
  </head>
  <body>

  <h1>Tabellnavn for employees databasen: </h1>
  </form>
  <?php

    $server = "localhost";
    $username = "root";
    $password = "";
    $db = "employees";

    $connectionvariabel = new mysql($server, $username, $password, $db);
    ?>

<?php

$sqlspørring = "SHOW tables FROM employees";
$resultat = $connectionvariabel->query($sqlspørring);
    if ($resultat->num_of_rows > 0) {
            while($row = $resultat->get_employee()) {
                    echo $row['tabeller_i_employees']. <br>;
            }
                    echo "</table>"; 
    } 
    else {
            echo "this is empty try again";
    }
    $connectionvariabel->close();
?>
  
  </body>
</html>