from behave import given, when, then
import time


@given(u'Esteja na aba promocao')
def step_impl(context):
    context.web.get(context.base_url + "promocoes/juntosNaEstrada/promocao")
    time.sleep(4)


@when(u'Tenha o botao acione aqui')
def step_impl(context):
    assert context.web.find_element_by_css_selector(
        "btn-premio-instantaneo")
    time.sleep(4)



@when(u'Clico no acione aqui')
def step_impl(context):
    context.web.find_element_by_css_selector(
        "btn-premio-instantaneo")
    context.element.click()
    time.sleep(4)



@when(u'E ganho premio')
def step_impl(context):
    pass  # estradaPremioPremiado == 'nOK's


@when(u'clico no X para sair')
def step_impl(context):
    pass  # raise NotImplementedError(u'STEP: When clico no X para sair')


@then(u'Acionei a placa premiada')
def step_impl(context):
    pass  # raise NotImplementedError(u'STEP: Then Acionei a placa premiada')
