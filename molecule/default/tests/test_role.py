import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("dnsmasq"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "username,groupname,path",
    [
        ("root", "root", "/etc/dnsmasq.d/cache"),
        ("root", "root", "/etc/dnsmasq.d/main"),
    ],
)
def test_config_files(host, username, groupname, path):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == username
    assert config.group == groupname
