import requests


def send_email(apiKey, subject, body, emails, sender, reply_addresses):
    resp = requests.post(_url('email'), auth={}, json={
        'to': {
            'addresses': emails.split(',')
        },
        'subject': subject,
        'body': body,
        'replyToAddresses': reply_addresses.split(','),
        'sender': sender
    })
    if resp.status_code != 200:
        raise RuntimeError('Cannot send email - HTTP status {}'.format(resp.status_code))
    else:
        print('Email sent successfully!')


def send_templated_email(apiKey, templateId, emails, params={}):
    resp = requests.post(_url('email/templated'), auth={}, json={
        'to': {
            'addresses': emails.split(',')
        },
        'templateId': templateId,
        'parameters': params
    })
    if resp.status_code != 200:
        raise RuntimeError('Cannot send templated email - HTTP status {}'.format(resp.status_code))
    else:
        print('Email sent successfully!')


def _url(path):
    return 'https://api.byteline.io/' + path
