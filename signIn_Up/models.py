from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    #email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)    # print(reset_password_token)
    # print("ddd")
    # print(reset_password_token.key)
    # email_plaintext_message = "response-reset-password/{}".format(reverse('reset-password-request'), reset_password_token.key)
    email_plaintext_message = "http://localhost:4200/response-reset-password/response/"+reset_password_token.user.email+"/"+reset_password_token.key

    send_mail(
        # title:
        "Password Reset for {title}".format(title=reset_password_token.user.email),
        # message:
        email_plaintext_message,
        # from:
        "stage@ensam-casa.ma",
        # to:
        [reset_password_token.user.email]
    )