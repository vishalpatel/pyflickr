#!/usr/bin/python
"""
@author: vishal patel
@email: vkpatel@cmu.edu
"""
import re,ipaddr,sys,optparse
regobj = re.compile('\d+\.\d+\.\d+\.\d+\s+');

def get_ip_range(s):
	global regobj;
	#print s;
	ipaddrs = regobj.findall(s);
	#print ipaddrs;
	if len(ipaddrs)<2 :
		return "Bad";
	addr_range = ipaddr.summarize_address_range(ipaddr.IPAddress(ipaddrs[0].strip()) , ipaddr.IPAddress(ipaddrs[1].strip()) );
	
	return_str = "%s" %addr_range[0];
	return return_str

def format_CIDR(s):
	s=s.strip()
	parts = s.split('/')
	if len(parts) < 2:
		print >> sys.stderr, "Bad String %s #req format xx.xx/dd";
		return "";
	numdots = parts[0].count('.')
	for i in range(numdots,3):
		parts[0]=parts[0]+'.0';
	return parts[0]+"/"+parts[1];

usage="usage: try giving inputs";


parser = optparse.OptionParser(usage=usage)
parser.add_option("-f", "--format",
                  action="store_true", default=False,
                  help="format ips to standard format. Eg. 24.5/8 => 24.5.0.0/8 [default]")
parser.add_option("-r", "--range",
                  action="store_true", default=False,
                  help="convert ip range to prefix format.")


def main():
	(options,args)=parser.parse_args()

	if options.format:
		#do the code for find & replace of each string with formatted ip
		searchre = re.compile('\d+\.?\d+?\.?\d+?\.?\d+?\/\d+\s');
		for line in sys.stdin:
			if len(searchre.findall(line)) ==0:
				print line;
			else:
				strs = searchre.findall(line);
				#print strs;
				for s in strs:
					ns=format_CIDR(s.strip())
					#print ns;
					line=line.replace(s,ns)
				print line;
		sys.exit(0);
	if options.range:
		for line in sys.stdin:
			sth = get_ip_range(line);
			print "%s" %sth;
		sys.exit(0);

if __name__ == '__main__':
	main();
