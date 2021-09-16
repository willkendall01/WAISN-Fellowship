# WAISN-Fellowship
Take home test for WAISN Fellowship

I used the `django-admin startproject` to start this project, so some files 
already had a few lines of code. Below the files are listed in (approximate)
order of most to least code added by me.

# Files 
(Assume they are prefixed by WAISN/Database/ unless prefixed otherwise):
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
I left my email details in WAISN/WAISN/settings.py so the site will work
right out of the box. However, if you want to use your own, I left a link 
to the tutorial I used to set it up.

In order to recieve the alert emails when a product reaches 0, you'll have to add your email to the recipients list in the `outOfStockAlert()` function at the bottom of 
views.py. I can also do this if you want me to, but I am on vacation this weekend and may not be able to change the code right away.

# Library Notes
I used django-tables2 to help me format the table of products on the site. I'm not sure
if it will install automatically when you try to run the code, but here is the link to 
the install page:

https://django-tables2.readthedocs.io/en/latest/pages/installation.html


# Resorces
Stuff I used to help me out!
- https://docs.djangoproject.com/en/3.2/intro/tutorial01/
- https://django-tables2.readthedocs.io/en/latest/
- https://css-tricks.com/
- https://stackoverflow.com/questions/5516437/django-form-has-no-errors-but-form-is-valid-doesnt-validate (among other S.O. posts)
- https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab
- https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/
- And other links I dont have open anymore!
