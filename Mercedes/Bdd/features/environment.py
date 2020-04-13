from selenium import webdriver
# import json


# def read_json():
#     with open('data.json', 'r') as file:
#         return json.load(file)


# data = read_json()
# print(data)


def before_all(context):
    context.base_url = "https://mercedesclubqa.azurewebsites.net/#/"
    context.web = webdriver.Firefox()


def after_step(context, step):
    context.user = "28761689017"
    context.password = "Yan@123456"


def after_all(context):
    pass  # context.web.quit()
