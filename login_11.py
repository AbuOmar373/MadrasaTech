site="www.madrasatech.com/admin/login.php"

login=['admin/','adinistrator/','admin1/','admin2/','memberadmin/','aministratorlogin/',
       'webadmin/index.html','admin/cp.php','admin/login.php','adminarea/admin.php',
       'adm/index.php','adm.php','affiliate.php','adminstratorlogin.php']

target=input("Enter website to scan:") # http://www.madrasatech.com/
target=target.replace("http://","") # اقتصاص النص

for each in login:
      final_website=target+each
      if final_website==site:
            print("Admin login page found ==>", final_website)
            break;
      else:
            print("Admin page not found")
