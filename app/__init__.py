from flask import Flask,render_template,send_file
from datetime import timedelta

app = Flask(__name__,static_folder="static")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=2)

# type
@app.route('/categories/archives')
def typeArchives_mehtod():
    return send_file("static/html/Categories/typeOC.html")

@app.route('/categories/rn')
def typeRN_mehtod():
    return send_file("static/html/Categories/typeRN.html")

@app.route('/categories/oc')
def typeOC_mehtod():
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

@app.route('/categories/swift')
def typeSwift_mehtod():
    return send_file("static/html/Categories/typeSwift.html")

@app.route('/categories/cocoa')
def typeCocoa_mehtod():
    return typeOC_mehtod();




@app.route('/categories/sourcecode')
def typeSourceCode_mehtod():
    return send_file("static/html/Categories/typeSourcecode.html")

@app.route('/categories/something')
def typeSomething_mehtod():
    return send_file("static/html/Categories/typeSomething.html")


@app.route('/base')
def base_mehtod():
    return send_file("static/html/404.html")


#RN
@app.route('/react-native-1')
def react_native_1():
    return send_file("static/html/React-Native/React-Native-1.html")

@app.route('/react-native-2')
def react_native_2():
    return send_file("static/html/React-Native/React-Native-2.html")

#OC
@app.route('/tryCatch')
def tryCatch():
    return send_file("static/html/Objective-C/C-OC_tryCatch.html")

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

#Swift
@app.route('/swift-1')
def swift_1():
    return send_file("static/html/swift/swift-1.html")

@app.route('/swift-2')
def swift_2():
    return send_file("static/html/swift/swift-2.html")

@app.route('/swift-3')
def swift_3():
    return send_file("static/html/swift/swift-3.html")

@app.route('/swift-4')
def swift_4():
    return send_file("static/html/swift/swift-4.html")

@app.route('/swift-5')
def swift_5():
    return send_file("static/html/swift/swift-5.html")

@app.route('/swift-6')
def swift_6():
    return send_file("static/html/swift/swift-6.html")

@app.route('/swift-7')
def swift_7():
    return send_file("static/html/swift/swift-7.html")

@app.route('/swift-8')
def swift_8():
    return send_file("static/html/swift/swift-8.html")

@app.route('/swift-9')
def swift_9():
    return send_file("static/html/swift/swift-9.html")

#docker
@app.route('/docker')
def docker():
    return send_file("static/html/docker/docker.html")

#sdwebimage
@app.route('/sdwebimage-1')
def sdweb_1():
    return send_file("static/html/SDWebImage/sdwebimage-1.html")


@app.route('/')
def navi_mehtod():
    return typeRN_mehtod();


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
#     # return send_file('templates/404.html'),404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


