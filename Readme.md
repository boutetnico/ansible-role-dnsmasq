[![tests](https://github.com/boutetnico/ansible-role-dnsmasq/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-dnsmasq/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.dnsmasq-blue.svg)](https://galaxy.ansible.com/boutetnico/dnsmasq)

ansible-role-dnsmasq
====================

This role installs and configures dnsmasq.

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)

Role Variables
--------------

| Variable             | Required | Default             | Choices   | Comments                                 |
|----------------------|----------|---------------------|-----------|------------------------------------------|
| dnsmasq_dependencies | true     | `dnsmasq`           | string    |                                          |
| dnsmasq_conf         | true     | `{}`                | dict      |                                          |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-dnsmasq
          dnsmasq_conf:
            main:
              - listen-address=127.0.0.1
              - bind-interfaces
            cache:
              - no-resolv
              - server=8.8.8.8
              - server=8.8.4.4
              - cache-size=500
              - neg-ttl=60
              - domain-needed
              - bogus-priv

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
