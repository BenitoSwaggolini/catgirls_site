from .models import CatGirl, CatGirlStatus
def _age_sort_catgirls(request):
    return CatGirl.objects.all().order_by('-age')

def _virgin_true_filter_catgirls(request):
    return CatGirl.objects.filter(virginity=True)

def _virgin_false_filter_catgirls(request):
    return CatGirl.objects.filter(virginity=False)



