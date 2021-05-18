from django.shortcuts import render

# Create your views here.

# Dynamic lorem texts.
text1 = "Strona w budowie..."
text2 = "Tu jeszcze nic nie ma..."


def sg(request):
    c = {'title': 'Strona główna', 'h1': 'Strona główna', 'text': text1}
    return render(
        request=request,
        template_name="infos/sg.html",
        context=c
    )


def me(request):
    c = {'title': 'O mnie', 'h1': 'O mnie', 'text': text2}
    return render(
        request=request,
        template_name="infos/me.html",
        context=c
    )


def contact(request):
    c = {'title': 'Kontakt', 'h1': 'Kontakt'}
    return render(
        request=request,
        template_name="infos/contact.html",
        context=c
    )

