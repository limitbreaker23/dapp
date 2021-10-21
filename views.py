
from flask import Blueprint, render_template
views  = Blueprint('views', __name__)
from .data import data

posts = None 
@views.route('/')
def home():
    return render_template("base.html", data=data)



@views.route('anime/<name>', methods=['GET'])
def episode(name):
    print(name)
    name = str(name)
    num = next((index for (index, d) in enumerate(data) if d["title"] == name), None)
    num = int(num)
    eptotal = (data[num]['eptotal'])
    syp = (data[num]['synopsis'])
    img = (data[num]['img'])
    title = (data[num]['title'])
    
    #x = data.index(filter(lambda n:n.get('title') == name, data))
    #print(x)
   

    #[i for i, d in enumerate(data) if name in print(d.values())]


    
    
    return render_template("episode.html", data = data[num], eptotal = int(eptotal), syp = syp, img = img, title = title)



@views.route('anime/<name>/episode<int:i>', methods=['GET'])
def player(name, i):
    print(name)
    print(i)
    name = str(name)
    num = next((index for (index, d) in enumerate(data) if d["title"] == name), None)
    num = int(num)
    eptotal = (data[num]['eptotal'])
    title = (data[num]['title'])
    eptotal= int(eptotal)
    eptotal = eptotal+1
    i = i-1
    i = str(i)
    link = data[num][i]
    print(link)
    return render_template("watch.html", data = data[num], eptotal = eptotal,title = title, link = link)