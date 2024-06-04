# views.py

from django.shortcuts import render, get_object_or_404
from .models import SecretMessage
from .forms import SecretMessageForm

def create_secret_message(request):
    """
    View to create a new secret message.
    """
    if request.method == 'POST':
        form = SecretMessageForm(request.POST)
        if form.is_valid():
            secret_message = form.save()
            # Redirect to the secret message's detail view
            return redirect('secret_message_detail', pk=secret_message.id)
    else:
        form = SecretMessageForm()
    return render(request, 'create_secret_message.html', {'form': form})

def secret_message_detail(request, pk):
    """
    View to retrieve a secret message using its unique identifier.
    """
    secret_message = get_object_or_404(SecretMessage, pk=pk)
    return render(request, 'secret_message_detail.html', {'secret_message': secret_message})
