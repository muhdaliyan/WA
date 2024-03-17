from django.shortcuts import render, redirect, HttpResponseRedirect

def sender(request):
    if request.method == "POST":
        data = request.POST

        ph = data.get('ph')
        msg = data.get('msg')
        phone_number = ph
        message = msg

        return open_whatsapp_chat(phone_number, message)

    pre_msg = "AOA! \nWe noticed [QubeSuit] doesn't have a website. Let's fix that! A professional website can attract more customers and boost credibility. \nCan we chat about how we can help this week? \nCheers, \nQubeknit "

    return render(request, 'index.html', {'prefilled_message': pre_msg})


def open_whatsapp_chat(phone_number, message):
    phone_number = phone_number.strip("+-0")
    phone_number = phone_number.replace(" ", "")
    encoded_message = message.replace(" ", "%20")

    if not phone_number.isdigit():
        print("Invalid phone number. Please enter a valid number with digits only.")
        return

    url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
    return HttpResponseRedirect(url)