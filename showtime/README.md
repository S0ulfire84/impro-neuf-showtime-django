# Add new modules

This program needs Python >=3.8 to run. If your version of Python is Python 2.X, use the following:

# Execution

```
alias py=python3
py manage.py runserver
```

# Add pip modules

Add new modules using:

```
py -m pip install <NAME OF THE MODULE>
```

# Migrations

After changing the model, run:

```
py manage.py makemigrations
py manage.py migrate
```

# Deployment to production

1. If there are any pip packages that were newly installed, run:
   `py -m pip freeze > requirements.txt`

2. Commit your changes to the git repo.
3. Update the git in Heroku:
   `git push heroku main`

# Installing on Heroku

The following steps were followed to set this up in Heroku:

1. The requirements file (requirements.txt) was created so the Heroku server can know what pip packages to install.
2. This file tracks the pip packages installed, so if any changes are made to the pip packages, follow the steps above in "Deployment to production".
3. The Procfile is another part of the Heroku installation. So is the White Noise Middleware. You don't need to worry about these for now.
4. You need to use Heroku login to get access to Heroku to do the necessary steps and run commands on the server:
   https://devcenter.heroku.com/articles/heroku-cli

   After installed, run:
   `heroku login`

5. Create the Heroku app, called "impro-neuf-showtime":
   `heroku create impro-neuf-showtime`
6. Set the configuration file to use in Heroku:
   `heroku config:set DJANGO_SETTINGS_MODULE=showtime.settings_production`
7. The ALLOWED_HOSTS in the settings_production.py file has to reflect the actual URL:
   `ALLOWED_HOSTS = ['impro-neuf-showtime.herokuapp.com'] # For Heroku production`
8. The Heroku application needs a database. The cheapest plan is the mini plan:
   `heroku addons:create heroku-postgresql:mini`
9. Migrate the database in Heroku:
   `heroku run python manage.py migrate`
10. A super user needs to be created to interact with the application as a dev:
    `heroku run python manage.py createsuperuser`
11. The uploads require also a separate account for file storage. In this case, an Amazon S3 storage is used. See below for the steps to set this up.

# Setting up image upload

1. Create an Amazon AWS account at https://aws.amazon.com/
2. Create an S3 bucket in Europe named 'impro-neuf-showtime'
3. Set up CORS configuration for your S3 bucket:
   To allow your application to access the media files stored in the S3 bucket, you need to set up a CORS (Cross-Origin Resource Sharing) configuration for the bucket. In the AWS S3 Management Console, follow these steps:

   a. Click on your S3 bucket.
   b. Click on the "Permissions" tab.
   c. Scroll down to the "Cross-origin resource sharing (CORS)" section.
   d. Click the "Edit" button.
   e. Add the following CORS configuration in the JSON editor:

   ```
   [
    {
        "AllowedHeaders": ["*"],
        "AllowedMethods": ["GET"],
        "AllowedOrigins": ["*"],
        "ExposeHeaders": []
    }
   ]
   ```

   f. Click the "Save changes" button.

4. Create a new IAM user that will have access to this bucket:
   Go to https://us-east-1.console.aws.amazon.com/iamv2/home?region=eu-north-1#/home

   You need to create an AWS IAM user with the required permissions to access your S3 bucket. In the AWS IAM Management Console, follow these steps:

   a. Click on "Users" in the left sidebar.
   b. Click the "Add user" button.
   c. Enter a user name, and select "Programmatic access" for the access type.
   d. Click the "Next: Permissions" button.
   e. Click the "Attach existing policies directly" tab.
   f. Click the "Create policy" button.
   g. In the "Create policy" window, switch to the JSON tab.
   h. Add the following policy, replacing <your_bucket_name> with the name of your S3 bucket:

5. Configure the necessary Heroku environment variables to point to the AWS account:
   ```
   heroku config:set AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
   heroku config:set AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key>
   heroku config:set AWS_STORAGE_BUCKET_NAME=<your_bucket_name>
   heroku config:set AWS_S3_REGION_NAME=<your_bucket_region>
   ```

# Creating a Django secret key

The settings_production.py points to an environment variable to get Django to work, called DJANGO_SECRET_KEY.

This has to be configured in Heroku in order for the application to run.

You can generate a key running `py utils/create-random-secret-key.py`

Then update the secret key in Heroku running:
heroku config:set DJANGO_SECRET_KEY='your-secret-key-here'
