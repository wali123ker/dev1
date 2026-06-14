import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login/')
def chatbot_view(request):
    response_text = None
    prompt = None
    error = None

    if request.method == 'POST':
        prompt = request.POST.get('prompt', '').strip()
        if prompt:
            try:
                from google import genai
                client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                response_text = response.text
            except Exception as e:
                error = f"Error al conectar con la API: {str(e)}"

    return render(request, 'chatbot/chatbot.html', {
        'response_text': response_text,
        'prompt': prompt,
        'error': error,
    })