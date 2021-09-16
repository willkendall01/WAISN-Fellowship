# WAISN-Fellowship
Take home coding assesment for WAISN Fellowship

I used the `django-admin startproject` to start this project, so some files 
already had a few lines of code. Below the files are listed in (approximate)
order of most to least code added by me.

# Set up

### In a terminal window
1. Clone this project into the directory you wish to ue
2. Start a virtual environment
3. Install required packages with `pip install -r requirements.txt`
4. CD into WAISN-Fellowship/WAISN and run `python manage.py migrate` you should see a list of all the applied migrations in your terminal output
5. Remaining in WAISN-Fellowship/WAISN, run `python manage.py runserver` to start the server
   - This might throw an error asking you to add the i.p. to the `ALLOWED_HOSTS` list in settings.py 
   - (I haven't had the opportunity to test this on a different computer, so I'm not sure)
   - Fix this error by copying the i.p. into the 'ALLOWED_HOSTS' list on line 38 of WAISN-Fellowship/WAISN/WAISN/settings.py  

# Files 
(Assume they are prefixed by WAISN/Database/ unless prefixed WAISN/WAISN/):
   1. views.py
   2. Static/CSS/index.CSS
   3. Templates/Database/index.html
   4. forms.py
   5. models.py
   6. admin.py
   7. tables.py
   8. WAISN/WAISN/urls.py
   9. urls.py
   10. WAISN/WAISN/settings.py (Just the email config settings)

I did not write code in any of the remaining files.

# Email Config
I left my email details as the email config data at the top of WAISN/WAISN/settings.py so the site will work
right out of the box. However, if you want to use your own, I left a link 
to the tutorial I used to set it up. If you follow this tutorial, you will also have to change the `host_email` parameter to `send_mail()` function in the `outOfStockAlert()` function which is the last function at the bottom of 
views.py (line 148).
- https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab


In order to recieve the alert emails when a product reaches a quantity of 0, you'll have to add your email to the `recipient_list` in the `outOfStockAlert()` function which is the last function at the bottom of 
views.py (line 149).

# Admin Config
After running a clean install of a git clone on my copmuter, it seems my admin account was erased. I made a minor change to the admin page to better display the product data to the admin. It's fairly minor, but if you wish to examine it, you may have to make a superuser for the db.

This link explaines the process very clearly: https://docs.djangoproject.com/en/1.8/intro/tutorial02/

# Library Notes
I used django-tables2 to help me format the table of products on the site. I'm not sure
if it will install automatically when you try to run the code, so, in case it doesn't work, here is the link to 
the install page:

https://django-tables2.readthedocs.io/en/latest/pages/installation.html

(It worked outside of my virtual env when I ran with a clean git clone in a new location on my computer. However, it did not prompt me to install the package, so it may be global on my computer.)

# Known Bugs
- After clicking table headers to re-order products, if the table is altered, the order will revert to defualt.
- The width and height of the site are actually larger than the view size of the browser.
- Alerts will sometimes pop-up upon page refresh (clearing cache in browser fixes this).
- Responsiveness is far from perfect, but the site still looks good on a 1920x1080 monitor (full or half width). 

# Resorces
Stuff I used to help me out!
- https://docs.djangoproject.com/en/3.2/intro/tutorial01/
- https://django-tables2.readthedocs.io/en/latest/
- https://css-tricks.com/
- https://stackoverflow.com/questions/5516437/django-form-has-no-errors-but-form-is-valid-doesnt-validate (among other S.O. posts)
- https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab
- https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/
- And other links I dont have open anymore!
