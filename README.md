Ansible role for shfmt
==================================

Installs shfmt

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-shfmt/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-shfmt/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-shfmt/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-shfmt/actions?query=workflow%3A%22Release%22)


Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `shfmt_root_directory` | Where to install shfmt | string | `/opt/shfmt` | `false` |
| `shfmt_version` | Version of shfmt to install | string | `v3.2.4` | `false` |

Install Directory
-----------------

By default, `shfmt` will be installed in `/opt/shfmt/$version/bin/shfmt`

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-shfmt
      vars:
        shfmt_version: v3.2.4
```

License
-------

[Apache License](LICENSE)
