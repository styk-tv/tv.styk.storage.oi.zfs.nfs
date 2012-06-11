import subprocess

def zpool_status():
    output = subprocess.Popen(['zpool', 'status'], stdout=subprocess.PIPE).communicate()[0]
    out_list = []
    key = ''
    out_dict = {}
    for line in output.splitlines():
        if ':' in line:
            key, value = line.split(':')
            if key.strip() == 'pool' and out_dict:
                out_list.append(out_dict)
                out_dict = {}
            if value:
                out_dict[key.strip()] = value.strip()
            else:
                out_dict[key.strip()] = []
        else:
            if line:
                out_dict[key].append(line.strip())
    out_list.append(out_dict)
    return out_list
