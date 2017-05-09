#!/home/ubuntu/anaconda2/envs/tf1.1_py2.7/bin/python
import cgitb
import cgi
import os

cgitb.enable()

print(
"Content-type: text/html"
""
"<!DOCTYPE html>"
"<html>"
"<head>"
"<title>TensorWeb Music</title>"

"<meta charset=\"utf-8\"/>"


"<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/jquery.swipebox/1.4.1/css/swipebox.min.css\">"
"<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/normalize/3.0.3/normalize.min.css\"/>"
"<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css\"/>"
"<link rel=\"stylesheet\" href=\"../tensorweb/css/main.css\">"
"<link rel=\"stylesheet\" href=\"../tensorweb/css/gallery.css\">"

"<script src=\"https://code.jquery.com/jquery-1.11.3.min.js\"></script>"
"<script src=\"https://cdnjs.cloudflare.com/ajax/libs/jquery.swipebox/1.4.1/js/jquery.swipebox.min.js\"></script>"
"<script>"
"$('.swipebox').swipebox();"
"</script>"

"</head>"

"<body>"

"<div class=\"header\"> "
"<h1>TensorWeb Music</h1>"
"</div>"

"<div class=\"formsubmit\">"
"<iframe name=\"mp3frame\" src=\"\"></iframe>"
"</div>"

"<div class=\"formsubmit\">"
"<nav><ul>"

"<li><b>Please select the file you wish to play</b></li>"
)

for file in os.listdir("../tensorweb/mp3files"):
    #if file.endswith(".mp3"):
    print ("<li><a href=\"/tensorweb/mp3files/%s\" target=\"mp3frame\">%s</a></li>" % (file, file))

print(
"</ul></nav>"
"</div>"

"<div class=\"footer\">"

"<p>Tensor Music | <a href=\"../tensorweb/index.html\">Create</a> and <a href=\"../tensorweb/play.html\">Play</a></p>"
"</div>"

"</body>"

"</html>"
)