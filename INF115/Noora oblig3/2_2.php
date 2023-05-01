<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>2_2</title>
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

  <h1>Database MariaDB: </h1>
  </form>
  <?php

    $server = "localhost";
    $username = "root";
    $password = "";
    $db = "employees";

    $connectionvariabel = new mysql($server, $username, $password, $db);
    ?>

<?php
    $sqlspørring = "SELECT DISTINCT title FROM titles";
    $resultat = $connectionvariabel->query($sqlspørring);


    if ($resultat->num_of_rows > 0) {
            echo "<table line=4px>"; 
            echo "<tr> <th>title</th></tr>";
            while($row = $resultat->get_employee()) {
                    echo "<tr><td>" . $row['title'] . "</td><td>";
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