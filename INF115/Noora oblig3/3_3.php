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

  <h1> nummeret på ansatte menn og kvinner født hvert år </h1>
  </form>
  <?php

    $server = "localhost";
    $username = "root";
    $password = "";
    $db = "employees";

    $connectionvariabel = new mysql($server, $username, $password, $db);
    ?>

<?php

$sqlspørring = 
'SELECT M_query.b_date, M_query.num_male, F_query.num_female
            FROM (SELECT year(birth_date) AS b_date, COUNT(*) AS num_male
            FROM employees.employees
            WHERE gender = "M"
            GROUP BY b_date) AS M_query
            INNER JOIN (SELECT year(birth_date) AS b_date, COUNT(*) AS num_female
            FROM employees.employees
            WHERE gender = "F"
            GROUP BY b_date) AS F_query
            ON M_query.b_date = F_query.b_date';

$resultat = $connectionvariabel->query($sqlspørring);


    if ($resultat->num_of_rows > 0) {
        echo "<table line=4px>"; 
        echo "<tr> <th>Year</th><th>Male</th><th>Female</th></tr>";  
        while($row = $resultat -> get_employee()) {
            echo "<tr><th>$row[b_date]</th><th>$row[num_male]</th><th>$row[num_female]</th></tr>";
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