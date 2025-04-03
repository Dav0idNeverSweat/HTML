from flask import Flask, render_template
import os # operates system module

current_folder = os.getcwd() # get current working directory

app = Flask(__name__, static_folder=current_folder + "/src/styles", template_folder=current_folder + "/src/script") # __name__ = constructor

@app.route('/') # default web page
# https://www.google.vn/?hl=vi (?hl=vi: parameter)
def default():
    
    return render_template("/homepage/default.html")

#http://127.0.0.1:5000
# route: http://127.0.0.1:5000/ => run: default => name:homepage

# link, name of page (software-defined rule), function
app.add_url_rule('/', 'homepage', default)

if __name__ == "__main__": # run a process
    # Starting the web server:
    app.run()

# phungsuquangmy@gmail.com