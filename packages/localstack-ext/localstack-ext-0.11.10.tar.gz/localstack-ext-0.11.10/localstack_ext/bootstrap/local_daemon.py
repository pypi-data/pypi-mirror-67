#!/usr/bin/env python
HfzTp=None
HfzTu=True
HfzTB=Exception
HfzTv=str
HfzTo=len
HfzTc=isinstance
HfzTi=dict
HfzTy=hasattr
HfzTP=int
HfzTG=False
HfzTr=bytes
import os
import sys
import json
import uuid
import socket
import logging
import tempfile
import threading
import subprocess
import boto3
import shutil
import requests
from six.moves.socketserver import ThreadingMixIn
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
LOG=logging.getLogger('local_daemon')
DEFAULT_PORT_LOCAL_DAEMON=4535
DEFAULT_PORT_LOCAL_DAEMON_ROOT=4534
DEFAULT_PORT_S3=4572
DEFAULT_PORT_EC2=4597
ENDPOINT_S3='http://localhost:%s'%DEFAULT_PORT_S3
ENDPOINT_EC2='http://localhost:%s'%DEFAULT_PORT_EC2
LOCAL_BIND_ADDRESS_PATTERN='127.0.100.*'
USED_BIND_ADDRESSES=[]
MAC_NETWORK_INTERFACE='en0'
BUCKET_MARKER_LOCAL='__local__'
class FuncThread(threading.Thread):
 def __init__(self,func,params=HfzTp):
  threading.Thread.__init__(self)
  self.daemon=HfzTu
  self.params=params
  self.func=func
 def run(self):
  try:
   self.func(self.params)
  except HfzTB as e:
   log('Error in thread function: %s'%e)
class ThreadedHTTPServer(ThreadingMixIn,HTTPServer):
 daemon_threads=HfzTu
class RequestHandler(BaseHTTPRequestHandler):
 def do_POST(self):
  self.read_content()
  try:
   result=self.handle_request()
   self.send_response(200)
  except HfzTB as e:
   error_string=HfzTv(e)
   result=json.dumps({'error':error_string})
   self.send_response(500)
  self.send_header('Content-Length','%s'%HfzTo(result)if result else 0)
  self.end_headers()
  if HfzTo(result or ''):
   self.wfile.write(to_bytes(result))
 def handle_request(self):
  request=self.request_json
  result='{}'
  operation=request.get('op','')
  if operation=='getos':
   result={'result':get_os()}
  elif operation=='shell':
   command=request.get('command')
   result=run_shell_cmd(command)
  elif operation=='s3:download':
   result=s3_download(request)
  elif operation.startswith('root:'):
   result=forward_root_request(request)
  elif operation=='kill':
   log('Terminating local daemon process (port %s)'%DEFAULT_PORT_LOCAL_DAEMON)
   os._exit(0)
  else:
   result={'error':'Unsupported operation "%s"'%operation}
  result=json.dumps(result)if HfzTc(result,HfzTi)else result
  return result
 def read_content(self):
  if HfzTy(self,'data_bytes'):
   return
  content_length=self.headers.get('Content-Length')
  self.data_bytes=self.rfile.read(HfzTP(content_length))
  self.request_json={}
  try:
   self.request_json=json.loads(self.data_bytes)
  except HfzTB:
   pass
class RequestHandlerRoot(RequestHandler):
 def handle_request(self):
  request=self.request_json
  result='{}'
  operation=request.get('op')
  if operation=='root:ssh_proxy':
   result=start_ssh_forward_proxy(request)
  elif operation=='kill':
   log('Terminating local daemon process (port %s)'%DEFAULT_PORT_LOCAL_DAEMON_ROOT)
   os._exit(0)
  else:
   result={'error':'Unsupported operation "%s"'%operation}
  result=json.dumps(result)if HfzTc(result,HfzTi)else result
  return result
def s3_download(request):
 bucket=request['bucket']
 key=request['key']
 tmp_dir=os.environ.get('TMPDIR')or tempfile.mkdtemp()
 target_file=os.path.join(tmp_dir,request.get('file_name')or 's3file.%s'%HfzTv(uuid.uuid4()))
 if not os.path.exists(target_file)or request.get('overwrite'):
  if bucket==BUCKET_MARKER_LOCAL:
   shutil.copy(key,target_file)
  else:
   s3=boto3.client('s3',endpoint_url=ENDPOINT_S3)
   log('Downloading S3 file s3://%s/%s to %s'%(bucket,key,target_file))
   s3.download_file(bucket,key,target_file)
 return{'local_file':target_file}
def forward_root_request(request):
 url='http://localhost:%s'%DEFAULT_PORT_LOCAL_DAEMON_ROOT
 response=requests.post(url,data=json.dumps(request))
 return json.loads(to_str(response.content))
def start_ssh_forward_proxy(options):
 path=os.path.dirname(__file__)
 if path not in sys.path:
  sys.path.append(path)
 from tcp_proxy import server_loop
 port=options.get('port')or get_free_tcp_port()
 host=LOCAL_BIND_ADDRESS_PATTERN.replace('*',HfzTv(HfzTo(USED_BIND_ADDRESSES)+2))
 create_network_interface_alias(host)
 USED_BIND_ADDRESSES.append(host)
 log('Starting local SSH forward proxy, %s:22 -> localhost:%s'%(host,port))
 options={'bind_port':22,'bind_addr':host,'port':port}
 FuncThread(server_loop,options).start()
 return{'host':host,'forward_port':port}
def create_network_interface_alias(address,interface=HfzTp):
 sudo_cmd='sudo'
 try:
  interface=interface or MAC_NETWORK_INTERFACE
  run_cmd('{sudo_cmd} ifconfig {iface} alias {addr}'.format(sudo_cmd=sudo_cmd,addr=address,iface=interface))
 except HfzTB:
  run_cmd('{sudo_cmd} ifconfig eth0:0 {addr} netmask 255.255.255.0 up'.format(sudo_cmd=sudo_cmd,addr=address))
def run_shell_cmd(command):
 try:
  return{'result':run_cmd(command)}
 except HfzTB as e:
  error_string=HfzTv(e)
  if HfzTc(e,subprocess.CalledProcessError):
   error_string='%s: %s'%(error_string,e.output)
  return{'error':error_string}
def get_os():
 if is_mac_os():
  return 'macos'
 if is_linux():
  return 'linux'
 return 'windows'
def run_cmd(cmd):
 log('Running command: %s'%cmd)
 return to_str(subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=HfzTu))
def log(*args):
 print(*args)
 sys.stdout.flush()
def is_mac_os():
 try:
  out=to_str(subprocess.check_output('uname -a',shell=HfzTu))
  return 'Darwin' in out
 except subprocess.CalledProcessError:
  return HfzTG
def is_linux():
 try:
  out=to_str(subprocess.check_output('uname -a',shell=HfzTu))
  return 'Linux' in out
 except subprocess.CalledProcessError:
  return HfzTG
def get_free_tcp_port():
 tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 tcp.bind(('',0))
 addr,port=tcp.getsockname()
 tcp.close()
 return port
def to_bytes(obj):
 return obj.encode('utf-8')if HfzTc(obj,HfzTv)else obj
def to_str(obj):
 return obj.decode('utf-8')if HfzTc(obj,HfzTr)else obj
def start_server(port,handler):
 try:
  requests.post('http://localhost:%s'%port,data='{"op":"kill"}')
 except HfzTB:
  pass
 try:
  log('Starting local daemon server on port %s'%port)
  httpd=ThreadedHTTPServer(('0.0.0.0',port),handler)
  httpd.serve_forever()
 except HfzTB:
  log('Local daemon server already running, or port %s not available'%port)
  pass
def main():
 logging.basicConfig()
 daemon_type=sys.argv[1]if HfzTo(sys.argv)>1 else 'main'
 os.environ['AWS_ACCESS_KEY_ID']=os.environ.get('AWS_ACCESS_KEY_ID')or 'test'
 os.environ['AWS_SECRET_ACCESS_KEY']=os.environ.get('AWS_SECRET_ACCESS_KEY')or 'test'
 if daemon_type=='main':
  start_server(DEFAULT_PORT_LOCAL_DAEMON,RequestHandler)
 elif daemon_type=='root':
  start_server(DEFAULT_PORT_LOCAL_DAEMON_ROOT,RequestHandlerRoot)
 else:
  log('Unexpected local daemon type: %s'%daemon_type)
def start_in_background():
 from localstack.config import TMP_FOLDER
 from localstack.utils.common import run
 log_file=os.path.join(TMP_FOLDER,'localstack_daemon.log')
 LOG.info('Logging local daemon output to %s'%log_file)
 python_cmd=sys.executable
 cmd='%s %s'%(python_cmd,__file__)
 run(cmd,outfile=log_file,asynchronous=HfzTu)
 LOG.info('Attempting to obtain sudo privileges for local daemon of EC2 API '+'(required to start SSH forward proxy on privileged port 22). '+'You may be asked for your sudo password.')
 run('sudo ls',stdin=HfzTu)
 def start_root_daemon(*args):
  cmd='%s %s root >> %s'%(python_cmd,__file__,log_file)
  run(cmd,outfile=log_file,stdin=HfzTu)
 FuncThread(start_root_daemon).start()
if __name__=='__main__':
 main()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
