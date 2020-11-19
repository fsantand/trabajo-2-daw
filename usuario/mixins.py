class InterpreteRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user,'interprete'):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class SolicitanteRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user,'solicitante'):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
