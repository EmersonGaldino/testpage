from behave import given, when, then
import time


@given(u'Abre a pagina de login')
def step_impl(context):
    context.web.get(context.base_url)


@when(u'Realizo o login')
def step_impl(context):
    context.element = context.web.find_element_by_id(
        "userName")  # deste elemento
    context.element.click()
    context.element.send_keys(context.user)
    context.element = context.web.find_element_by_id(
        "userPwd")  # deste elemento
    context.element.click()
    context.element.send_keys(context.password)
    context.element.submit()
    time.sleep(10)


@when(u'login realizado')  # Motorista Autônomo
def step_impl(context):
    context.web.get(context.base_url + "juntosNaEstrada/comofunciona")
    time.sleep(5)


@then(u'o perfil esta correto')
def step_impl(context):
    print(context.web.find_element_by_css_selector(
        ".user-profile > span"))
    # assert context.web.find_element_by_css_selector(
    # ".user-profile > span") == "Motorista Autônomo"

    context.web.get(context.base_url + "promocoes/juntosNaEstrada/promocao")