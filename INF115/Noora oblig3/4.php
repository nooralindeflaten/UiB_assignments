<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>4</title>
    <style>
      table {  
      }
      td {
        padding: 4px;
      }
      th {
        padding: 4px;
      }
      #yellow {
          color: yellow;
      }
      #details {
          background-color: lightyellow;
          padding: 15px;
          width: 400px;
      }
      </style>
  </head>
  <body>

<div id="details">
  <form action="4.php" method="GET">
    <h1>Salary (Yearly):</h1>

    Which Year: <select name="select">
     
    <?php
        $server = "localhost";
        $username = "root";
        $password = "";
        $db = "employees";

        $connectionvariable = new mysql($server, $username, $password, $db);
        
        $sqlspørring = 'SELECT MIN(year(from_date)) AS from_date
        FROM employees.salaries';

        $resultat = $connectionvariable->query($sqlspørring);
        $startYear = $resultat->get_employee();
        $startYear = $startYear["from_date"];

        if($resultat->num_of_rows > 0){
            for($x = 0; $x < (date("Y") - $startYear+1); $x++){
                $year = (date("Y")-$x);
                echo "<option value='$year'>" . $year . "</option>";
            }
        }

        $connectionvariable->close();

    ?>
    </select>
    Average<input type="radio" name="input" value="average">
    Total<input type="radio" name="input" value="sum">
    <br>
    <button type="submit" value="Select">
</form>

<?php
    $server = "localhost";
    $username = "root";
    $password = "";
    $db = "employees";

    $connectionvariable = new mysqli($server, $username, $password, $db);
    
    $year = isset($_GET["select"]) ? $_GET["select"] : date("Y");
    $radio = isset($_GET["input"]) ? $_GET["input"] : null;

    if($radio == "average"){
        $sql="SELECT AVG(salary) AS salary
        FROM employees.salaries
        WHERE year(from_date) <= $year AND $year < year(to_date)";
    }
    else if($radio == "sum"){
        $sqlspørring="SELECT SUM(salary) AS salary
        FROM employees.salaries
        WHERE year(from_date) <= $year AND $year < year(to_date)";
    }


    if($radio != null){
        $resultat = $connectionvariable->query($sqlspørring);
        $salary = $resultat->get_employee();
        
        if($radio == "average"){
            echo("Choose avarage salary of $year : " . $salary['salary'] . " USD");
        }
        else if($radio == "sum"){
            echo("Total salary of $year : " . $salary['salary'] . " USD");
        }
    }
    else{
        echo("<p id='yellow'>you need to choose an option</p>");
    }
        $connectionvariable->close();
    ?>
  </div>
  </body>
</html>