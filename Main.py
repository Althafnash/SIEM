import subprocess

es = subprocess.Popen(r'D:\elasticsearch-9.0.3\bin\elasticsearch.bat', shell=True)
kib = subprocess.Popen(r'D:\kibana-9.0.3\bin\kibana.bat', shell=True)

es.wait()
kib.wait()