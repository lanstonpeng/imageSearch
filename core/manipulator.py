from flask import render_template

def dealing(result):
    trehold = 0.002
    result.sort(key=lambda tup : tup[1])
    result.reverse()
    print result
    return [name for name,rate in result if rate > trehold]

def renderImage(result):
    hostname = "http://127.0.0.1:8888/static/"
    temp = [{ "url" : hostname + name , "name" : name} for name in result]
    return render_template("result.html",images = temp)
    
