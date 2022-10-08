
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Pedido, Oferta, Projeto, Vendas, Like
from django.utils import timezone
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login as loginid, logout


def index(request):
    return render(request,'musica/index.html')

def inicio(request):
    if request.user.is_authenticated:
        return render(request, 'musica/inicio.html')
    else:
        return render(request,'musica/index.html')

def social(request):
    latest_post_list = Post.objects.order_by('-pub_data')[:100]
    context = {
                'latest_post_list': latest_post_list,
            }
    return render(request, 'musica/social.html',context)

def detalhe(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'musica/detalhe.html',{'post': post})

def like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = get_object_or_404(User, pk=request.user.id)
    like = Like(user = user, post = post)
    objetos = Like.objects.all()
    if not objetos.exists():
        post.incgosto()
        post.save()
        like.save()
        return render(request, 'musica/detalhe.html', {'post': post})
    else:
        for i in objetos:
            if(i.post_id == post_id and i.user_id == user.id):
                return render(request, 'musica/detalhe.html', {'post': post})
        post.incgosto()
        post.save()
        like.save()
        return render(request, 'musica/detalhe.html', {'post': post})
    return render(request, 'musica/detalhe.html', {'post': post})

def novopost(request):
    return render(request, 'musica/novopost.html')

def adicionarpost(request, user_id):
    id_user = get_object_or_404(User, pk=user_id)
    posttxt = request.POST['novoPost']
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES.get('myfile')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        i = "media/"+str(myfile.name)
        q = Post(user= id_user, post_texto=posttxt, pub_data=timezone.now(), imagem = i)
        q.save()
        return render(request, 'musica/post.html', {'uploaded_file_url': uploaded_file_url})
    else:
        q = Post(user= id_user, post_texto=posttxt, pub_data=timezone.now(), imagem = None)
        q.save()
        return render(request,'musica/post.html')

def current_user(request):
    current_user = request.user.id
    return current_user

def apagarpost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if(current_user(request)==post.user_id):
        post.delete()
    return HttpResponseRedirect(reverse('musica:social'))

def novocomentario(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'musica/novocomentario.html', {'post': post})

def adicionarcomentario(request, post_id):
    post = Post.objects.get(pk=post_id)
    comentariotxt = request.POST['novoComentario']
    post.comentario_set.create(user = request.user, comentario_texto=comentariotxt, pub_data=timezone.now())
    return render(request, 'musica/detalhe.html', {'post': post})

def centro_ajuda(request):
    return render(request, 'musica/centroajuda.html',)

def procura(request):
    latest_pedido_list = Pedido.objects.order_by('-pub_data')[:100]
    context = {
                'latest_pedido_list': latest_pedido_list,
            }
    return render(request, 'musica/procura.html',context)

def detalhe_ajuda(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'musica/detalhe_ajuda.html', {'pedido': pedido})

def novopedido(request):
    return render(request, 'musica/novopedido.html')

def publicar_procura(request, user_id):
    id_user = get_object_or_404(User, pk=user_id)
    titulo = request.POST['titulo']
    txt = request.POST['texto']
    contacto = request.POST['contacto']
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES.get('myfile')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        i = "media/"+str(myfile.name)
        q = Pedido(user= id_user, pedido_titulo = titulo, pedido_texto = txt, pedido_contacto = contacto, imagem = i, pub_data = timezone.now())
        q.save()
        return render(request, 'musica/procurapublicada.html', {'uploaded_file_url': uploaded_file_url})
    else:
        q = Pedido(user= id_user, pedido_titulo = titulo, pedido_texto = txt, pedido_contacto = contacto, imagem = None, pub_data = timezone.now())
        q.save()
        return render(request,'musica/procurapublicada.html')

def apagarajuda(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if(current_user(request)==pedido.user_id):
        pedido.delete()
    return HttpResponseRedirect(reverse('musica:procura'))

def oferta(request):
    latest_oferta_list = Oferta.objects.order_by('-pub_data')[:100]
    context = {
                'latest_oferta_list': latest_oferta_list,
            }
    return render(request, 'musica/oferta.html',context)

def novaoferta(request):
    return render(request, 'musica/novaoferta.html')

def publicar_oferta(request, user_id):
    id_user = get_object_or_404(User, pk=user_id)
    titulo = request.POST['titulo']
    txt = request.POST['texto']
    contacto = request.POST['contacto']
    q = Oferta(user = id_user, oferta_titulo = titulo, oferta_texto = txt, oferta_contacto = contacto, pub_data = timezone.now())
    q.save()
    return render(request, 'musica/ofertapublicada.html')

def detalhe_oferta(request, oferta_id):
    oferta = get_object_or_404(Oferta, pk=oferta_id)
    return render(request, 'musica/detalhe_oferta.html', {'oferta': oferta})

def apagaroferta(request, oferta_id):
    oferta = get_object_or_404(Oferta, pk=oferta_id)
    if(current_user(request)==oferta.user_id):
        oferta.delete()
    return HttpResponseRedirect(reverse('musica:oferta'))

def projetos(request):
    latest_projetos_list = Projeto.objects.order_by('-pub_data')[:100]
    context = {
                'latest_projetos_list': latest_projetos_list,
            }
    return render(request, 'musica/projetos.html',context)

def novoproj(request):
    return render(request, 'musica/novoproj.html')

def publicar_proj(request, user_id):
    id_user = get_object_or_404(User, pk=user_id)
    titulo = request.POST['titulo']
    txt = request.POST['texto']
    contacto = request.POST['contacto']
    instrumento = request.POST['instrumento']
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES.get('myfile')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        i = "media/"+str(myfile.name)
        q = Projeto(user = id_user, projeto_titulo = titulo, projeto_texto = txt, projeto_contacto = contacto, projeto_instrumento = instrumento, imagem = i, pub_data = timezone.now())
        q.save()
        return render(request, 'musica/projetopublicado.html', {'uploaded_file_url': uploaded_file_url})
    else:
        q = Projeto(user = id_user, projeto_titulo = titulo, projeto_texto = txt, projeto_contacto = contacto, projeto_instrumento = instrumento, imagem = None, pub_data = timezone.now())
        q.save()
        return render(request,'musica/projetopublicado.html')

def detalhe_projeto(request, proj_id):
    projeto = get_object_or_404(Projeto, pk=proj_id)
    return render(request, 'musica/detalhe_projeto.html', {'projetos': projeto})

def apagarprojeto(request, proj_id):
    projeto = get_object_or_404(Projeto, pk=proj_id)
    if(current_user(request)==projeto.user_id):
        projeto.delete()
    return HttpResponseRedirect(reverse('musica:projetos'))

def venda(request):
    latest_venda_list = Vendas.objects.order_by('-pub_data')[:100]
    context = {
                'latest_venda_list': latest_venda_list,
            }
    return render(request, 'musica/venda.html',context)

def novavenda(request):
    return render(request, 'musica/novavenda.html')

def publicar_venda(request, user_id):
    id_user = get_object_or_404(User, pk=user_id)
    titulo = request.POST['titulo']
    txt = request.POST['texto']
    contacto = request.POST['contacto']
    preco = request.POST['preco']
    negociavel = request.POST.get('negociavel', False)
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES.get('myfile')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        i = "media/"+str(myfile.name)
        q = Vendas(user = id_user, venda_titulo = titulo, venda_texto = txt, venda_contacto = contacto, venda_preco = preco, venda_negociavel = negociavel, imagem = i, pub_data = timezone.now())
        q.save()
        return render(request, 'musica/anunciopublicado.html', {'uploaded_file_url': uploaded_file_url})
    else:
        q = Vendas(user = id_user, venda_titulo = titulo, venda_texto = txt, venda_contacto = contacto, venda_preco = preco, venda_negociavel = negociavel, imagem = None, pub_data = timezone.now())
        q.save()
        return render(request,'musica/anunciopublicado.html')


def detalhe_venda(request, venda_id):
    venda = get_object_or_404(Vendas, pk = venda_id)
    return render(request, 'musica/detalhe_venda.html', {'venda': venda})

def apagarvenda(request, venda_id):
    venda = get_object_or_404(Vendas, pk=venda_id)
    if(current_user(request)==venda.user_id):
        venda.delete()
    return HttpResponseRedirect(reverse('musica:venda'))

def aboutUs(request):
    return render(request, 'musica/aboutUs.html')

def entrar(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        loginid(request, user)
        return render(request, 'musica/inicio.html')
    else:
        x = True
        return render(request, 'musica/index.html', {'x': x})

def registration(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    objetos = User.objects.all()
    for i in objetos:
        if (i.username == username or i.email== email):
            x = True
            return render(request, 'musica/registration.html', {'x': x})
    User.objects.create_user(username, email, password)
    return render(request, 'musica/index.html')

def registar(request):
    return render(request, 'musica/registration.html')

def logoutview(request):
    logout(request)
    return render(request, 'musica/index.html')
