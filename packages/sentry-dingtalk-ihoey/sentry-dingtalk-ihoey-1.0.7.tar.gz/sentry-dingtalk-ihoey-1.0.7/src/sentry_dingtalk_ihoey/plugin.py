# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sentry_dingtalk_ihoey
from .forms import DingTalkOptionsForm
from sentry.plugins.bases.notify import NotificationPlugin

DING_TALK_API = 'https://oapi.dingtalk.com/robot/send?access_token={token}'


class DingTalkPlugin(NotificationPlugin):
    author = 'ihoey'
    author_url = 'https://github.com/ihoey/sentry_dingtalk_ihoey'
    description = 'sentry extension which can send error to dingtalk'
    resource_links = [
        ('Source', 'https://github.com/ihoey/sentry_dingtalk_ihoey'),
        ('Bug Tracker', 'https://github.com/ihoey/sentry_dingtalk_ihoey/issues'),
        ('README', 'https://github.com/ihoey/sentry_dingtalk_ihoey/blob/master/README.md'),
    ]
    version = sentry_dingtalk_ihoey.VERSION

    slug = 'Ding Talk: Robot'
    title = 'Ding Talk: Robot'
    conf_key = slug
    conf_title = title
    project_conf_form = DingTalkOptionsForm

    def is_configured(self, project):
        return bool(self.get_option('access_token', project))

    def notify_users(self, group, event, *args, **kwargs):
        if not self.is_configured(group.project):
            self.logger.info('dingtalk token config error')
            return None

        if self.should_notify(group, event):
            self.logger.info('send msg to dingtalk robot yes')
            self.send_msg(group, event, *args, **kwargs)
        else:
            self.logger.info('send msg to dingtalk robot no')
            return None

    def send_msg(self, group, event, *args, **kwargs):
        del args, kwargs

        # error_title = u'【WARNING】捕获到来自【%s】的异常' % event.project.slug
        error_title = u'【%s】捕获到来自【%s】的异常' % (event.get_tag("level"), event.project.slug)
        # self.logger.info(event.__dict__)

        data = {
            "msgtype": 'markdown',
            "markdown": {
                "title": error_title,
                "text": u'#### {title} \n\n > {message} \n\n > {release} \n\n > {environment} \n\n [查看详情]({url})'.format(
                    title=error_title,
                    message=event.title,
                    release=event.get_tag("release"),
                    environment=event.get_tag("environment"),
                    url=u'{url}events/{id}/'.format(
                        url=group.get_absolute_url(),
                        id=event.event_id
                    ),
                )
            }
        }

        requests.post(
            url=DING_TALK_API.format(token=self.get_option('access_token', group.project)),
            headers={
                'Content-Type': 'application/json'
            },
            data=json.dumps(data).encode('utf-8')
        )
