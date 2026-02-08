from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    
    def ready(self):
        import accounts.signals  # Import signals to ensure they are registered when the app is ready
