from django.shortcuts import render

# Create your views here.
def skills(request):
    """  ___ __ ._`.*.'_._ ____ רףאל
        . +  * .\   o.* `.`. +.  א .
       *  .ת' '  \^/|  `. * .  * `
                 \V/ . +
        יהוה     /_\  .`.
       ======== _/W\_ =אדני:By: Two.0:.*"""
    context = {}
    return render(request, 'pages/skills.html', context)
