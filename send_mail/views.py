from django.core.mail import send_mail
from django.http import JsonResponse

def sending_mail(request):
    subject = "Test Email"
    message = "This is a test email sent using SMTP in Django."
    from_email = "example@gmail.com"
    recipient_list = ["example@gmail.com"]  # Corrected email address

    send_mail(subject, message, from_email, recipient_list)

    return JsonResponse({'success': True})
