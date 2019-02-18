import logging
import os
import subprocess
import time

from tenacity import retry, stop_after_attempt

logger = logging.getLogger(__name__)


def clear_ap_name(ap_name):
    return ap_name.replace('(', '').replace(')', '')


class CreateApHelper:

    @staticmethod
    def list_ap_running():
        aps = []
        try:
            p = subprocess.run(['create_ap', '--list-running'], stdout=subprocess.PIPE)
            if p.returncode == 0:
                aps = [{'wiface': x.split()[1], 'wlan': clear_ap_name(x.split()[2])} for x in
                       p.stdout.decode("utf-8").split('\n')[2:] if len(x) > 2]
        except Exception:
            pass
        return aps

    @staticmethod
    def stop_ap(ap_name):
        try:
            p = subprocess.run(["create_ap", '--stop', ap_name], stdout=subprocess.PIPE)
            if p.returncode == 0:
                return True
        except Exception:
            pass
        return False

    @staticmethod
    @retry(reraise=True, stop=stop_after_attempt(3))
    def create_ap(wiface, bridge, ssid, password, virt_prefix, channel=1, wpa_version="1+2", timeout=30):
        try:
            logger.info("Create AP {}".format(virt_prefix))

            ap_running = [ap['wlan'] for ap in CreateApHelper.list_ap_running() if virt_prefix in ap['wlan']]

            os.system('nmcli r wifi off')
            os.system('rfkill unblock wlan')

            os.system(
                'create_ap -m bridge {} {} {} {} --virt-prefix {} -c {} -w {} --no-dns --daemon'.format(wiface, bridge,
                                                                                                        ssid, password,
                                                                                                        virt_prefix,
                                                                                                        channel,
                                                                                                        wpa_version))
            logger.info("Creating AP {}, waiting {}".format(virt_prefix, timeout))
            # proc = subprocess.Popen(
            #     ['create_ap', '-m', 'bridge', wiface, bridge, ssid, password, '--virt-prefix', virt_prefix, '-c',
            #      str(channel), '-w', wpa_version, '--no-dns', '--daemon'])
            #
            # try:
            #     returncode = proc.wait(timeout=timeout)
            #     pass
            # except subprocess.TimeoutExpired:
            #     # proc.kill()
            #     # outs, errs = proc.communicate()
            #     pass

            # waiting for virtual WiFi to be created
            time.sleep(timeout)
            # confirm creation
            last_ap_running = [ap['wlan'] for ap in CreateApHelper.list_ap_running() if virt_prefix in ap['wlan']]
            ap_diff = list(set(last_ap_running) - set(ap_running))
            # if not, recreate
            if not len(ap_diff) > 0:
                raise Exception("The ap was not created")
            # else, return the created virtual WiFi interface
            return list(ap_diff)
        except Exception as e:
            raise Exception("Could not create the ap interface with prefix {}".format(virt_prefix))
