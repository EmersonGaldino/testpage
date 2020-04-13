from behave import given, when, then
import time


@given(u'Estou logado posso navegar')
def step_impl(context):
    context.web.get(context.base_url)


@given(u'validar todos os links')
def step_impl(context):
    context.web.get(context.base_url + "juntosNaEstrada/comofunciona")
    time.sleep(4)
    context.web.get(context.base_url + "juntosNaEstrada/premiacao")
    time.sleep(4)
    context.web.get(context.base_url + "promocoes/juntosNaEstrada/promocao")
    time.sleep(4)
    context.web.get(context.base_url + "juntosNaEstrada/regulamento")
    time.sleep(4)
    context.web.get(context.base_url + "juntosNaEstrada/ajudaSuporte")
    time.sleep(4)


@then(u'Proximo step')
def step_impl(context):
    pass
