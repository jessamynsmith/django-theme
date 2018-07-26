# django-theme

This is an example of custom static configuration in Django that serves css based on subdomain. I am not certain this is the best solution to this problem, but it is at least a solution that works.

Key details of this solution:

1. Custom storages implementation that overrides the url method, that loads static files from a subdomain folder if it exists: lib/custom_storages.py
2. Custom static templatetag that replaces the django one in order to pass the domain into storages: home/templatetags/custom_static.py
3. Load custom static rather than django static in templates: django_theme/templates/base.html


Like my work? Tip me! https://www.paypal.me/jessamynsmith


### Development

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/django-theme.git

Create a virtualenv using Python 3 and install dependencies. I recommend getting python3 using a package manager (homebrew on OSX), then installing [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation) to that python. NOTE! You must change 'path/to/python3'
to be the actual path to python3 on your system.

    mkvirtualenv eggtimer --python=/path/to/python3
    pipenv install

Optional environment variables, required in production (and localhost, if you want to serve by subdomain):

    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    
You can add the exporting of environment variables to the virtualenv activate script so they are always available.

Set up db:

    python manage.py migrate

Run server:

    python manage.py runserver
    
Or run using gunicorn:

    gunicorn django_theme.wsgi


### Deployment

This project is already set up for deployment to Heroku.

1. Make as many new Heroku apps as you want subdomains, ensuring you have the following addons:

    Heroku Postgres

1. Set up Amazon S3 for static and media as defined in this [Caktus blog post](https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/)

1. Add Heroku config variables for AWS:

    heroku config:set AWS_ACCESS_KEY_ID=<value_from_amazon>
    heroku config:set AWS_SECRET_ACCESS_KEY=<value_from_amazon>

1. In your S3 bucket, create a directory inside the static directory for each subdomain you want to serve. Inside that directory, mirror the path of any file you want to override. Note that this will fully override the default file, so you'll want to make sure that the file you upload for each customer is a clean replacement of a base file you create.


### Future enhancements:

1. Programmatically upload the CSS to S3 using boto.
