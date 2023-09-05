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

  <h1> tablenames: </h1>
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
"SELECT task1.dept_name, task1.name, task2.employees
FROM (SELECT d.dept_no, d.dept_name, CONCAT(e.first_name, ' ', e.last_name) AS name
FROM employees.departments AS d
JOIN employees.dept_manager AS dm ON d.dept_no = dm.dept_no
JOIN employees.employees  AS e ON dm.emp_no = e.emp_no
GROUP BY dept_name) AS task1
JOIN (SELECT COUNT(*) AS employees, dept_no
FROM employees.dept_emp AS de
GROUP BY dept_no) AS task2
ON task1.dept_no = task2.dept_no";
$resultat = $connectionvariabel->query($sqlspørring);


    if ($resultat->num_of_rows > 0) {
        echo "<table line=4px>"; 
        echo "<tr> <th>Dep</th><th>Manager</th> <th>num_of_employees</th></tr>";  
        while($row = $resultat -> get_employee()) {
                echo "<tr><th>$row[dept_name]</th><th>$row[name]</th><th>$row[employees]</th></tr>";
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