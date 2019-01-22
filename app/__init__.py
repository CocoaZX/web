from flask import Flask,render_template,send_file
from datetime import timedelta

app = Flask(__name__,static_folder="static")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=2)

# type
@app.route('/categories/oc')
def typeOc_mehtod():
    return send_file("static/html/Categories/typeOC.html")

@app.route('/categories/temp')
def temp_mehtod():
    return send_file("static/html/temp.html")


@app.route('/categories/docker')
def typeDocker_mehtod():
    return send_file("static/html/Categories/typeDocker.html")


@app.route('/categories/github')
def typeGithub_mehtod():
    return send_file("static/html/Categories/typeGithub.html")


@app.route('/base')
def base_mehtod():
    return send_file("static/html/404.html")

@app.route('/')
def navi_mehtod():
    return send_file("static/html/Categories/typeOC.html")




#OC
@app.route('/objective-c-runtime-1')
def oc_runtime_1():
    return send_file("static/html/Objective-C/objective-c-runtime-1.html")

@app.route('/objective-c-runtime-2')
def oc_runtime_2():
    return send_file("static/html/Objective-C/objective-c-runtime-2.html")

@app.route('/objective-c-runtime-3')
def oc_runtime_3():
    return send_file("static/html/Objective-C/objective-c-runtime-3.html")

@app.route('/objective-c-runtime-4')
def oc_runtime_4():
    return send_file("static/html/Objective-C/objective-c-runtime-4.html")

@app.route('/objective-c-runtime-5')
def oc_runtime_5():
    return send_file("static/html/Objective-C/objective-c-runtime-5.html")

@app.route('/objective-c-runtime-6')
def oc_runtime_6():
    return send_file("static/html/Objective-C/objective-c-runtime-6.html")



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    # return send_file('templates/404.html'),404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


