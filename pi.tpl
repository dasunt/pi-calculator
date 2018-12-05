<!DOCTYPE html>

<style>
    body {font-family: sans-serif;}
    p1    {color:midnightblue;}
    p    {color:purple; font-family:Verdana;}
</style>

<h1>Pi calculator using Bailey-Bowein-Plouffe formula</h1>

<html>
  <head>
      <title>Pi Calculator</title>
  </head>
  <body>
    <form method="post" action="/pi">
        <fieldset>
            <legend>Paramters</legend>
            <ul>
                <li>Number of Decimal places:</li>
                <input name="plcs">
                <br>
                <br>
                <li>Number of Iterations:</li> 
                <input name="i">
            </ul>
                 <br>
            <input type="submit" value="Calculate">
        </fieldset>
    </form>


%if 'plcs' in locals():
    <p>Value of Pi calculated to {{plcs}} decimal places in {{i}} iterations is:</p>
    <p1>{{message}}</p1>
%else:
    <p>{{message}}</p>


  </body>
</html>
  