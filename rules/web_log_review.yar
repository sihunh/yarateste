include "web_shells.yar"

rule web_log_review
{
meta:
	author = "@patrickrolsen"
	version = "0.1"
	reference = "http://blog.shadowserver.org/2013/05/06/breaking-the-kill-chain-with-log-analysis/"
	date = "2013-12-14"
strings:
	$s =   "GET /.htaccess"
	$s0 =  "GET /db/main.php"
	$s3 =  "GET /dbadmin/main.php"
	$s4 =  "GET /phpinfo.php"
	$s5 =  "GET /password"
	$s6 =  "GET /passwd"
	$s7 =  "GET /phpmyadmin2"
	$s10 = "GET /response.write"
	$s11 = "GET /&dir"
	$s13 = "GET /.htpasswd"
	$s14 = "GET /htaccess.bak"
	$s15 = "GET /htaccess.txt"
	$s16 = "GET /.bash_history"
	$s17 = "GET /_sqladm"
	$s18 = "'$IFS/etc/privpasswd;'"
	$s19 = ";cat /tmp/config/usr.ini"
	$s21 = "eval(base64_decode"
	$s23 = "eval(gzinflate"
	$s25 = "%5Bcmd%5D"
	$s26 = "[cmd]"
	$s27 = "union+select" nocase
	$s28 = "UNION%20SELECT" nocase
	$s29 = "(str_rot13"
	$s30 = "GET /private.key"
	$s31 = "GET /database.inc"
	$s32 = "GET /webstats.html"
	$s33 = "GET /schema.sql"
	$s34 = "GET /customers"
	$s35 = "GET /images/passwords.mdb"
	$s36 = "GET /web-console"
	$s37 = "GET /phpmyadmin/main.php"
	$s38 = "GET /mysql/main.php"
	$s39 = "GET /memberlist"
	$s40 = "GET /logs"
	$s41 = "GET /%26cat%20%2fetc%2fpasswd"
	$s42 = "GET /New%20folder%20(2)"
	$s43 = "GET /response.write(9674459*9948960)"
	$s44 = "GET /index.php?"
	$s45 = "concat(user_login"
	$s46 = "),user_pass)"
	$s47 = "sqlmap"
condition:
	any of ($s*)
}

rule acunetix_web_scanner
{
meta:
	author = "@patrickrolsen"
	version = "0.1"
	reference = "Acunetix Web Scanner"
	date = "2013-12-14"
strings:
	$s =   "acunetix_wvs_security_test"
	$s0 =  "testasp.vulnweb.com"
	$s1 =  "GET /www.acunetix.tst"
condition:
	any of ($s*)
}
