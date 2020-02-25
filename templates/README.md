# Car Dealer Feedback Survey App
#### Submitted by : Sheetal Bongale | Feb 2020
---

Python Flask Feedback app that sends data from the survey to Postgres database and send emails using SMTP. 
The app is then deployed using Heroku.

Technologies used: `Python`, `Flask`, `Flask-SQLAlchemy`, `Postgres` and `Heroku`

The goals for this project are to:
- Create a front end Web app using HTML and CSS.
- Create an the entry & exit point to the application [app.py](app.py)
- Use MailTrap.io Email client to send the feedback to a demo inbox.
- Deploy application using Heroku.

### Instruction to run

```bash
# Add your DATABASE URI in app.py and your mail params in send_mail.py

# Install dependencies
pipenv shell
pipenv install

# Serve on localhost:5000
python app.py
```

Created following tutorial by Brad Traversy