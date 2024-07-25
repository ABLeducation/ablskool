import logging
from django.utils import timezone
from datetime import timedelta
from .models import UserActivity1
import re

logger = logging.getLogger(__name__)

class ActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f'Request path: {request.path}')
        response = self.get_response(request)

        if request.user.is_authenticated:
            current_time = timezone.now()
            curriculum_pattern = re.compile(r'^/curriculum/\d+/\w+/.+/$')

            try:
                last_activity_str = request.session.get('last_activity', None)
                last_activity = timezone.datetime.fromisoformat(last_activity_str).replace(tzinfo=current_time.tzinfo) if last_activity_str else None

                logger.info(f'Current request path: {request.path}')
                logger.info(f'Last activity timestamp: {last_activity_str}')

                if request.path == '/user_login/':
                    UserActivity1.objects.create(
                        user=request.user,
                        date=current_time,
                        login_time=current_time
                    )
                    logger.info(f'Login activity recorded for user: {request.user.username} at {current_time}')
                    logger.debug(f'UserActivity1 entry created: {UserActivity1.objects.filter(user=request.user, login_time=current_time).first()}')

                elif request.path == '/user_logout/':
                    logger.info(f'Logout path detected for user: {request.user.username}')
                    try:
                        last_login_activity = UserActivity1.objects.filter(user=request.user, login_time__isnull=False).first()
                        logger.info(f'Login time fetched for user: {request.user.username} is {last_login_activity.login_time}')
                        
                        if last_login_activity:
                            login_time = last_login_activity.login_time
                            logout_time = timezone.now()
                            total_time_spent = logout_time - login_time
                            last_login_activity.logout_time = logout_time
                            last_login_activity.total_time_spent = total_time_spent
                            last_login_activity.save()
                            logger.info(f'Logout time recorded for user: {request.user.username} at {logout_time}, total time spent: {total_time_spent}')
                            logger.info(f'Save operation successful for user: {request.user.username}, last_login_activity: {last_login_activity}')
                        else:
                            logger.warning(f'No login activity found for user: {request.user.username}')
                    except UserActivity1.DoesNotExist:
                        logger.error(f'No login activity found for user: {request.user.username}')
                    except Exception as e:
                        logger.error(f'Error updating logout time for user: {request.user.username}, error: {e}')

                elif curriculum_pattern.match(request.path):
                    time_spent = (current_time - last_activity) if last_activity else timedelta(seconds=0)
                    UserActivity1.objects.create(
                        user=request.user,
                        date=current_time,
                        page_visited=request.path,
                        curriculum_time_spent=time_spent
                    )
                    logger.info(f'Curriculum activity recorded for user: {request.user.username}, page: {request.path}, time_spent: {time_spent}')

                request.session['last_activity'] = current_time.isoformat()
                logger.info(f'Session updated with current time for user: {request.user.username}')

            except Exception as e:
                logger.error(f'Error recording activity for user: {request.user.username}, error: {e}')

        return response
