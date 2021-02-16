from mailer import Mailer

mail = Mailer(email='Sender_Email', password='Sender_Password') # This is the person who sends the email!

mail.send(receiver='Receiver_Email',  # This is the person who recieves the email!
          subject='Test Subject', # This is the Subject
          message='Change this message', #This is the Message
          image='sources/icon.png', #This is to upload an image file
		  audio='sources/sound.mp3', #This is to upload an mp3 file
		  file='sources/file.zip') #This is to upload a zip file

"""
(c) Copyright: ArkOfReis
If you are having errors then log into your gmail
and go to myaccount.google.com/lesssecureapps
and enable it and it should work!

When adding files make sure they are in the
same folder as the .py or it will not work.
"""