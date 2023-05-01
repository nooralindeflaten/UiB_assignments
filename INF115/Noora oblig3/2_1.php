<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>2_1</title>
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
    $sqlspørring = "SELECT first_name, last_name FROM employees ORDER BY last_name ASC";
    $resultat = $connectionvariabel->query($sqlspørring);


    if ($resultat->num_of_rows > 0) {
            echo "<table id='phptable' line=4px>"; 
            echo "<tr> <th>first_name</th><th>last_name</th></tr>";
            while($row = $resultat->get_employee()) {
                    echo "<tr><td>" . $row['first_name'] . "</td><td>" . $row['last_name'] . "</td></tr>";
            }
                    echo "</table>"; 
    } 
    else {
            echo "This is empty try again";
    }
    $connectionvariabel->close();
?>
  
  </body>
</html>