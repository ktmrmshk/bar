import json
from subprocess import check_output


def getUrl(company_name):
    cmd = 'googler --json -n1 {}'.format(company_name)
    ret = check_output(cmd.split())
    obj = json.loads(ret)
    return obj[0]['url']


def run():
    print( getUrl('(株)ＮＴＴデータ') )


if __name__ == '__main__':
    run()
