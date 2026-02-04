import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("dnsmasq"),
    ],
)
def test_dependencies_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_dnsmasq_service_is_running(host):
    service = host.service("dnsmasq")
    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize(
    "path,user,group,mode",
    [
        ("/etc/dnsmasq.d/cache", "root", "root", 0o644),
        ("/etc/dnsmasq.d/main", "root", "root", 0o644),
    ],
)
def test_config_files_exist(host, path, user, group, mode):
    config = host.file(path)
    assert config.exists
    assert config.is_file
    assert config.user == user
    assert config.group == group
    assert config.mode == mode


def test_main_config_contains_expected_settings(host):
    config = host.file("/etc/dnsmasq.d/main")
    assert config.contains("listen-address=127.0.0.1")
    assert config.contains("bind-interfaces")


def test_cache_config_contains_expected_settings(host):
    config = host.file("/etc/dnsmasq.d/cache")
    assert config.contains("server=8.8.8.8")
    assert config.contains("cache-size=500")


def test_dnsmasq_command_is_available(host):
    cmd = host.run("which dnsmasq")
    assert cmd.rc == 0
