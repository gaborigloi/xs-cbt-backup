import cbt_test_lib
import os


class CBTTests(object):
    def __init__(self, pool_master, host=None, username=None, password=None):
        username = username or os.environ['XS_USERNAME']
        password = password or os.environ['XS_PASSWORD']
        self._pool_master = pool_master
        self._host = host or pool_master
        self._username = username
        self._password = password
        self._session = cbt_test_lib.create_session(
            pool_master=pool_master, username=username, password=password)

    def create_test_session(self):
        session = cbt_test_lib.create_test_session(
            pool_master=self._pool_master,
            username=self._username,
            password=self._password)
        print(session)

    def create_test_vdi(self, sr=None):
        vdi = cbt_test_lib.create_test_vdi(
            session=self._session, host=self._host, sr=sr)
        print(self._session.xenapi.VDI.get_uuid(vdi))

    def read_from_vdi(self, vdi=None):
        cbt_test_lib.read_from_vdi(
            session=self._session, host=self._host, vdi=vdi)

    def loop_connect_disconnect(self, vdi=None, n=1000):
        cbt_test_lib.loop_connect_disconnect(
            session=self._session, host=self._host, vdi=vdi, n=n)


if __name__ == '__main__':
    import fire
    fire.Fire(CBTTests)
