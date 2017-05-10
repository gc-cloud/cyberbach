#!/home/ubuntu/anaconda2/envs/tf1.1_py2.7/bin/python
import cgitb
import cgi
import os

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
print("<p>Your Song is Ready!</p>")
print("</div>")

print("<div class=\"formsubmit\">")
#print("<iframe name=\"mp3frame\" src=\"\"></iframe>")
print("<iframe name=\"mp3frame\" src=\"/tensorweb/mp3files/newsong.wav\">Play Your Song</iframe>")
print("</div>")

#print("<div class=\"formsubmit\">")
#print("<nav><ul>")

#print ("<li><b> Finished composing... Click to play</b></li>")

#for file in os.listdir("../tensorweb/mp3files"):
    #if file.endswith(".mp3"):
    #print ("<li><a href=\"/tensorweb/mp3files/%s\" target=\"mp3frame\">%s</a></li>" % (file, file))
#    print ("<li><a href=\"/tensorweb/mp3files/%s\" target=\"mp3frame\">%s</a></li>" % (file, "Play Your Song!"))

#print("</ul></nav>")
#print("</div>")

print("<div class=\"footer\">")
#print(
#"<p>Tensor Music | <a href=\"../tensorweb/index.html\">Create New Song</a> and <a href=\"../tensorweb/play.html\">Play</a></p>")
print(
"<p>Tensor Music | <a href=\"../tensorweb/index.html\">Create New Song</a> </p>")
print("</div>")

print("</body>")

print("</html>")