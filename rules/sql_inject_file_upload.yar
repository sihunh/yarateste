rule PHP_GET_POST_SQL
{
  meta:
    author      = "Moath Maharmeh"
    date        = "2021/Jul/7"
    description = "Find PHP scripts contains $_GET $_POST - possible SQL Injection vulns"
    filetype    = "php"
  strings:
    $p1 = "<?"

    $s1 = "$_GET["
    $s2 = "$_POST["

    $d1 = "mysql_query("
    $d2 = "mysqli_query"
    $d3 = "mssql_query"
    $d4 = "sqlsrv_query"
  condition:
    $p1 at 0 and any of ($s*) and any of ($d*)
}


rule PHP_GET_POST_FILE_UPLOAD
{
  meta:
    author      = "Moath Maharmeh"
    date        = "2021/Jul/7"
    description = "Find PHP scripts contains $_GET $_POST - possible File Upload vulns"
    filetype    = "php"
  strings:
    $p1 = "<?"

    $s1 = "$_POST["

    $d1 = "move_uploaded_file"
    $d2 = "file_put_contents"
    $d3 = "fwrite("

    $n1 = "php://input"
  condition:
    $p1 at 0 and ( ($s1 and any of ($d*)) or ($n1 and any of ($d*)) )
}