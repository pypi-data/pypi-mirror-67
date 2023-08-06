from tests.modified_environ import modified_environ
from enough import cmd


def test_playbook(capsys, mocker):
    # do not tamper with logging streams to avoid
    # ValueError: I/O operation on closed file.
    mocker.patch('cliff.app.App.configure_logging')
    mocker.patch('enough.common.ansible_utils.Playbook.run_from_cli',
                 side_effect=lambda **kwargs: print('PLAYBOOK'))
    assert cmd.main(['playbook']) == 0
    out, err = capsys.readouterr()
    assert 'PLAYBOOK' in out


def test_service(capsys, mocker):
    # do not tamper with logging streams to avoid
    # ValueError: I/O operation on closed file.
    mocker.patch('cliff.app.App.configure_logging')
    name = 'abc'
    fqdn = f'{name}.example.com'

    class Service(object):
        def create_or_update(self):
            return {'fqdn': fqdn}

    mocker.patch('enough.common.service.service_factory',
                 return_value=Service())
    assert cmd.main(['--debug', 'service', 'create', name]) == 0
    out, err = capsys.readouterr()
    assert fqdn in out


def test_openstack(capsys, mocker):
    # do not tamper with logging streams to avoid
    # ValueError: I/O operation on closed file.
    mocker.patch('cliff.app.App.configure_logging')
    mocker.patch('enough.common.openstack.OpenStack.run',
                 side_effect=lambda *args, **kwargs: print('OPENSTACK'))
    with modified_environ(OS_CLIENT_CONFIG_FILE="/dev/null"):
        assert cmd.main(['openstack', '--debug', 'help']) == 0
    out, err = capsys.readouterr()
    assert 'OPENSTACK' in out
