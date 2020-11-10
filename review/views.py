from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Review
from atencion.models import Atencion

from .forms import ReviewForm

# Create your views here.
class ReviewView(View):
    def get(self, request, atencion, *args, **kwargs):
        ctx = {}
        atencion = get_object_or_404(Atencion, pk = atencion)
        if atencion.esta_finalizada():
            usuario_review = -1
            template = ''
            # Conseguir el tipo de usuario
            if hasattr(request.user,"solicitante"):
                usuario_review = atencion.inteprete
                usuario_actual = atencion.solicitante
                template = 'review/solicitante_create.html'
            else:
                usuario_review = atencion.solicitante
                usuario_actual = atencion.interprete
                template = 'review/interprete_create.html'
            # Valida que el usuario este habilitado para hacer la reseña
            if usuario_actual != request.user:
                return redirect('dash')
            # Verificar si no existe la reseña ya
            if atencion.reviews.filter(usuario = request.user):
                return redirect('dash')
            ctx['atencion'] = atencion
            ctx['usuario'] = usuario_review
            ctx['form'] = ReviewForm({'usuario_pk':usuario_review.usuario.pk})
            return render(request, template, ctx)
        return redirect('dash')

    def post(self, request, atencion, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            atencion = get_object_or_404(Atencion, pk = atencion)
            new_review = Review.objects.create(
                atencion=atencion,
                usuario=form.cleaned_data['usuario_pk'],
                review=form.cleaned_data['review'],
                calificacion=form.cleaned_data['calificacion']
            )
        return redirect('dash')
