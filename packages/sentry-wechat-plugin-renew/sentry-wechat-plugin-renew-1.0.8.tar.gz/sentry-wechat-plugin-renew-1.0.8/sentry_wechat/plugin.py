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


class WechatForm(forms.Form):
    key = forms.CharField(
        max_length=255,
        help_text='WeChat robot key'
    )


WeChat_API = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"

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

        key = self.get_option('key', group.project)
        send_url = WeChat_API.format(key=key)
        title = u'【%s】的项目异常' % event.project.slug

        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": u"#### {title} \n\n > {message} \n\n [详细信息]({url})".format(
                    title=title,
                    message=event.title or event.message,
                    url=u"{}events/{}/".format(group.get_absolute_url(), event.event_id),
                )
            }
        }
        requests.post(
            url=send_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8")
        )