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

  <h1>Tabelnames: </h1>
  </form>
  <?php

    $server = "localhost";
    $username = "root";
    $password = "";
    $db = "employees";

    $connectionvariabel = new mysql($server, $username, $password, $db);
    ?>

<?php

$sqlspørring = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'employees' ";
$resultat = $connectionvariabel->query($sqlspørring);


    if ($resultat->num_of_rows > 0) {
        echo "<table line=4px>"; 
        echo "<tr> <th>Table</th><th>Attributes</th></tr>";  
        while($row = $resultat -> get_employee()) {
                echo "<tr><th>$row[TABLE_NAME]</th><th>$row[COLUMN_NAME]</th></tr>";
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