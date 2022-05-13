import smtplib
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main():
    welcome()
    global connect 
    
    try:
        
        connect=smtplib.SMTP('smtp.gmail.com',587)
        connect.ehlo()
        connect.starttls()    
         
        sender_email=input("Enter your gmail Id : ")
        #don’t want your password to show on your screen when you type it, use getpass.getpass()
        sender_passwd=getpass.getpass("Enter your specific app password :")
        a=login_func(sender_email,sender_passwd)
        print(a)
        print()
        #send_from=input("Enter Gmail Id sending from : ")
        receiver_email=input("Enter Gmail Id you want to send : ")
        subject=input("Enter your mail subject : ")
        msg_text=input("Enter your mail message : ")
        print("Message length is", len(msg_text))


        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails
        print()
        # Add body to email
        message.attach(MIMEText(msg_text, "plain"))
        #files_number=int(input("Enter the number of file you want send: "))

        print("""Enter filename of pdf file.\nFor example:\n>>>Filname:note.pdf\n>>>Filename:kewang_cv.pdf\n>>>Filename:document.pdf\n""" )
        #pdf need to be in same directory with python file
    
        filename=input("Filname:")
        # filename=filename+'.pdf'
        print()
        
       
        
        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
                
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)


        # Add header as key/value pair to attachment part
        part.add_header("Content-Disposition", f"attachment; filename= {filename}",)

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()


        # b=sendmail_func(sender_email,receiver_email,msg="Subject:{}\n{}.".format(subject,msg_text))
        b=sendmail_func(sender_email,receiver_email,text)
        print("Successfully email📧 sent")

    except Exception as e:
    # Print any error messages to stdout
        print(e)
    ##The finally block gets executed no matter if the try block raises any errors or not:
    finally:
        connect.quit()
        
 

def welcome():
    print("----------------------------------------------------\n")
    print()
    print("                    Send mail📧                       ")
    print()
    print("-------------------------------------------------------")
    print()


 
def login_func(sender_email,sender_passwd):
    login_done= connect.login(sender_email,sender_passwd)
    return login_done


def sendmail_func(send_email,receiver_email,text):
    mail=connect.sendmail(send_email,receiver_email,text)
    return mail

if __name__ == '__main__':
        main()