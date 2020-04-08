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


@when(u'login realizado')  # Representante legal
def step_impl(context):
    pass


@then(u'o perfil esta correto')
def step_impl(context):
    pass
