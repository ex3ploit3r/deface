from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('input', '')
        # Vulnerable endpoint using render_template_string with enhanced HTML
        return render_template_string(f"""
            <!DOCTYPE html>
           
<html>
<head>
	<title>Hacked by 0xsha4</title>
	<style>
	    iframe {
		    display:none;
	    }
	</style>
</head>

<body background="https://i.imgur.com/5rZ91h5.gif">
	<iframe width="200" height="113" src="https://www.youtube.com/embed/hZsaPu-kthY?playlist=hZsaPu-kthY&amp;autoplay=1&amp;loop=1&amp;rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
	<center>
		<h1 style=color:red;>(? ?? ? ??)? D0 Y0U W4NN4 PL4Y A G4M3 ? (?? ? ??? )</h1>
		<h2 style=color:green;>This website is H4CK3D by 0xsha4.</h2>
		<img src="https://i.imgur.com/OhoiDOT.png">
		<h3 style=color:grey; >*****HASH XXX******</h3>
		<p style=color:grey; >Greetz to --> ezirprus, revaer luos, yzeets, yajyaj, ximer, erifdliw, selym, yeda, zalbzaw, ongap, ymon</p>
	</center>
</body>
</html>


        """)
    # Initial form when no input has been submitted
    return '''
        <form method="POST">
            <input name="input" type="text" placeholder="Enter text"/>
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
