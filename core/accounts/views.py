from django.http import JsonResponse
from models import User
from exeptions import InvalidSuperuserError


def create_superuser(request):
    try:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_superuser(email, password)
        return JsonResponse({
            'status': 'success',
            'message': 'Superuser created successfully',
            'user': {
                'id': user.id,
                'email': user.email,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
                'is_active': user.is_active
            }
        })
    except InvalidSuperuserError:
        return JsonResponse({'status': 'error', 'message': 'Invalid superuser'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
