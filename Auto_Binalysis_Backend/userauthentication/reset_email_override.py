from djoser.email import PasswordResetEmail


class CustomPasswordResetEmail(PasswordResetEmail):
    def get_context_data(self):
        context = super().get_context_data()
        context['domain'] = 'localhost:3000'
        context['protocol'] = 'http'

        return context
