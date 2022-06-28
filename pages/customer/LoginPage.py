#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""@Time : 2021/12/21 17:09
@Author : jianbo
@File : LoginPage.py"""
from time import sleep

from pages.customer.CustomerBasePage import CustomerBasePage


class LoginPage(CustomerBasePage):
    # 登陆页，操作元素
    selectors = {
        "account": "input[placeholder='邮箱/手机']",
        "password": "input[placeholder='密码']",
        "checkbox": "input[type=\"checkbox\"]",
        "login_btn": "form >> text=登录",  # 登录页-登录按钮
        "text1": "text=绑定微信绑定微信，第一时间接收留言与项目进度提醒 >> svg",
    }

    @staticmethod
    def check_element() -> None:
        """页面审查元素"""
        print("页面审查元素成功")
        pass

    # 自然流量客户端登陆流程
    def login(self, account, password):
        self.page.fill(LoginPage.selectors['account'], account)
        self.page.fill(LoginPage.selectors['password'], password)
        self.page.uncheck(LoginPage.selectors['checkbox'])
        self.page.check(LoginPage.selectors['checkbox'])
        self.page.click(LoginPage.selectors['login_btn'])
        # sleep(2)
        self._wait(2)
        """取消提示绑定微信弹窗按钮"""
        # self.page.click(LoginPage.selectors['text1'])
        # self.close_weixintanchuang()
        print("成功登陆了")

    # def close_weixintanchuang(self):
    #     """若页面出现提示绑定微信弹窗，则点击关闭按钮"""
    #     self.page.wait_for_load_state('networkidle')
    #     self.page.wait_for_timeout(5000)
    #     if self.page.query_selector("text=绑定微信绑定微信，第一时间接收留言与项目进度提醒 >> svg"):
    #         self.page.click(LoginPage.selectors['text1'])
