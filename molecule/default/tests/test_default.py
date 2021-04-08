import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_host(host):
    assert host.file("/opt/shfmt/v3.2.4/bin/shfmt").exists

    cmd = host.run("/opt/shfmt/v3.2.4/bin/shfmt --version")
    print(cmd)
    assert cmd.stdout == "v3.2.4\n"
