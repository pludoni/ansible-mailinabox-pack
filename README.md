# Mail-in-A-Box workarounds (Ubuntu Xenial 16.04)

First, This role creates some very basic setup for Mail-in-a-Box using our Mailinabox fork.
Further, it adds some features that we need, that are not part of Mail-in-a-Box, such as:

**Attentation** Mail-in-a-Box is not yet compatible with Ubuntu 16.04 in the master branch, we are using a fork.

### Dovecot Adjustments

* POP3s enabled
* Adds the names "spam" "junk" "inbox/Junk-E-Mail" to the list of Spamfolders that Spamassassin regards as Spam folders for learning

### Postfix Adjustments

* Postfix queue lifetime tuning - Reducing the time that a mail is kept in the queue down to 30m
* Optional Graylist disabling - For a company server this is not very useful, most customers have a new domain name and one needs to wait a long time
* Optional Allow all authenticated users to write a mail as anybody - We trust our employees and we have some usecases where employees use that, or we have an API mail user that needs to post as anybody
* Creates a "noreply@" Alias that writes to /dev/null
* Creates a (sorry, German) landing page on the website with instructions for users how to setup thunderbird/outlook
* Creates any number of virtual bouncer domains, such as "bounce@mydomain". All e-mails sent to that mail are POSTed to a HTTP url of your choice for postprocessing of your App. Very useful in combination with the + autotag, like "bounce+f73a3802@yourdomain.de" to identify conversations


## Playbook


```yaml
---
- hosts: mailer
  vars:
  roles:
    - role: pludoni.mailinabox
      # using a fork that seems to work with Ubuntu 16.04
      mailinabox_ref: 'ubuntu16.04'
      mailinabox_repo: 'https://github.com/pludoni/mailinabox.git'
      postfix_disable_graylisting: yes
      postfix_allow_all_users_to_send_as_any: yes
      create_noreply_alias: yes
      mail_bouncer_aliases:
        - name: 'bounces'
          url: 'https://yourapp.com/bounce_api?access_token=123'
```

The aliases created by "create_noreply_alias" and "mail_bouncer_aliases" only work, if you create a Mail alias in the Mail-in-a-box UI, such as:

* bounces@yourdomain.de -> bounces@localhost.localdomain
* noreply@yourdomain.de -> noreply@localhost.localdomain
