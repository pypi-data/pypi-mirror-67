"""
sentry_wechat.models
~~~~~~~~~~~~~~~~~~~~~
:copyright: (c) 2020 by cxt, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

import json
import requests
from sentry.plugins.bases.notify import NotificationPlugin
import sentry_wechat
from django import forms
from django.utils.translation import ugettext_lazy as _


class WechatForm(forms.Form):
   urls = forms.CharField(
        label=_('Wechat robot url'),
        widget=forms.Textarea(attrs={
            'class': 'span6', 'placeholder': 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx-xxx-xxx-xxx-xxx'}),
        help_text=_('Enter wechat robot url.'))

class WechatPlugin(NotificationPlugin):
    """
    Sentry plugin to send error counts to WeChat.
    """
    author = 'cxt'
    author_url = 'https://github.com/susujs/sentry-wechat-plugin'
    version = sentry_wechat.VERSION
    description = "Integrates wechat robot."
    resource_links = [
        ('Bug Tracker', 'https://github.com/susujs/sentry-wechat-plugin/issues'),
        ('Source', 'https://github.com/susujs/sentry-wechat-plugin'),
    ]

    slug = 'wechat'
    title = 'wechat'
    conf_title = title
    conf_key = 'wechat'
    project_conf_form = WechatForm

    def get_webhook_urls(self, project):
        url = self.get_option('urls', project)
        if not url:
            return ''
        return url
        
    def is_configured(self, project):
        """
        Check if plugin is configured.
        """
        return bool(self.get_option('key', project))

    def notify_users(self, group, event, *args, **kwargs):
        self.post_process(group, event, *args, **kwargs)

    def post_process(self, group, event, *args, **kwargs):
        """
        Process error.
        """
        if not self.is_configured(group.project):
            return

        if group.is_ignored():
            return

        send_url = self.get_webhook_urls(group.project)
        title = "【{}】发生错误，请尽快查看处理!".format(event.project.slug)
        url="{}events/{}/".format(group.get_absolute_url(),event.event_id)

        data = {
          "msgtype": "news",
    "news": {
       "articles" : [
           {
               "title" : title,
               "description" : event.title or event.message,
               "url" : url,
               "picurl" : "http://pic1.zhimg.com/v2-c41cd2b3b6c58245908ad89f7ddc55e7_b.jpg"
           }
        ]
    }
        }
        requests.post(
            url=send_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )
#       data = {
#             "msgtype": "markdown",
#             "markdown": {
#                 "content": '''
#                 ## 错误报警   \n
#                 ### 项目{project_name}发生错误，请尽快查看处理!   \n   ![screenshot](http://pic1.zhimg.com/v2-c41cd2b3b6c58245908ad89f7ddc55e7_b.jpg)
# > [点我直接查看BUG]({link})
#                 '''.format(
#                     project_name=project,
#                     link=link,
#                 ),
#             },
#             }
