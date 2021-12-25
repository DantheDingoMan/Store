"""Flask app"""
import os
from flask import render_template, request, redirect
from werkzeug.utils import send_from_directory
from config import app, db
from model import items, itemsSchema
from werkzeug.utils import secure_filename


@app.route("/")
def client():
    itemlist = items.query.all()
    item_schema = itemsSchema(many=True)
    return render_template("clientpage.html", itemlist = item_schema.dump(itemlist))

@app.route("/admin")
def admin():
    itemlist = items.query.all()
    item_schema = itemsSchema(many=True)
    return render_template("adminpage.html", itemlist = item_schema.dump(itemlist))

@app.route("/admin/edit", methods=["GET", "POST"])
def adminedit():

    delete = request.form.get("delete")
    itemname = request.form.get("itemname")
    print(itemname)
    if delete == "yes":
        items.query.filter(items.itemname==itemname).delete()
        db.session.commit()
        itemlist = items.query.all()
        item_schema = itemsSchema(many=True)
        return render_template("adminpage.html", itemlist = item_schema.dump(itemlist))
    else:
        price = request.form.get("price")
        
        description = request.form.get("description")

        items.query.filter(items.itemname==itemname).update({items.price: price})
        items.query.filter(items.itemname==itemname).update({items.description: description})
        db.session.commit()
        itemlist = items.query.all()
        item_schema = itemsSchema(many=True)
        return render_template("adminpage.html", itemlist = item_schema.dump(itemlist))
        

UPLOAD_FOLDER = 'static/uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024




ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


	

#return redirect(url_for('static', filename='uploads/' + filename), code=301)




@app.route("/admin/add", methods=["GET", "POST"])
def adminadd():
    try:
        
        itemname=request.form.get("itemname")

            
        if 'file' not in request.files:
           
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
        
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print(file)
            filename = secure_filename(file.filename)
            
            filename = itemname + ".jpg"
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        else:
     
            return redirect(request.url)
        
        
        
        new_item = items(
                itemname=request.form.get("itemname"),
                price=request.form.get("price"),
                description=request.form.get("description")
            )
        
        db.session.add(new_item)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        itemlist = items.query.all()
        item_schema = itemsSchema(many=True)
        return render_template("adminpage.html", itemlist = item_schema.dump(itemlist))
    except:
        itemlist = items.query.all()
        item_schema = itemsSchema(many=True)
        return render_template("adminpage.html", itemlist = item_schema.dump(itemlist))


   