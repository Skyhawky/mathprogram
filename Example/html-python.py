name  = input("enter your name here:")
age  = input("enter your age here:")
html = """
<div style = "background-color:blue">
<p>Hello this is my website :D</p>
</div>
<div style ="background-color:green">
<p>The name you entered is:{} </p><br>
<p>The age you entered is:{} </p>
""".format(name, age)
f = open("myWeb.html", "w")
f.write(html)
f.close()
import os
os.system("start myWeb.html")