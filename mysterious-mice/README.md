![Spacebook Logo](spacebook-logo-light.png)

# Spacebook, by Mysterious Mice
The internet has finally made it to Mars, and to celebrate a social media site has been created for NASA's rovers! Take a look around the profiles and photos of these rovers, see what weather is like on Mars, and even play a game where you get to control your very own rover! Don't forget to leave us a note in the guestbook!

## Installation

### With Docker

In the main `mysterious-mice\` directory:
- Run `docker-compose build` to build the Docker image.
- Run `docker-compose up -d` to build, create, start and attach the container. The `d` runs the container in the background.

Open the web app by going to `localhost:8000` in your web browser.

### Without Docker

In the main `mysterious-mice\` directory, create and activate a virtual environment:
- Windows:
  - Run `python -m venv venv` to create the virtual environment.
  - Run `venv\Scripts\Activate` to activate the virtual environment.

- Linux / OS X:
  - Run `python3 -m venv venv` to create the virtual environment.
  - Run `source venv\Scripts\activate` to activate the virtual environment.
- Run `python -m pip install --upgrade pip` to ensure the latest version of pip is installed.
- Run `python -m pip install -r requirements.txt` to install all the required packages.

In the `spacebook\` subdirectory and with the virtual environment active:
- Run `python manage.py makemigrations`
- Run `python manage.py migrate`
- Run `python manage.py loaddata db.json`
- Run `python manage.py runserver`

Open the web app by going to `localhost:8000` in your web browser.

## Updating The Database

If you made changes to the database that you want to commit, run `python manage.py dumpdata > db.json` in the `spacebook\` subdirectory to create a JSON file.

## Admin

To access the admin site, a superuser account will be needed. Run the following command in the `spacebook\` subdirectory to create an account:
`python manage.py createsuperuser`

Then run the server and navigate to `localhost:8000/admin` and log into the newly created account.

## Sources

All photos taken on or of Mars are courtesy of NASA.  
The starry background image is courtesy of [1-background.com](https://1-background.com/stars_1.htm)
