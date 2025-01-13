from django.apps import AppConfig


class PollsConfig(AppConfig):
    '''
    Configuration class for the 'polls' app.

    This class is used to configure settings for the application,
    such as the default primary key field type and the app name.
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
 
