#!/home/sford/anaconda2/envs/tf1.1_py2.7/bin/python
import cgitb
import cgi
import subprocess

cgitb.enable()    

print("Content-type: text/html")
print("")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<title>TensorWeb Music</title>")
    
print("<meta charset=\"utf-8\"/>")
    
print("<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/jquery.swipebox/1.4.1/css/swipebox.min.css\">")
print("<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/normalize/3.0.3/normalize.min.css\"/>")
print("<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css\"/>")
print("<link rel=\"stylesheet\" href=\"../tensorweb/css/main.css\">")
print("<link rel=\"stylesheet\" href=\"../tensorweb/css/gallery.css\">")
        
print("<script src=\"https://code.jquery.com/jquery-1.11.3.min.js\"></script>")
print("<script src=\"https://cdnjs.cloudflare.com/ajax/libs/jquery.swipebox/1.4.1/js/jquery.swipebox.min.js\"></script>")
print("<script>")
print("$('.swipebox').swipebox();")
print("</script>")

print("</head>")
    
print("<body>")
    
print("<div class=\"header\"> ")
print("<h1>TensorWeb Music</h1>")
print("</div>")
    
print("<div class=\"formsubmit\">")
print("<h3>Generating the music file ...</h3>")
print("</div>")

print("<pre>")

#subprocess.call("../rnn_rbm_generate.py","../parameter_checkpoints/pretrained.ckpt")
subprocess.call("/home/sford/anaconda2/envs/tf1.1_py2.7/bin/python ../rnn_rbm_generate.py ../parameter_checkpoints/pretrained.ckpt", shell=True)


print("</pre>")

print("<div class=\"formsubmit\">")
print("<h3>Process completed </h3>")
print("</div>")

print("<div class=\"footer\">")
print("<p>Tensor Music | Create and <a href=\"../tensorweb/play.html\">Play</a></p>")
print("</div>")
    
print("</body>")

print("</html>")


