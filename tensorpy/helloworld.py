#!/home/ubuntu/anaconda2/envs/tf1.1_py2.7/bin/python
import cgitb
import cgi
import playfile

cgitb.enable()

print("Content-type: text/html")
print("")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<title>TensorWeb Music</title>")

print("<meta charset=\"utf-8\"/>")

print(
"<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/jquery.swipebox/1.4.1/css/swipebox.min.css\">")
print("<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/normalize/3.0.3/normalize.min.css\"/>")
print("<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css\"/>")
print("<link rel=\"stylesheet\" href=\"../tensorweb/css/main.css\">")
print("<link rel=\"stylesheet\" href=\"../tensorweb/css/gallery.css\">")

print("<script src=\"https://code.jquery.com/jquery-1.11.3.min.js\"></script>")
print(
"<script src=\"https://cdnjs.cloudflare.com/ajax/libs/jquery.swipebox/1.4.1/js/jquery.swipebox.min.js\"></script>")
print("<script>")
print("$('.swipebox').swipebox();")
print("</script>")

print("</head>")

print("<body>")

print("<div class=\"header\"> ")
print("<h1>TensorWeb Music</h1>")
print("</div>")

print("<div class=\"formsubmit\">")
print("<h2>We are composing your song...</h2>")
print("</div>")

print("<div class=\"footer\">")
print("</div>")

print("</body>")

print("</html>")
