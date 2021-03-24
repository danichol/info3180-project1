"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/property',methods=['GET', 'POST'])
def addproperty():
    form = PropertyForm()

    if request.method == 'POST:
        if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        bedroom=form.bedroom.data
        bathroom = form.bathroom.data
        price = form.price.data
        ptype = form.ptype.data
        location = form.location.data
        img = form.photo.data
        
        img_name = secure_filename(img.filename)
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_name))

        new_property = Property(title, description, bedroom, bathroom, price, ptype, location, img_name)
        db.session.add(new_property)
        db.session.commit()

        flash('New property successfully added.','success')
        return redirect(url_for('properties'))
    return render_template('property.html',form=form)    
,

## View All Properties 
@app.route('/properties')
def properties()"
    return render_template('properties.html')

## Individual Property
@app.route('/property/propertyid')
def propertyid()
    indprop = Property.query.filter_by(propertyid=id).first()
    return render_template('indproperty.html',indprop=indprop)

## Upload Pictures 
@app.route('/uploads/<filename>')
def get_image(filename):
    rootdirectory = os.getcwd()
    return  send_from_directory(os.path.join(rootdirectory,app.config['UPLOAD_FOLDER']),filename)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
