from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect

def sender(request):
    if request.method == "POST":
        data = request.POST
        btn = data.get('platform')
        ph = data.get('ph')
        client = data.get('client')


        if btn == 'shopify':
            message = f"AOA! We noticed *{client}* doesn't have a Online Store. Let's fix that! A professional E-Commerce Store can attract more customers and boost credibility. Can we chat about how we can help this week?\nCheers,\n*Qubeknit* 🚀"
        else:
            message = f"AOA! We noticed *{client}* doesn't have a website. Let's fix that! A professional website can attract more customers and boost credibility. Can we chat about how we can help this week?\nCheers,\n*Qubeknit* 🚀"

        return open_whatsapp_chat(ph, message)

    return render(request, 'index.html',)


def open_whatsapp_chat(phone_number, message):
    phone_number = phone_number.strip("+-0")
    phone_number = phone_number.replace(" ", "")
    encoded_message = message.replace(" ", "%20")

    if not phone_number.isdigit():
        print("Invalid phone number. Please enter a valid number with digits only.")
        return  HttpResponseRedirect('/')

    url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
    return HttpResponseRedirect(url)