"""
@author: vishal patel
@email: vkpatel@cmu.edu
"""
import urllib,re,commands;

def sendmail(to='vkpatel@cmu.edu', subject='autmaticmail', contents='~Zues coder'):
        uriparams=urllib.urlencode([('to',emailstr),('subject',subject),('contents',contents)])
        httpurl='http://vishal.chaoticmind.org/mynew.php?'+uriparams
        resp=urllib.urlopen(httpurl);

def fetchurl(url='http://www.cbdr.cmu.edu/experiments/index.asp'):
        resp = urllib.urlopen(url);
        exp = re.compile('<b>(.*?)<\/b>');
        data=exp.findall(resp.read());
        data.sort(); 
        return data;

def savedata(filename=u'filedata.txt',data=[]):
        fh = open(str(filename),"w");
        for l in data:
                if l =='Scheduled Times':
                        continue;
                fh.write(str(l)+"\n");

        fh.close();

if __name__ == '__main__':
        d = fetchurl();
        savedata(data=d);
		s = commands.getstatusoutput("diff filedata.txt oldfiledata.txt")[1];
		if len(s) >0:
			sendmail(contents=s+"\n\n Thanks\nVishal patel");
			print "sent mail";
		commands.getstatusoutput("mv filedata.txt oldfiledata.txt");
