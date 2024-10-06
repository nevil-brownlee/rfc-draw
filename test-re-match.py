
import re, sys

rere_0_4 = "(\d+)\s+\((.+)\s+(.+)\)\s+\[(.+)\]\s+\"(.+)\""  # works
    # field   0        1      2          3          4
    #       objid    type    skey       coords     text 
rere_v1 = rere_0_4 + "\s+(\S)\s+([\s\S]+)\Z"
    # rdd v1:              5      6
    #                     g_nbr  g_type
    #                   '0  N' or '1 group'

#rere_v2 = rere_0_4 + "\s+(\d+)\s+(\d+)\s+(\d+)\Z"
rere_v2 = rere_0_4 + "\s+(\S+)\s+(\S+)\s+(\S+)(\s.+)?"
    #                      5       6       7    8
    #              parent_id,     v1,     v2,   Optional comment

rdd_e_0_4 = re.compile(rere_0_4)
rdd_e_v1 = re.compile(rere_v1)
rdd_e_v2 = re.compile(rere_v2)

#ev2_split = rdd_e_v2.split(line)
#    returns '' as first and last chars of result <<<

def parse_rdd_line(line):
    line = line.rstrip()
    print("line = >%s<" % line)
    #if rdd_e_0_4.match(line):  # v2 match (5 fields)
    #    m = rdd_e_v2.split(line)
    #3    print("0_4 split %s len %d" % (m, len(m)))
    #else:
    #    print("Couldn't match 0_4 .rdd")
    hx = line.find("#")
    if hx == 0:
        print("* # in col 0, ignore")
    else:
        if rdd_e_v2.match(line):  # v2 match (7 fields)
            m = rdd_e_v2.split(line)
            print("v2 split %s len %d" % (m, len(m)))
        else:
            print("Couldn't match v1 or v2 .rdd")
    return hx
        
#f_name = "RFC2722-TM-Architecture.rdd"
#f_name = "qqq-text.rdd"
#f_name = "test-n_rect.rdd"
#f_name = "RFC2722-TM-Architecture-v2.rdd"
#f_name = "save-mpm.rdd"
#f_name = "monospace-text+line.rdd"
#f_name = "RFC9293-TCP.rdd"
f_name = sys.argv[1]
print("Reading file %s" % f_name)
rdd_f = open(f_name)
j = 0
for line in rdd_f:
    j += 1
    if j >= 4:
        hx = parse_rdd_line(line)
        #if hx < 0:
        #    break
rdd_f.close()
